import io

from PyQt5 import uic

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


class QdesignTxtTranslate(object):
    def setupUi(self, MainWindow):
        super().__init__()
        desig_4 = io.StringIO(design_txtfiles)
        uic.loadUi(desig_4, self)
