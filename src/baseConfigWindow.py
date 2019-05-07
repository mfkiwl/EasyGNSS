#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 17:42:52 2019

@author: edgar
"""

from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QTabWidget, QDialog
from PyQt5 import QtCore
from PyQt5.QtGui import QFont

from outputConfig import OutputConfig
from inputConfig import InputConfig
from outputSerialConfig import OutputSerialConfig
from logConfig import LogConfig
from basePosConfig_Base import BasePosConfig_Base


class BaseConfigWindow:
    '''
    Class BaseConfigWindow is a QDialog subwindow that opens when TabBase.__confi_b is clicked
    It contains all the changeable parameters for the acquisition sorted by type
    
    Attributtes:
        private QDialog window 
        private InputConfig tab_input
        private OutputConfig tab_output
        private OutputSerialConfig tab_output_serial
        private LogConfig tab_log
        private BaseposConfig_Base tab_basepos
    '''
    
    def __init__(self, parent=None):
        
        self.__window = QDialog(parent)
        self.__parent = parent
        self.__window.setFont(QFont('Helvetica',18))

        self.__window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.__window.setGeometry(0, 0, 700, 500)

        
        ######  CONFIGURATION PART  ######
        tabs = QTabWidget()

        self.__tab_input = InputConfig()
        self.__tab_output = OutputConfig()
        self.__tab_output_serial = OutputSerialConfig()
        self.__tab_log = LogConfig()
        self.__tab_basepos = BasePosConfig_Base()
        
        tabs.addTab(self.__tab_input,"Input")
        tabs.addTab(self.__tab_output,"Output")
        tabs.addTab(self.__tab_output_serial,"Solution")
        tabs.addTab(self.__tab_log,"Log")
        tabs.addTab(self.__tab_basepos,"BasePos")
        
        
        ######  BUTTONS  ######

        self.__apply_button= QPushButton('Apply')
#        self.__apply_button.clicked.connect(self.applyParam)
        self.__close_button= QPushButton('Close')
        self.__close_button.clicked.connect(self.__window.close)

        layout = QVBoxLayout()
        layout.addWidget(tabs)

        hbox = QHBoxLayout()
        hbox.addWidget(self.__apply_button,1)
        hbox.addWidget(self.__close_button,1)
        layout.addLayout(hbox)

        self.__window.setLayout(layout)
        
        
    def show(self):
        '''
        Displays BaseConfigWindow on screen 
        '''
        self.__window.exec_()