# coding: utf-8

import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QFileDialog, \
    QLabel
import io
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
import sqlite3
from PyQt5 import uic
from googletrans import Translator

SCREEN_SIZE = [405, 400]

# Дизайн первого окна
design = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>WelcomeWindow</class>
 <widget class="QMainWindow" name="WelcomeWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>780</width>
    <height>495</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>WelcomeWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(27, 27, 27);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QWidget" name="widget" native="true">
      <property name="styleSheet">
       <string notr="true"/>
      </property>
      <widget class="QWidget" name="verticalLayoutWidget">
       <property name="geometry">
        <rect>
         <x>190</x>
         <y>40</y>
         <width>371</width>
         <height>351</height>
        </rect>
       </property>
       <layout class="QVBoxLayout" name="verticalLayout_2">
        <item>
         <widget class="QLabel" name="label">
          <property name="toolTip">
           <string/>
          </property>
          <property name="styleSheet">
           <string notr="true">font: 23pt &quot;Pristina&quot;;
color: rgb(0, 0, 0);
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(99, 134, 167), stop:1 rgba(200, 233, 222, 215));
border-radius: 14px;  </string>
          </property>
          <property name="text">
           <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;TRRTranslator&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="newtranslation_button">
          <property name="enabled">
           <bool>true</bool>
          </property>
          <property name="sizePolicy">
           <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
            <horstretch>0</horstretch>
            <verstretch>0</verstretch>
           </sizepolicy>
          </property>
          <property name="maximumSize">
           <size>
            <width>16777215</width>
            <height>100</height>
           </size>
          </property>
          <property name="cursor">
           <cursorShape>PointingHandCursor</cursorShape>
          </property>
          <property name="styleSheet">
           <string notr="true">background-color: rgb(99, 134, 167); 
font: 81 14pt &quot;Rockwell Extra Bold&quot;;
border-radius: 30px;  </string>
          </property>
          <property name="text">
           <string>New translation</string>
          </property>
          <property name="checkable">
           <bool>false</bool>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="translationhistory_button">
          <property name="enabled">
           <bool>true</bool>
          </property>
          <property name="sizePolicy">
           <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
            <horstretch>0</horstretch>
            <verstretch>0</verstretch>
           </sizepolicy>
          </property>
          <property name="maximumSize">
           <size>
            <width>16777215</width>
            <height>100</height>
           </size>
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
           <string>Translation history</string>
          </property>
          <property name="checkable">
           <bool>false</bool>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="translatetxtfile_button">
          <property name="enabled">
           <bool>true</bool>
          </property>
          <property name="sizePolicy">
           <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
            <horstretch>0</horstretch>
            <verstretch>0</verstretch>
           </sizepolicy>
          </property>
          <property name="maximumSize">
           <size>
            <width>16777215</width>
            <height>100</height>
           </size>
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
           <string>Translation of a text file (.txt)</string>
          </property>
          <property name="checkable">
           <bool>false</bool>
          </property>
         </widget>
        </item>
       </layout>
      </widget>
      <widget class="QLabel" name="label_2">
       <property name="geometry">
        <rect>
         <x>460</x>
         <y>420</y>
         <width>301</width>
         <height>20</height>
        </rect>
       </property>
       <property name="styleSheet">
        <string notr="true">color: rgb(253, 253, 253);
font: 7pt &quot;Palatino Linotype&quot;;</string>
       </property>
       <property name="text">
        <string>Назначение клавиш можно посмотреть в &quot;помощи&quot;</string>
       </property>
      </widget>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>780</width>
     <height>26</height>
    </rect>
   </property>
   <widget class="QMenu" name="menu">
    <property name="title">
     <string>Помощь</string>
    </property>
    <addaction name="action"/>
   </widget>
   <addaction name="menu"/>
  </widget>
  <action name="action">
   <property name="text">
    <string>назначение кнопок</string>
   </property>
  </action>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

# Дизайн второго окна
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

