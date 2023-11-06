import io

from PyQt5 import uic

design_SQL = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1231</width>
    <height>606</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>History</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(0, 0, 45);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QGridLayout" name="gridLayout">
    <item row="1" column="1">
     <widget class="QComboBox" name="language_history">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(255, 255, 255);
font: 10pt &quot;Arial Rounded MT Bold&quot;;</string>
      </property>
      <item>
       <property name="text">
        <string>Английский</string>
       </property>
      </item>
      <item>
       <property name="text">
        <string>Арабский</string>
       </property>
      </item>
      <item>
       <property name="text">
        <string>Греческий</string>
       </property>
      </item>
      <item>
       <property name="text">
        <string>Испанский</string>
       </property>
      </item>
      <item>
       <property name="text">
        <string>Итальянский</string>
       </property>
      </item>
      <item>
       <property name="text">
        <string>Китайский</string>
       </property>
      </item>
      <item>
       <property name="text">
        <string>Корейский</string>
       </property>
      </item>
      <item>
       <property name="text">
        <string>Немецкий</string>
       </property>
      </item>
      <item>
       <property name="text">
        <string>Польский</string>
       </property>
      </item>
      <item>
       <property name="text">
        <string>Португальский</string>
       </property>
      </item>
      <item>
       <property name="text">
        <string>Румынский</string>
       </property>
      </item>
      <item>
       <property name="text">
        <string>Русский</string>
       </property>
      </item>
      <item>
       <property name="text">
        <string>Турецкий</string>
       </property>
      </item>
      <item>
       <property name="text">
        <string>Украинский</string>
       </property>
      </item>
      <item>
       <property name="text">
        <string>Французкий</string>
       </property>
      </item>
      <item>
       <property name="text">
        <string>Японский</string>
       </property>
      </item>
     </widget>
    </item>
    <item row="1" column="0">
     <widget class="QLabel" name="label">
      <property name="styleSheet">
       <string notr="true">color: rgb(255, 255, 255);
font: 20pt &quot;Countless&quot;;</string>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;Your translation history&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
    </item>
    <item row="0" column="1">
     <widget class="QLabel" name="label_2">
      <property name="styleSheet">
       <string notr="true">color: rgb(255, 255, 255);
font: 9pt &quot;Countless&quot;;</string>
      </property>
      <property name="text">
       <string>Language history sorted</string>
      </property>
     </widget>
    </item>
    <item row="3" column="1">
     <widget class="QPushButton" name="sort_button">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(49, 49, 49);
color: rgb(255, 255, 255);
font: 10pt &quot;Arial Rounded MT Bold&quot;;</string>
      </property>
      <property name="text">
       <string>SORT</string>
      </property>
     </widget>
    </item>
    <item row="10" column="1">
     <widget class="QPushButton" name="clear_button">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(49, 49, 49);
color: rgb(255, 255, 255);
font: 10pt &quot;Arial Rounded MT Bold&quot;;</string>
      </property>
      <property name="text">
       <string>CLEAR ALL HISTORY</string>
      </property>
     </widget>
    </item>
    <item row="3" column="0">
     <widget class="QPushButton" name="mood_button">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(49, 49, 49);
color: rgb(255, 255, 255);
font: 10pt &quot;Arial Rounded MT Bold&quot;;</string>
      </property>
      <property name="text">
       <string>Кнопка хорошего настроения)</string>
      </property>
     </widget>
    </item>
    <item row="5" column="0">
     <widget class="QTableWidget" name="tableWidget">
      <property name="styleSheet">
       <string notr="true">color: rgb(143, 143, 143);
background-color: rgb(0, 0, 46);</string>
      </property>
     </widget>
    </item>
    <item row="5" column="1">
     <widget class="QPushButton" name="delete_button">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(49, 49, 49);
color: rgb(255, 255, 255);
font: 10pt &quot;Arial Rounded MT Bold&quot;;</string>
      </property>
      <property name="text">
       <string>DELETE THIS TRANSLATE</string>
      </property>
     </widget>
    </item>
    <item row="10" column="0">
     <widget class="QPushButton" name="update_button">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(49, 49, 49);
color: rgb(255, 255, 255);
font: 10pt &quot;Arial Rounded MT Bold&quot;;</string>
      </property>
      <property name="text">
       <string>UPDATE HISTORY DATA</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources>
  <include location="../../../Downloads/imade_dvoichni.qrc"/>
 </resources>
 <connections/>
</ui>
'''


class QdesignHistoryWindow(object):
    def setupUi(self, MainWindow):
        super().__init__()
        desig_3 = io.StringIO(design_SQL)
        uic.loadUi(desig_3, self)
