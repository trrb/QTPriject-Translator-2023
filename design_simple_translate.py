import io

from PyQt5 import uic

second_design = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>608</width>
    <height>621</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>TranslateWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(27, 27, 27);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QHBoxLayout" name="horizontalLayout">
    <item>
     <widget class="QWidget" name="widget" native="true">
      <widget class="QComboBox" name="language">
       <property name="geometry">
        <rect>
         <x>330</x>
         <y>300</y>
         <width>211</width>
         <height>31</height>
        </rect>
       </property>
       <property name="cursor">
        <cursorShape>WhatsThisCursor</cursorShape>
       </property>
       <property name="toolTip">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;what language to translate into&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
       <property name="whatsThis">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(85, 116, 144);</string>
       </property>
       <item>
        <property name="text">
         <string>Английский</string>
        </property>
       </item>
       <item>
        <property name="text">
         <string>Румынский</string>
        </property>
       </item>
       <item>
        <property name="text">
         <string>Турецкий</string>
        </property>
       </item>
       <item>
        <property name="text">
         <string>Польский</string>
        </property>
       </item>
       <item>
        <property name="text">
         <string>Арабский</string>
        </property>
       </item>
       <item>
        <property name="text">
         <string>Итальянский</string>
        </property>
       </item>
       <item>
        <property name="text">
         <string>Русский</string>
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
         <string>Украинский</string>
        </property>
       </item>
       <item>
        <property name="text">
         <string>Греческий</string>
        </property>
       </item>
       <item>
        <property name="text">
         <string>Португальский</string>
        </property>
       </item>
       <item>
        <property name="text">
         <string>Немецкий</string>
        </property>
       </item>
       <item>
        <property name="text">
         <string>Испанский</string>
        </property>
       </item>
       <item>
        <property name="text">
         <string>Японский</string>
        </property>
       </item>
       <item>
        <property name="text">
         <string>Французкий</string>
        </property>
       </item>
      </widget>
      <widget class="QPushButton" name="translatebutton">
       <property name="geometry">
        <rect>
         <x>40</x>
         <y>220</y>
         <width>491</width>
         <height>61</height>
        </rect>
       </property>
       <property name="sizePolicy">
        <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="cursor">
        <cursorShape>PointingHandCursor</cursorShape>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(99, 134, 167); 
font: 81 12pt &quot;Rockwell Extra Bold&quot;;
border-radius: 30px;  </string>
       </property>
       <property name="text">
        <string>translate</string>
       </property>
      </widget>
      <widget class="QTextEdit" name="textEdit">
       <property name="geometry">
        <rect>
         <x>20</x>
         <y>60</y>
         <width>541</width>
         <height>151</height>
        </rect>
       </property>
       <property name="cursor" stdset="0">
        <cursorShape>IBeamCursor</cursorShape>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(44, 44, 44);
color: rgb(255, 255, 255);
font: 12pt &quot;Rockwell&quot;;</string>
       </property>
      </widget>
      <widget class="QTextEdit" name="textEdit_2">
       <property name="geometry">
        <rect>
         <x>20</x>
         <y>340</y>
         <width>541</width>
         <height>151</height>
        </rect>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(44, 44, 44);
color: rgb(255, 255, 255);
font: 12pt &quot;Rockwell&quot;;</string>
       </property>
      </widget>
      <widget class="QLabel" name="label_2">
       <property name="geometry">
        <rect>
         <x>20</x>
         <y>20</y>
         <width>191</width>
         <height>31</height>
        </rect>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(99, 134, 167); 
font: 81 12pt &quot;Rockwell Extra Bold&quot;;
border-radius: 10px;  </string>
       </property>
       <property name="text">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;enter the text:&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
      </widget>
      <widget class="QLabel" name="label_3">
       <property name="geometry">
        <rect>
         <x>20</x>
         <y>300</y>
         <width>301</width>
         <height>31</height>
        </rect>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(99, 134, 167); 
font: 81 12pt &quot;Rockwell Extra Bold&quot;;
border-radius: 10px;  </string>
       </property>
       <property name="text">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;translation of this text:&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
      </widget>
      <widget class="QPushButton" name="save_button">
       <property name="geometry">
        <rect>
         <x>310</x>
         <y>500</y>
         <width>251</width>
         <height>61</height>
        </rect>
       </property>
       <property name="sizePolicy">
        <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="cursor">
        <cursorShape>PointingHandCursor</cursorShape>
       </property>
       <property name="toolTip">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;save the translation to the database&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
       <property name="whatsThis">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(99, 134, 167); 
font: 81 12pt &quot;Rockwell Extra Bold&quot;;
border-radius: 30px;  </string>
       </property>
       <property name="text">
        <string>save translate</string>
       </property>
      </widget>
      <widget class="QPushButton" name="clear_button">
       <property name="geometry">
        <rect>
         <x>20</x>
         <y>500</y>
         <width>281</width>
         <height>61</height>
        </rect>
       </property>
       <property name="sizePolicy">
        <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="cursor">
        <cursorShape>PointingHandCursor</cursorShape>
       </property>
       <property name="toolTip">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;the board is cleared for a new transfer&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
       <property name="whatsThis">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(99, 134, 167); 
font: 81 12pt &quot;Rockwell Extra Bold&quot;;
border-radius: 30px;  </string>
       </property>
       <property name="text">
        <string>clear translate board</string>
       </property>
      </widget>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class QdesignSimpletranslate(object):
    def setupUi(self, MainWindow):
        super().__init__()
        desig_2 = io.StringIO(second_design)
        uic.loadUi(desig_2, self)