# Дизайн окна "Помощи"
design_buttonsValue = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>buttons</class>
 <widget class="QWidget" name="buttons">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1059</width>
    <height>394</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>ButtonsValue</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(24, 26, 65);</string>
  </property>
  <layout class="QHBoxLayout" name="horizontalLayout">
   <item>
    <widget class="QWidget" name="widget" native="true">
     <widget class="QWidget" name="verticalLayoutWidget">
      <property name="geometry">
       <rect>
        <x>10</x>
        <y>20</y>
        <width>381</width>
        <height>341</height>
       </rect>
      </property>
      <layout class="QVBoxLayout" name="verticalLayout_2">
       <item>
        <widget class="QPushButton" name="newtranslation_button">
         <property name="enabled">
          <bool>true</bool>
         </property>
         <property name="sizePolicy">
          <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="maximumSize">
          <size>
           <width>16777215</width>
           <height>100</height>
          </size>
         </property>
         <property name="cursor">
          <cursorShape>PointingHandCursor</cursorShape>
         </property>
         <property name="styleSheet">
          <string notr="true">background-color: rgb(99, 134, 167); 
font: 81 14pt &quot;Rockwell Extra Bold&quot;;
border-radius: 30px;  </string>
         </property>
         <property name="text">
          <string>New translation</string>
         </property>
         <property name="checkable">
          <bool>false</bool>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="translationhistory_button">
         <property name="enabled">
          <bool>true</bool>
         </property>
         <property name="sizePolicy">
          <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="maximumSize">
          <size>
           <width>16777215</width>
           <height>100</height>
          </size>
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
          <string>Translation history</string>
         </property>
         <property name="checkable">
          <bool>false</bool>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="translatetxtfile_button">
         <property name="enabled">
          <bool>true</bool>
         </property>
         <property name="sizePolicy">
          <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="maximumSize">
          <size>
           <width>16777215</width>
           <height>100</height>
          </size>
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
          <string>Translation of a text file (.txt)</string>
         </property>
         <property name="checkable">
          <bool>false</bool>
         </property>
        </widget>
       </item>
      </layout>
     </widget>
     <widget class="QLabel" name="label_2">
      <property name="geometry">
       <rect>
        <x>390</x>
        <y>50</y>
        <width>51</width>
        <height>41</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true">color: rgb(255, 255, 255);</string>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:12pt;&quot;&gt;-&amp;gt;&amp;gt;&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLabel" name="label_7">
      <property name="geometry">
       <rect>
        <x>390</x>
        <y>280</y>
        <width>51</width>
        <height>41</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true">color: rgb(255, 255, 255);</string>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:12pt;&quot;&gt;-&amp;gt;&amp;gt;&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLabel" name="label_8">
      <property name="geometry">
       <rect>
        <x>390</x>
        <y>160</y>
        <width>51</width>
        <height>41</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true">color: rgb(255, 255, 255);</string>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:12pt;&quot;&gt;-&amp;gt;&amp;gt;&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QWidget" name="verticalLayoutWidget_3">
      <property name="geometry">
       <rect>
        <x>460</x>
        <y>20</y>
        <width>561</width>
        <height>341</height>
       </rect>
      </property>
      <layout class="QVBoxLayout" name="verticalLayout">
       <item>
        <widget class="QLabel" name="label">
         <property name="styleSheet">
          <string notr="true">background-color: rgb(42, 45, 113);
font: 81 14pt &quot;Rockwell Extra Bold&quot;;
border-radius: 50px;  </string>
         </property>
         <property name="text">
          <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;Button to switch to a regular translator&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLabel" name="label_5">
         <property name="styleSheet">
          <string notr="true">background-color: rgb(42, 45, 113);
font: 81 14pt &quot;Rockwell Extra Bold&quot;;
border-radius: 50px;  </string>
         </property>
         <property name="text">
          <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;Go to your translation history&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLabel" name="label_6">
         <property name="styleSheet">
          <string notr="true">background-color: rgb(42, 45, 113);
font: 81 14pt &quot;Rockwell Extra Bold&quot;;
border-radius: 50px;  </string>
         </property>
         <property name="text">
          <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;Switching to the text&lt;/p&gt;&lt;p align=&quot;center&quot;&gt; file translation environment&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
         </property>
        </widget>
       </item>
      </layout>
     </widget>
    </widget>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

# Дизайн окна Истории переводов
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
    <item row="2" column="1">
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
    <item row="3" column="0">
     <widget class="QTableWidget" name="SQLHistory">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(0, 0, 57);</string>
      </property>
     </widget>
    </item>
    <item row="3" column="1">
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

