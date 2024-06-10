# -*- encoding: utf-8 -*- #
"""
Coding by using PyCharm
File: changed图片添加工具/code.py
Be created at 2024/02/25
Be created by HOPE
"""
from UI import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QFileDialog
from PyQt5.QtCore import QUrl, QRegExp
from PyQt5.QtGui import QRegExpValidator
import requests
import sys, os
import webbrowser


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initwindget()

        validator = QRegExpValidator(QRegExp('[^\\\\/:*?"<>|\r\n]+$'))
        self.ui.hint_input.setValidator(validator)
        self.imagePath, self.DFP, self.savePath = "", "", ""

    def initwindget(self):
        self.ui.download_file.clicked.connect(self.Download_and_Add)
        self.ui.fandomLinkButton_2.clicked.connect(self.Link_Fandom)
        self.ui.esixLinkButton.clicked.connect(self.Link_e621)
        self.ui.preview_btn.clicked.connect(self.change_webviewer_url)

    def change_webviewer_url(self):
        try:
            self.ui.ImagewebPreViewer.load(QUrl(self.ui.downloadfilepathEdit.text()))
        except Exception as e:
            self.Dialogue("出问题了!", e, 2)

    @staticmethod
    def Link_Fandom():
        webbrowser.open("https://changed.fandom.com/wiki/Changed_Wiki")

    @staticmethod
    def Link_e621():
        webbrowser.open("https://e621.net/posts?tags=changed_%28video_game%29+rating%3As")

    def Download_and_Add(self):
        savefilename = self.ui.hint_input.text()
        try:
            if self.ui.downloadfilepathEdit.text() == "":
                raise ValueError("未输入下载地址!")
            if self.ui.hint_input.text() == "":
                raise ValueError("未输入“你知道吗”内容!")
            res = requests.get(self.ui.downloadfilepathEdit.text())
        except Exception as e:
            self.Dialogue("出问题了!", f"错误原因: {str(e)}", 2)
        else:
            if not os.path.exists(f"{os.getcwd()}\\PICTURES_CARD"):
                os.mkdir("PICTURES_CARD")
                self.Dialogue("信息", "未检测到PICTURES_CARD文件夹,已创建")
            with open(f'{os.getcwd()}\\PICTURES_CARD\\{savefilename}.png', 'wb') as file:
                file.write(res.content)
            self.Dialogue("喜报", f"{savefilename}下载完成", 0)

            # 添加
            if os.path.exists("hints.txt"):
                with open("hints.txt", "a", encoding="utf-8") as f:
                    f.write(f"\n{self.ui.hint_input.text()}")
            else:
                self.Dialogue("通知", "未检测到hint文件,已创建", 0)
                with open("hints.txt", "w", encoding="utf-8") as f:
                    f.write(f"{self.ui.hint_input.text()}")
            self.Dialogue("喜报", f"{savefilename}添加完成", 0)

    def Dialogue(self, title, text, mode=0):
        """
        mode:{0:  info
              1: warning
              2: Error
              3: question
        """
        if mode == 0:
            QMessageBox.information(self, title, text)
        elif mode == 1:
            QMessageBox.warning(self, title, text)
        elif mode == 2:
            QMessageBox.critical(self, title, text)
        elif mode == 3:
            QMessageBox.question(self, title, text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
