import io

from PyQt5 import uic

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

class QdesignButtonsValue(object):
    def setupUi(self, MainWindow):
        super().__init__()
        desig_5 = io.StringIO(design_buttonsValue)
        uic.loadUi(desig_5, self)
