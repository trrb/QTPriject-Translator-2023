from design_WelcomeWindow import QdesignWelcomeWindow
from design_simple_translate import QdesignSimpletranslate
from design_translate_history import QdesignHistoryWindow
from design_txt_translate import QdesignTxtTranslate
from design_buttons_value import QdesignButtonsValue
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, \
    QLabel, QTableWidgetItem
import sqlite3
from googletrans import Translator

SCREEN_SIZE = [405, 400]
lang_in_code = {'Английский': 'en',
                'Румынский': 'ro',
                'Турецкий': 'tr',
                'Польский': 'pl',
                'Арабский': 'ar',
                'Итальянский': 'it',
                'Русский': 'ru',
                'Китайский': 'zh-TW',
                'Корейский': 'ko',
                'Украинский': 'uk',
                'Греческий': 'el',
                'Португальский': 'pt',
                'Немецкий': 'de',
                'Испанский': 'es',
                'Японский': 'ja',
                'Французкий': 'fr'}


# Класс отвечающий за окно истории переводов (вторая кнопка)
class SQLWigetHistory(QMainWindow, QdesignHistoryWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.box = TRRBBox()
        with sqlite3.connect('translation_history_db.db') as db:
            cur = db.cursor()
            result_rows = cur.execute('''SELECT id FROM history''').fetchall()
            result_orig = cur.execute(
                '''SELECT original_text FROM history''').fetchall()
            result_translated = cur.execute(
                '''SELECT translated_text FROM history''').fetchall()
            result_language = cur.execute(
                '''SELECT language FROM history''').fetchall()
            self.tableWidget.setRowCount(len(result_rows))
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setColumnWidth(0, 10)
            self.tableWidget.setColumnWidth(1, 400)
            self.tableWidget.setColumnWidth(2, 400)
            for i, elem in enumerate(result_rows):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
            for i, elem in enumerate(result_orig):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j + 1,
                                             QTableWidgetItem(str(val)))
            for i, elem in enumerate(result_translated):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j + 2,
                                             QTableWidgetItem(str(val)))
            for i, elem in enumerate(result_language):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j + 3,
                                             QTableWidgetItem(str(val)))
        self.mood_button.clicked.connect(self.moodfunction)
        self.delete_button.clicked.connect(self.delete_buttonClicked)
        self.clear_button.clicked.connect(self.delete_all)
        self.sort_button.clicked.connect(self.sort_function)
        self.update_button.clicked.connect(self.updateClick)

    def updateClick(self):
        pass

    def sort_function(self):
        with sqlite3.connect('translation_history_db.db') as db:
            cur = db.cursor()
            result = cur.execute(
                f"""SELECT * FROM history WHERE language = (SELECT id FROM languages WHERE name = '{self.language_history.currentText()}')""").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setColumnWidth(0, 10)
        self.tableWidget.setColumnWidth(1, 400)
        self.tableWidget.setColumnWidth(2, 400)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def delete_all(self):
        with sqlite3.connect('translation_history_db.db') as db:
            cur = db.cursor()
            cur.execute('''DELETE FROM history WHERE id > -1''').fetchone()
            db.commit()
        self.tableWidget.setRowCount(0)

    def delete_buttonClicked(self):
        row = self.tableWidget.currentRow()
        if row != self.tableWidget.rowCount() - 1:
            with sqlite3.connect('translation_history_db.db') as db:
                cur = db.cursor()
                cell = self.tableWidget.itemAt(0, row).text()
                cur.execute(
                    f"""DELETE FROM history WHERE id = {int(cell) + (row)}""")
                db.commit()
                if row > -1:
                    self.tableWidget.removeRow(row)
        else:
            with sqlite3.connect('translation_history_db.db') as db:
                cur = db.cursor()
                cur.execute(
                    f"""DELETE FROM history WHERE id = (SELECT max(id) FROM history)""")
                db.commit()
                if row > -1:
                    self.tableWidget.removeRow(row)

    def moodfunction(self):
        self.box.show()


# Класс отвечающий за окно "Помощи"
class ButtonsValue(QMainWindow, QdesignButtonsValue):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


# Класс кнопки "хорошего настроения"
class TRRBBox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 420, *SCREEN_SIZE)
        self.setWindowTitle('Хорошего настроения!')
        self.pixmap = QPixmap('TRRTranslateBOX.png')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(400, 400)
        # Отображаем содержимое QPixmap в объекте QLabel
        self.image.setPixmap(self.pixmap)