design_txtfiles = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>603</width>
    <height>720</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(0, 0, 0);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QHBoxLayout" name="horizontalLayout">
    <item>
     <widget class="QWidget" name="widget" native="true">
      <widget class="QComboBox" name="language">
       <property name="geometry">
        <rect>
         <x>360</x>
         <y>400</y>
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
         <x>50</x>
         <y>320</y>
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
      <widget class="QTextEdit" name="text_of_your_file">
       <property name="geometry">
        <rect>
         <x>20</x>
         <y>150</y>
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
      <widget class="QTextEdit" name="text_of_new_file">
       <property name="geometry">
        <rect>
         <x>20</x>
         <y>440</y>
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
         <y>110</y>
         <width>251</width>
         <height>31</height>
        </rect>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(99, 134, 167); 
font: 81 12pt &quot;Rockwell Extra Bold&quot;;
border-radius: 10px;  </string>
       </property>
       <property name="text">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;text from your file:&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
      </widget>
      <widget class="QLabel" name="label_3">
       <property name="geometry">
        <rect>
         <x>20</x>
         <y>400</y>
         <width>331</width>
         <height>31</height>
        </rect>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(99, 134, 167); 
font: 81 12pt &quot;Rockwell Extra Bold&quot;;
border-radius: 10px;  </string>
       </property>
       <property name="text">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;translation of this text file:&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
      </widget>
      <widget class="QPushButton" name="clear_button">
       <property name="geometry">
        <rect>
         <x>20</x>
         <y>600</y>
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
      <widget class="QPushButton" name="name_file_button">
       <property name="geometry">
        <rect>
         <x>20</x>
         <y>30</y>
         <width>541</width>
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
        <string notr="true">background-color: rgb(64, 87, 108);
font: 81 12pt &quot;Rockwell Extra Bold&quot;;
border-radius: 10px;  </string>
       </property>
       <property name="text">
        <string>paste your file here</string>
       </property>
      </widget>
      <widget class="QPushButton" name="save_button">
       <property name="geometry">
        <rect>
         <x>310</x>
         <y>600</y>
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


# Класс отвечающий за окно истории переводов (вторая кнопка)
class SQLWigetHistory(QMainWindow):
    def __init__(self):
        super().__init__()
        desig_SQL = io.StringIO(design_SQL)
        uic.loadUi(desig_SQL, self)
        self.box = TRRBBox()
        self.mood_button.clicked.connect(self.moodfunction)

    ''' self.con = sqlite3.connect('translation_history_db.db')
     cur = self.con.cursor()
     self.allHistory = cur.execute()
     self.SQLHistory.setRowCount(len(str(self.allHistory)))
     self.con.close()'''

    def moodfunction(self):
        self.box.show()


# Класс отвечающий за окно "Помощи"
class ButtonsValue(QMainWindow):
    def __init__(self):
        super().__init__()
        desig_buttonsValue = io.StringIO(design_buttonsValue)
        uic.loadUi(desig_buttonsValue, self)


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
class Txtfiles_translate(QMainWindow):
    def __init__(self):
        super().__init__()
        desig_txt = io.StringIO(design_txtfiles)
        uic.loadUi(desig_txt, self)
        self.setWindowTitle('TXTfilesTranslate')
        self.fname = None
        self.language.model().sort(0)
        self.status = self.statusBar()
        self.status.setStyleSheet(
            "QStatusBar{padding-left:8px;color:white;font-weight:bold;}")
        self.name_file_button.clicked.connect(self.txttranslate)
        self.translatebutton.clicked.connect(self.translate_file_button)
        self.clear_button.clicked.connect(self.clear_func)

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
            if self.language.currentText() == 'Английский':
                self.text_of_new_file.setText(self.translate_text(text, 'en'))
            elif self.language.currentText() == 'Арабский':
                self.text_of_new_file.setText(self.translate_text(text, 'ar'))
            elif self.language.currentText() == 'Греческий':
                self.text_of_new_file.setText(self.translate_text(text, 'el'))
            elif self.language.currentText() == 'Испанский':
                self.text_of_new_file.setText(self.translate_text(text, 'es'))
            elif self.language.currentText() == 'Итальянский':
                self.text_of_new_file.setText(self.translate_text(text, 'it'))
            elif self.language.currentText() == 'Китайский':
                self.text_of_new_file.setText(
                    self.translate_text(text, 'zh-TW'))
            elif self.language.currentText() == 'Корейский':
                self.text_of_new_file.setText(self.translate_text(text, 'ko'))
            elif self.language.currentText() == 'Немецкий':
                self.text_of_new_file.setText(self.translate_text(text, 'de'))
            elif self.language.currentText() == 'Польский':
                self.text_of_new_file.setText(self.translate_text(text, 'pl'))
            elif self.language.currentText() == 'Португальский':
                self.text_of_new_file.setText(self.translate_text(text, 'pt'))
            elif self.language.currentText() == 'Румынский':
                self.text_of_new_file.setText(self.translate_text(text, 'ro'))
            elif self.language.currentText() == 'Русский':
                self.text_of_new_file.setText(self.translate_text(text, 'ru'))
            elif self.language.currentText() == 'Турецкий':
                self.text_of_new_file.setText(self.translate_text(text, 'tr'))
            elif self.language.currentText() == 'Украинский':
                self.text_of_new_file.setText(self.translate_text(text, 'uk'))
            elif self.language.currentText() == 'Французкий':
                self.text_of_new_file.setText(self.translate_text(text, 'fr'))
            elif self.language.currentText() == 'Японский':
                self.text_of_new_file.setText(self.translate_text(text, 'ja'))
        else:
            self.status.showMessage('Выберите файл.')


