# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(650, 670)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(sizePolicy)
        main_window.setMinimumSize(QtCore.QSize(650, 670))
        main_window.setMaximumSize(QtCore.QSize(650, 1100))
        main_window.setSizeIncrement(QtCore.QSize(0, 300))
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.central_widget)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_top_frame = QtWidgets.QFrame(self.central_widget)
        self.main_top_frame.setMinimumSize(QtCore.QSize(0, 450))
        self.main_top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_top_frame.setObjectName("main_top_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_top_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.path_to_table_big_frame = QtWidgets.QFrame(self.main_top_frame)
        self.path_to_table_big_frame.setMaximumSize(QtCore.QSize(16777215, 140))
        self.path_to_table_big_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.path_to_table_big_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.path_to_table_big_frame.setObjectName("path_to_table_big_frame")
        self.path_to_table_frame = QtWidgets.QFrame(self.path_to_table_big_frame)
        self.path_to_table_frame.setGeometry(QtCore.QRect(9, 30, 594, 91))
        self.path_to_table_frame.setStyleSheet("QFrame#path_to_table_frame {\n"
"    border-color: rgb(194, 233, 233);\n"
"    border-width: 1px;\n"
"    border-style: double;\n"
"\n"
"}")
        self.path_to_table_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.path_to_table_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.path_to_table_frame.setObjectName("path_to_table_frame")
        self.path_to_table_button = QtWidgets.QPushButton(self.path_to_table_frame)
        self.path_to_table_button.setGeometry(QtCore.QRect(10, 30, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.path_to_table_button.setFont(font)
        self.path_to_table_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(38, 153, 153);\n"
"    color: rgb(240,240,240);\n"
"    border-style: none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(30, 134, 134);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(22, 114, 114);\n"
"}")
        self.path_to_table_button.setObjectName("path_to_table_button")
        self.path_to_table_input = QtWidgets.QLineEdit(self.path_to_table_frame)
        self.path_to_table_input.setGeometry(QtCore.QRect(150, 30, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.path_to_table_input.setFont(font)
        self.path_to_table_input.setStyleSheet("QLineEdit{\n"
"    border-color: rgb(153, 153, 153);\n"
"}\n"
"QLineEdit:hover{\n"
"    border-color: rgb(117, 117, 117);\n"
"}\n"
"QLineEdit:focus{\n"
"    border-color: rgb(61, 207, 207);\n"
"}\n"
"")
        self.path_to_table_input.setText("")
        self.path_to_table_input.setReadOnly(True)
        self.path_to_table_input.setClearButtonEnabled(False)
        self.path_to_table_input.setObjectName("path_to_table_input")
        self.covid_frame = QtWidgets.QFrame(self.path_to_table_frame)
        self.covid_frame.setEnabled(False)
        self.covid_frame.setGeometry(QtCore.QRect(450, 10, 141, 71))
        self.covid_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.covid_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.covid_frame.setObjectName("covid_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.covid_frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.covid_descript = QtWidgets.QLabel(self.covid_frame)
        self.covid_descript.setEnabled(False)
        self.covid_descript.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.covid_descript.setFont(font)
        self.covid_descript.setStyleSheet("Qlabel {\n"
"    background-color: rgba(255,255,255,0);\n"
"    border-color: rgba(255,255,255,0);\n"
"}")
        self.covid_descript.setObjectName("covid_descript")
        self.verticalLayout_4.addWidget(self.covid_descript)
        self.path_to_table_ok = QtWidgets.QRadioButton(self.covid_frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.path_to_table_ok.setFont(font)
        self.path_to_table_ok.setStyleSheet("QRadioButton{\n"
"    color:rgb(0, 135, 0)\n"
"}\n"
"QRadioButton:disabled{\n"
"    color:rgb(150,150,150)\n"
"}")
        self.path_to_table_ok.setObjectName("path_to_table_ok")
        self.verticalLayout_4.addWidget(self.path_to_table_ok)
        self.path_to_table_ill = QtWidgets.QRadioButton(self.covid_frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.path_to_table_ill.setFont(font)
        self.path_to_table_ill.setStyleSheet("QRadioButton{\n"
"    color: rgb(135, 0, 0)\n"
"}\n"
"QRadioButton:disabled{\n"
"    color:rgb(150,150,150)\n"
"}")
        self.path_to_table_ill.setObjectName("path_to_table_ill")
        self.verticalLayout_4.addWidget(self.path_to_table_ill)
        self.path_to_table_deco = QtWidgets.QFrame(self.path_to_table_big_frame)
        self.path_to_table_deco.setGeometry(QtCore.QRect(20, 20, 116, 21))
        self.path_to_table_deco.setStyleSheet("QFrame#path_to_table_deco {\n"
"    background-color: rgb(240, 240, 240)\n"
"    \n"
"}")
        self.path_to_table_deco.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.path_to_table_deco.setFrameShadow(QtWidgets.QFrame.Raised)
        self.path_to_table_deco.setObjectName("path_to_table_deco")
        self.path_to_table_descript = QtWidgets.QLabel(self.path_to_table_deco)
        self.path_to_table_descript.setGeometry(QtCore.QRect(0, 0, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.path_to_table_descript.setFont(font)
        self.path_to_table_descript.setStyleSheet("Qlabel {\n"
"    background-color: rgba(255,255,255,0);\n"
"    border-color: rgba(255,255,255,0);\n"
"}")
        self.path_to_table_descript.setObjectName("path_to_table_descript")
        self.toolButton = QtWidgets.QToolButton(self.path_to_table_big_frame)
        self.toolButton.setGeometry(QtCore.QRect(500, 0, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.toolButton.setFont(font)
        self.toolButton.setStyleSheet("QToolButton {\n"
"    background-color: rgb(38, 153, 153);\n"
"    color: rgb(240,240,240);\n"
"    border-style: none;\n"
"}\n"
"QToolButton:hover{\n"
"    background-color: rgb(30, 134, 134);\n"
"}\n"
"QToolButton:pressed{\n"
"    background-color: rgb(22, 114, 114);\n"
"}")
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.path_to_table_big_frame)
        self.toolButton_2.setGeometry(QtCore.QRect(200, 0, 200, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.toolButton_2.setFont(font)
        self.toolButton_2.setStyleSheet("QToolButton {\n"
"    background-color: rgb(200, 75, 75);\n"
"    color: rgb(240,240,240);\n"
"    border-style: none;\n"
"}\n"
"QToolButton:hover{\n"
"    background-color: rgb(180, 65, 65);\n"
"}\n"
"QToolButton:pressed{\n"
"    background-color: rgb(160, 55, 55);\n"
"}")
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.toolButton_2.setObjectName("toolButton_2")
        self.verticalLayout_2.addWidget(self.path_to_table_big_frame)
        self.frame = QtWidgets.QFrame(self.main_top_frame)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(18, 0, 19, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.start_parsing_button = QtWidgets.QPushButton(self.frame)
        self.start_parsing_button.setEnabled(False)
        self.start_parsing_button.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.start_parsing_button.setFont(font)
        self.start_parsing_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(38, 153, 153);\n"
"    color: rgb(240,240,240);\n"
"    border-style: none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(30, 134, 134);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(22, 114, 114);\n"
"}\n"
"QPushButton:disabled{\n"
"    background-color: rgb(180,180,180);\n"
"}")
        self.start_parsing_button.setObjectName("start_parsing_button")
        self.verticalLayout_3.addWidget(self.start_parsing_button)
        self.verticalLayout_2.addWidget(self.frame)
        self.login_big_frame = QtWidgets.QFrame(self.main_top_frame)
        self.login_big_frame.setEnabled(False)
        self.login_big_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_big_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_big_frame.setObjectName("login_big_frame")
        self.login_frame = QtWidgets.QFrame(self.login_big_frame)
        self.login_frame.setGeometry(QtCore.QRect(9, 20, 594, 191))
        self.login_frame.setStyleSheet("QFrame#login_frame {\n"
"    border-color: rgb(194, 233, 233);\n"
"    border-width: 1px;\n"
"    border-style: double;\n"
"\n"
"}")
        self.login_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_frame.setObjectName("login_frame")
        self.username_descript = QtWidgets.QLabel(self.login_frame)
        self.username_descript.setGeometry(QtCore.QRect(10, 30, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.username_descript.setFont(font)
        self.username_descript.setStyleSheet("Qlabel {\n"
"    background-color: rgba(255,255,255,0);\n"
"    border-color: rgba(255,255,255,0);\n"
"}")
        self.username_descript.setObjectName("username_descript")
        self.password_descript = QtWidgets.QLabel(self.login_frame)
        self.password_descript.setGeometry(QtCore.QRect(308, 30, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.password_descript.setFont(font)
        self.password_descript.setStyleSheet("Qlabel {\n"
"    background-color: rgba(255,255,255,0);\n"
"    border-color: rgba(255,255,255,0);\n"
"}")
        self.password_descript.setObjectName("password_descript")
        self.start_main_algorithm = QtWidgets.QPushButton(self.login_frame)
        self.start_main_algorithm.setEnabled(False)
        self.start_main_algorithm.setGeometry(QtCore.QRect(9, 130, 575, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.start_main_algorithm.setFont(font)
        self.start_main_algorithm.setStyleSheet("QPushButton {\n"
"    background-color: rgb(38, 153, 153);\n"
"    color: rgb(240,240,240);\n"
"    border-style: none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(30, 134, 134);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(22, 114, 114);\n"
"}\n"
"QPushButton:disabled{\n"
"    background-color: rgb(180,180,180);\n"
"}")
        self.start_main_algorithm.setObjectName("start_main_algorithm")
        self.splitter = QtWidgets.QSplitter(self.login_frame)
        self.splitter.setGeometry(QtCore.QRect(9, 55, 575, 31))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(20)
        self.splitter.setObjectName("splitter")
        self.username_input = QtWidgets.QLineEdit(self.splitter)
        self.username_input.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.username_input.setFont(font)
        self.username_input.setStyleSheet("QLineEdit{\n"
"    border-color: rgb(153, 153, 153);\n"
"}\n"
"QLineEdit:hover{\n"
"    border-color: rgb(117, 117, 117);\n"
"}\n"
"QLineEdit:focus{\n"
"    border-color: rgb(61, 207, 207);\n"
"}\n"
"")
        self.username_input.setText("")
        self.username_input.setReadOnly(False)
        self.username_input.setClearButtonEnabled(False)
        self.username_input.setObjectName("username_input")
        self.password_input = QtWidgets.QLineEdit(self.splitter)
        self.password_input.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.password_input.setFont(font)
        self.password_input.setStyleSheet("QLineEdit{\n"
"    border-color: rgb(153, 153, 153);\n"
"}\n"
"QLineEdit:hover{\n"
"    border-color: rgb(117, 117, 117);\n"
"}\n"
"QLineEdit:focus{\n"
"    border-color: rgb(61, 207, 207);\n"
"}\n"
"")
        self.password_input.setText("")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setReadOnly(False)
        self.password_input.setClearButtonEnabled(False)
        self.password_input.setObjectName("password_input")
        self.login_frame_deco = QtWidgets.QFrame(self.login_big_frame)
        self.login_frame_deco.setGeometry(QtCore.QRect(20, 10, 104, 21))
        self.login_frame_deco.setStyleSheet("QFrame#login_frame_deco {\n"
"    background-color: rgb(240, 240, 240)\n"
"    \n"
"}")
        self.login_frame_deco.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_frame_deco.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_frame_deco.setObjectName("login_frame_deco")
        self.login_frame_descript = QtWidgets.QLabel(self.login_frame_deco)
        self.login_frame_descript.setGeometry(QtCore.QRect(0, 0, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.login_frame_descript.setFont(font)
        self.login_frame_descript.setStyleSheet("Qlabel {\n"
"    background-color: rgba(255,255,255,0);\n"
"    border-color: rgba(255,255,255,0);\n"
"}")
        self.login_frame_descript.setObjectName("login_frame_descript")
        self.verticalLayout_2.addWidget(self.login_big_frame)
        self.table_parse_error_descript = QtWidgets.QLabel(self.main_top_frame)
        self.table_parse_error_descript.setEnabled(True)
        self.table_parse_error_descript.setMaximumSize(QtCore.QSize(16777215, 18))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.table_parse_error_descript.setFont(font)
        self.table_parse_error_descript.setText("")
        self.table_parse_error_descript.setAlignment(QtCore.Qt.AlignCenter)
        self.table_parse_error_descript.setObjectName("table_parse_error_descript")
        self.verticalLayout_2.addWidget(self.table_parse_error_descript)
        self.verticalLayout.addWidget(self.main_top_frame)
        self.table_widget = QtWidgets.QTableWidget(self.central_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.table_widget.setFont(font)
        self.table_widget.setAutoScrollMargin(8)
        self.table_widget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_widget.setProperty("showDropIndicator", False)
        self.table_widget.setDragDropOverwriteMode(False)
        self.table_widget.setAlternatingRowColors(False)
        self.table_widget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.table_widget.setObjectName("table_widget")
        self.table_widget.setColumnCount(2)
        self.table_widget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(1, item)
        self.table_widget.horizontalHeader().setVisible(True)
        self.table_widget.horizontalHeader().setCascadingSectionResizes(False)
        self.table_widget.horizontalHeader().setDefaultSectionSize(150)
        self.table_widget.horizontalHeader().setSortIndicatorShown(False)
        self.table_widget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.table_widget)
        self.wtrm = QtWidgets.QLabel(self.central_widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.wtrm.setFont(font)
        self.wtrm.setStyleSheet("QLabel{\n"
"    color:rgb(100,100,100)\n"
"}")
        self.wtrm.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.wtrm.setIndent(3)
        self.wtrm.setObjectName("wtrm")
        self.verticalLayout.addWidget(self.wtrm)
        main_window.setCentralWidget(self.central_widget)
        self.statusBar = QtWidgets.QStatusBar(main_window)
        self.statusBar.setObjectName("statusBar")
        main_window.setStatusBar(self.statusBar)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "???????????? ?????????????????????? ???????????? ???? COVID-19 ?? ??????????"))
        self.path_to_table_button.setText(_translate("main_window", "?????????????? ????????..."))
        self.path_to_table_input.setPlaceholderText(_translate("main_window", "  ???????????????? ????????, ?????????? ???? ???????????? ??????????"))
        self.covid_descript.setText(_translate("main_window", "COVID-????????????"))
        self.path_to_table_ok.setText(_translate("main_window", "??????????????????????????"))
        self.path_to_table_ill.setText(_translate("main_window", "??????????????????????????"))
        self.path_to_table_descript.setText(_translate("main_window", "???????? ???? ??????????????"))
        self.toolButton.setText(_translate("main_window", "??????????????????"))
        self.toolButton_2.setText(_translate("main_window", "???????????????? ???? ???????????? ?? ??????????????????"))
        self.start_parsing_button.setText(_translate("main_window", "???????????????????? ???????????? ???? ??????????????"))
        self.username_descript.setText(_translate("main_window", "?????? ????????????????????????"))
        self.password_descript.setText(_translate("main_window", "????????????"))
        self.start_main_algorithm.setText(_translate("main_window", "?????????????????? ???????????? ???? ?????????????? ?? ??????????????"))
        self.username_input.setPlaceholderText(_translate("main_window", "  ?????????????? ?????? ????????????????????????"))
        self.password_input.setPlaceholderText(_translate("main_window", "  ?????????????? ????????????"))
        self.login_frame_descript.setText(_translate("main_window", "???????? ?? ??????????????"))
        item = self.table_widget.horizontalHeaderItem(0)
        item.setText(_translate("main_window", "????????????????????????"))
        item = self.table_widget.horizontalHeaderItem(1)
        item.setText(_translate("main_window", "?????????????????????? ????????????"))
        self.wtrm.setText(_translate("main_window", "Figurin Ivan, 2020"))
