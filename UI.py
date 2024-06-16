# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(471, 698)
        Form.setMinimumSize(QtCore.QSize(469, 468))
        Form.setMaximumSize(QtCore.QSize(471, 121212))
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 451, 101))
        self.groupBox.setMaximumSize(QtCore.QSize(121234, 16777215))
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.esixLinkButton = QtWidgets.QCommandLinkButton(self.groupBox)
        self.esixLinkButton.setGeometry(QtCore.QRect(0, 60, 451, 41))
        self.esixLinkButton.setDescription("")
        self.esixLinkButton.setObjectName("esixLinkButton")
        self.fandomLinkButton_2 = QtWidgets.QCommandLinkButton(self.groupBox)
        self.fandomLinkButton_2.setGeometry(QtCore.QRect(0, 20, 451, 41))
        self.fandomLinkButton_2.setDescription("")
        self.fandomLinkButton_2.setObjectName("fandomLinkButton_2")
        self.add_file = QtWidgets.QPushButton(Form)
        self.add_file.setGeometry(QtCore.QRect(30, 640, 399, 31))
        self.add_file.setObjectName("add_file")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 440, 401, 191))
        self.groupBox_3.setObjectName("groupBox_3")
        self.ImagewebPreViewer = QtWebEngineWidgets.QWebEngineView(self.groupBox_3)
        self.ImagewebPreViewer.setGeometry(QtCore.QRect(40, 20, 321, 161))
        self.ImagewebPreViewer.setProperty("url", QtCore.QUrl("about:blank"))
        self.ImagewebPreViewer.setObjectName("ImagewebPreViewer")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 100, 451, 231))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 670, 401, 31))
        self.label_5.setStyleSheet("color: rgb(122, 122, 122);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 330, 451, 109))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mode_changer_combobox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.mode_changer_combobox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mode_changer_combobox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.mode_changer_combobox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.mode_changer_combobox.setObjectName("mode_changer_combobox")
        self.mode_changer_combobox.addItem("")
        self.mode_changer_combobox.addItem("")
        self.verticalLayout.addWidget(self.mode_changer_combobox, 0, QtCore.Qt.AlignVCenter)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.downloadfilepathEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.downloadfilepathEdit.setObjectName("downloadfilepathEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.downloadfilepathEdit)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.hint_input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hint_input.setObjectName("hint_input")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.hint_input)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.preview_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.preview_btn.setObjectName("preview_btn")
        self.horizontalLayout.addWidget(self.preview_btn)
        self.choose_img_file_path_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.choose_img_file_path_btn.setEnabled(False)
        self.choose_img_file_path_btn.setCheckable(False)
        self.choose_img_file_path_btn.setChecked(False)
        self.choose_img_file_path_btn.setAutoRepeat(False)
        self.choose_img_file_path_btn.setAutoExclusive(False)
        self.choose_img_file_path_btn.setObjectName("choose_img_file_path_btn")
        self.horizontalLayout.addWidget(self.choose_img_file_path_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        self.mode_changer_combobox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Changed图片添加器"))
        self.groupBox.setTitle(_translate("Form", "图片常见网站"))
        self.esixLinkButton.setText(_translate("Form", "Changed e621 Tag"))
        self.fandomLinkButton_2.setText(_translate("Form", "Changed Fandom Wiki"))
        self.add_file.setText(_translate("Form", "下载并添加"))
        self.groupBox_3.setTitle(_translate("Form", "图片预览"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft YaHei UI\'; font-weight:696;\">添加自定义图片到随机图片库(本地)</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft YaHei UI\';\">具体的实现原理为：</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft YaHei UI\';\">· 将图片文件命名为&quot;你知道吗&quot;的内容之一 </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft YaHei UI\';\">· 在显示图片时使用{hint}替代图片路径</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft YaHei UI\';\">所以可以通过添加&quot;你知道吗&quot;的条目来将图片添加到播放列表</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft YaHei UI\'; color:#7a7a7a;\">注：因为文件名不能包含特殊字符(\\ / : ? &quot; &lt; &gt; | )</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft YaHei UI\'; color:#7a7a7a;\">所以&quot;你知道吗&quot;的内容也不能包含这些字符</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "Designed by HOPE"))
        self.mode_changer_combobox.setItemText(0, _translate("Form", "从互联网下载文件导入"))
        self.mode_changer_combobox.setItemText(1, _translate("Form", "从本地选择文件导入"))
        self.label_3.setText(_translate("Form", "下载地址"))
        self.downloadfilepathEdit.setPlaceholderText(_translate("Form", "链接必须为以http://或https://开头的网址,部分网址可能无法下载"))
        self.label.setText(_translate("Form", "\"你知道吗\""))
        self.hint_input.setPlaceholderText(_translate("Form", "输入\"你知道吗\"的内容"))
        self.preview_btn.setText(_translate("Form", "预览"))
        self.choose_img_file_path_btn.setText(_translate("Form", "选择图片文件"))
from PyQt5 import QtWebEngineWidgets
