import io

from PyQt5 import uic

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


class QdesignWelcomeWindow(object):
    def setupUi(self, MainWindow):
        super().__init__()
        desig = io.StringIO(design)
        uic.loadUi(desig, self)