# Класс отвечающий за начальное окно
class TranslatorWelcomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        desig = io.StringIO(design)
        uic.loadUi(desig, self)
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


'''    def transition_history_window(self):
'''


# Класс отвечающий за окно обычного переводчика (вторая кнопка)
class Translator_second(QMainWindow):
    def __init__(self):
        super().__init__()
        desig_second = io.StringIO(second_design)
        uic.loadUi(desig_second, self)
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
            if self.language.currentText() == 'Английский':
                id_language = cur.execute(f'''SELECT id FROM languages WHERE name = "Английский"''').fetchall()
                cur.execute(f'''
                INSERT INTO history(original_text, translated_text, language)
                VALUES({self.textEdit.toPlainText()}, {self.textEdit_2.toPlainText()}, {id_language[0][0]})''').fetchall()
                db.commit()

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
            if self.language.currentText() == 'Английский':
                self.textEdit_2.setText(self.translate_text(question, 'en'))
            elif self.language.currentText() == 'Арабский':
                self.textEdit_2.setText(self.translate_text(question, 'ar'))
            elif self.language.currentText() == 'Греческий':
                self.textEdit_2.setText(self.translate_text(question, 'el'))
            elif self.language.currentText() == 'Испанский':
                self.textEdit_2.setText(self.translate_text(question, 'es'))
            elif self.language.currentText() == 'Итальянский':
                self.textEdit_2.setText(self.translate_text(question, 'it'))
            elif self.language.currentText() == 'Китайский':
                self.textEdit_2.setText(self.translate_text(question, 'zh-TW'))
            elif self.language.currentText() == 'Корейский':
                self.textEdit_2.setText(self.translate_text(question, 'ko'))
            elif self.language.currentText() == 'Немецкий':
                self.textEdit_2.setText(self.translate_text(question, 'de'))
            elif self.language.currentText() == 'Польский':
                self.textEdit_2.setText(self.translate_text(question, 'pl'))
            elif self.language.currentText() == 'Португальский':
                self.textEdit_2.setText(self.translate_text(question, 'pt'))
            elif self.language.currentText() == 'Румынский':
                self.textEdit_2.setText(self.translate_text(question, 'ro'))
            elif self.language.currentText() == 'Русский':
                self.textEdit_2.setText(self.translate_text(question, 'ru'))
            elif self.language.currentText() == 'Турецкий':
                self.textEdit_2.setText(self.translate_text(question, 'tr'))
            elif self.language.currentText() == 'Украинский':
                self.textEdit_2.setText(self.translate_text(question, 'uk'))
            elif self.language.currentText() == 'Французкий':
                self.textEdit_2.setText(self.translate_text(question, 'fr'))
            elif self.language.currentText() == 'Японский':
                self.textEdit_2.setText(self.translate_text(question, 'ja'))
        else:
            self.status.showMessage('Введите текст.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TranslatorWelcomeWindow()
    ex.show()
    sys.exit(app.exec_())