# Класс отвечающий за перевод txt файлов (третья кнопка)
class Txtfiles_translate(QMainWindow, QdesignTxtTranslate):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('TXTfilesTranslate')
        self.fname = None
        self.language.model().sort(0)
        self.status = self.statusBar()
        self.status.setStyleSheet(
            "QStatusBar{padding-left:8px;color:white;font-weight:bold;}")
        self.name_file_button.clicked.connect(self.txttranslate)
        self.translatebutton.clicked.connect(self.translate_file_button)
        self.clear_button.clicked.connect(self.clear_func)
        self.save_button.clicked.connect(self.save_function_txtfiles)

    def save_function_txtfiles(self):
        with sqlite3.connect('translation_history_db.db') as db:
            cur = db.cursor()
            print(1)
            lang = self.language.currentText()
            if self.name_file_button.text() != 'paste your file here':
                if self.text_of_new_file.toPlainText() != '':
                    id_language = cur.execute(
                        f'''SELECT id FROM languages WHERE name = "{lang}"''').fetchall()
                    cur.execute(f'''
                    INSERT INTO history(original_text, translated_text, language)
                    VALUES("{self.text_of_your_file.toPlainText()}", "{self.text_of_new_file.toPlainText()}", {id_language[0][0]})''').fetchall()
                    db.commit()
                else:
                    self.status.showMessage('Сначала переведите выбраный файл')
            else:
                self.status.showMessage(
                    'Выберите файл и переведите его перед сохранением')

    # Функция для изменения названия кнопки выбора файла,
    # копирование его пути в переменную self.fname и
    # копирование текста из файла
    def txttranslate(self):
        text_wanted = ''
        fname = QFileDialog.getOpenFileName(self, 'Выберите текст-файл', '',
                                            'Файл (*.txt)')[0]
        file_name = fname.split('/')
        self.name_file_button.setText(f'{file_name[-1]}')
        with open(fname, 'r', encoding='UTF-8') as f:
            file = f.readlines()
        for i in file:
            text_wanted += f'{i}'
        self.text_of_your_file.setText(text_wanted)
        self.fname = fname

    # функция перевода всего файла построчно
    def translate_file(self, file_path, target_lang):
        translator = Translator()
        list_translate = []
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.readlines()
        for i in range(len(text)):
            translation = translator.translate(i, dest=target_lang)
            list_translate.append(translation)
        return list_translate

    def translate_text(self, text, target_lang):
        translator = Translator()
        translation = translator.translate(text, dest=target_lang)
        return translation.text

    # функция кнопки чистки полей
    def clear_func(self):
        if self.text_of_your_file.toPlainText() == '' and self.text_of_new_file.toPlainText() == '':
            self.status.showMessage('Ваши поля уже пусты.')
        else:
            self.name_file_button.setText('paste your file here')
            self.text_of_your_file.clear()
            self.text_of_new_file.clear()

    # функция кнопки перевода файла
    def translate_file_button(self):
        text = self.text_of_your_file.toPlainText()
        if text != '':
            self.text_of_new_file.setText(self.translate_text(text,
                                                              lang_in_code[
                                                                  self.language.currentText()]))
        else:
            self.status.showMessage('Выберите файл.')


# Класс отвечающий за начальное окно
class TranslatorWelcomeWindow(QMainWindow, QdesignWelcomeWindow):
    def __init__(self, *arg):
        super().__init__(*arg)
        self.setupUi(self)
        self.transportate = Translator_second()
        self.buttonsvalue = ButtonsValue()
        self.SQLWIGET = SQLWigetHistory()
        self.txt = Txtfiles_translate()
        self.action.triggered.connect(lambda: self.buttons_value())
        self.newtranslation_button.clicked.connect(
            self.transition_second_window)
        self.translationhistory_button.clicked.connect(self.sqlWiget_function)
        self.translatetxtfile_button.clicked.connect(self.txtButtonTranslate)

    def txtButtonTranslate(self):
        self.txt.show()

    def buttons_value(self):
        self.buttonsvalue.show()

    def sqlWiget_function(self):
        self.SQLWIGET.show()

    def transition_second_window(self):
        self.transportate.show()


# Класс отвечающий за окно обычного переводчика (вторая кнопка)
class Translator_second(QMainWindow, QdesignSimpletranslate):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Сортировка моделей QComboBox по алфавиту
        self.language.model().sort(0)
        self.status = self.statusBar()
        self.status.setStyleSheet(
            "QStatusBar{padding-left:8px;color:white;font-weight:bold;}")
        self.translatebutton.clicked.connect(self.translate_data)
        self.clear_button.clicked.connect(self.clear_function)
        self.save_button.clicked.connect(self.save_function)

    def save_function(self):
        with sqlite3.connect('translation_history_db.db') as db:
            cur = db.cursor()
            lang = self.language.currentText()
            if self.textEdit.toPlainText() != '':
                if self.textEdit_2.toPlainText() != '':
                    if self.textEdit_2.toPlainText() == self.translate_text(
                            self.textEdit.toPlainText(),
                            lang_in_code[self.language.currentText()]):
                        id_language = cur.execute(
                            f'''SELECT id FROM languages WHERE name = "{lang}"''').fetchall()
                        cur.execute(f'''
                        INSERT INTO history(original_text, translated_text, language)
                        VALUES("{self.textEdit.toPlainText()}", "{self.textEdit_2.toPlainText()}", {id_language[0][0]})''').fetchall()
                        db.commit()
                    else:
                        self.status.showMessage(
                            'Сначала переведите текст на выбранный язык')
                else:
                    self.status.showMessage(
                        'Сначала переведите введенный текст')
            else:
                self.status.showMessage(
                    'Сначала введите текст и переведите его')

    def clear_function(self):
        if self.textEdit.toPlainText() == '' and self.textEdit_2.toPlainText() == '':
            self.status.showMessage('Ваши поля уже пусты.')
        else:
            self.textEdit.clear()
            self.textEdit_2.clear()

    # Функция для перевода входного текста
    def translate_text(self, text, target_lang):
        translator = Translator()
        translation = translator.translate(text, dest=target_lang)
        return translation.text

    # Функция вывода перевода во второй QTextEdit
    def translate_data(self):
        question = self.textEdit.toPlainText()
        if question != '':
            self.textEdit_2.setText(self.translate_text(question, lang_in_code[
                self.language.currentText()]))
        else:
            self.status.showMessage('Введите текст.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TranslatorWelcomeWindow()
    ex.show()
    sys.exit(app.exec_())
