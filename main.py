import csv
import sqlite3
import sys
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
	QApplication,
	QMainWindow,
	QStackedWidget,
	QStatusBar,
	QFileDialog,
	QDialog,
	QVBoxLayout,
	QLabel,
)


class Ui_Notes(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(800, 600)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
		self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 51))
		self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.profile_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		self.profile_button.setText("")
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("img/free-icon-font-user-3917688.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.profile_button.setIcon(icon)
		self.profile_button.setIconSize(QtCore.QSize(40, 40))
		self.profile_button.setObjectName("profile_button")
		self.horizontalLayout.addWidget(self.profile_button)
		self.notes_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		self.notes_button.setText("")
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap("img/free-icon-font-edit-3917361.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.notes_button.setIcon(icon1)
		self.notes_button.setIconSize(QtCore.QSize(40, 40))
		self.notes_button.setObjectName("notes_button")
		self.horizontalLayout.addWidget(self.notes_button)
		self.info_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		self.info_button.setText("")
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap("img/free-icon-font-info-3916699.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.info_button.setIcon(icon2)
		self.info_button.setIconSize(QtCore.QSize(40, 40))
		self.info_button.setObjectName("info_button")
		self.horizontalLayout.addWidget(self.info_button)
		self.noteEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
		self.noteEdit.setGeometry(QtCore.QRect(0, 400, 391, 91))
		self.noteEdit.setObjectName("noteEdit")
		self.add_button = QtWidgets.QPushButton(self.centralwidget)
		self.add_button.setGeometry(QtCore.QRect(0, 500, 391, 41))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.add_button.setFont(font)
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap("img/free-icon-font-add-3914248.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.add_button.setIcon(icon3)
		self.add_button.setObjectName("add_button")
		self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
		self.calendarWidget.setGeometry(QtCore.QRect(0, 60, 391, 331))
		self.calendarWidget.setObjectName("calendarWidget")
		self.notes = QtWidgets.QListWidget(self.centralwidget)
		self.notes.setGeometry(QtCore.QRect(395, 61, 401, 481))
		self.notes.setObjectName("notes")
		self.upload_button = QtWidgets.QPushButton(self.centralwidget)
		self.upload_button.setGeometry(QtCore.QRect(0, 550, 391, 41))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.upload_button.setFont(font)
		icon4 = QtGui.QIcon()
		icon4.addPixmap(QtGui.QPixmap("img/free-icon-font-download-3917330.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.upload_button.setIcon(icon4)
		self.upload_button.setObjectName("upload_button")
		self.delete_button = QtWidgets.QPushButton(self.centralwidget)
		self.delete_button.setGeometry(QtCore.QRect(400, 550, 401, 41))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.delete_button.setFont(font)
		icon5 = QtGui.QIcon()
		icon5.addPixmap(QtGui.QPixmap("img/free-icon-font-trash-3917242.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.delete_button.setIcon(icon5)
		self.delete_button.setObjectName("delete_button")
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.add_button.setText(_translate("MainWindow", "Добавить заметку"))
		self.upload_button.setText(_translate("MainWindow", "Загрузить с .txt"))
		self.delete_button.setText(_translate("MainWindow", "Удалить заметку"))


class Ui_Info(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(800, 600)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
		self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 51))
		self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.profile_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		self.profile_button.setText("")
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("img/free-icon-font-user-3917688.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.profile_button.setIcon(icon)
		self.profile_button.setIconSize(QtCore.QSize(40, 40))
		self.profile_button.setObjectName("profile_button")
		self.horizontalLayout.addWidget(self.profile_button)
		self.notes_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		self.notes_button.setText("")
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap("img/free-icon-font-edit-3917361.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.notes_button.setIcon(icon1)
		self.notes_button.setIconSize(QtCore.QSize(40, 40))
		self.notes_button.setObjectName("notes_button")
		self.horizontalLayout.addWidget(self.notes_button)
		self.info_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		self.info_button.setText("")
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap("img/free-icon-font-info-3916699.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.info_button.setIcon(icon2)
		self.info_button.setIconSize(QtCore.QSize(40, 40))
		self.info_button.setObjectName("info_button")
		self.horizontalLayout.addWidget(self.info_button)
		self.telegram_button = QtWidgets.QPushButton(self.centralwidget)
		self.telegram_button.setGeometry(QtCore.QRect(10, 90, 271, 241))
		self.telegram_button.setText("")
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap("img/kdlogo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.telegram_button.setIcon(icon3)
		self.telegram_button.setIconSize(QtCore.QSize(300, 300))
		self.telegram_button.setObjectName("telegram_button")
		self.logoButton = QtWidgets.QTextBrowser(self.centralwidget)
		self.logoButton.setGeometry(QtCore.QRect(295, 91, 501, 241))
		self.logoButton.setObjectName("logoButton")
		self.save_csv_button = QtWidgets.QPushButton(self.centralwidget)
		self.save_csv_button.setGeometry(QtCore.QRect(10, 370, 291, 71))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.save_csv_button.setFont(font)
		icon4 = QtGui.QIcon()
		icon4.addPixmap(QtGui.QPixmap("img/free-icon-font-align-justify-3917034.png"), QtGui.QIcon.Normal,
						QtGui.QIcon.Off)
		self.save_csv_button.setIcon(icon4)
		self.save_csv_button.setObjectName("save_csv_button")
		self.statsBrowser = QtWidgets.QTextBrowser(self.centralwidget)
		self.statsBrowser.setGeometry(QtCore.QRect(310, 360, 471, 121))
		self.statsBrowser.setObjectName("statsBrowser")
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.logoButton.setHtml(_translate("MainWindow",
										   "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
										   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
										   "p, li { white-space: pre-wrap; }\n"
										   "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
										   "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">YandexNotes - разработано специально для Яндекс.Лицей.</span></p>\n"
										   "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Описание проекта:</span></p>\n"
										   "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Возможность введение нескольких аккаунтов</span></p>\n"
										   "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Создание/Удаление заметок</span></p>\n"
										   "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Изменение профиля</span></p></body></html>"))
		self.save_csv_button.setText(_translate("MainWindow", "Получить все заметки csv"))
		self.statsBrowser.setHtml(_translate("MainWindow",
											 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
											 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
											 "p, li { white-space: pre-wrap; }\n"
											 "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
											 "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Статистика</span></p>\n"
											 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Всего пользователей:</span></p>\n"
											 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Всего заметок:</span></p></body></html>"))


class Ui_Profile(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(800, 600)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
		self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 51))
		self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.profile_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		self.profile_button.setText("")
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("img/free-icon-font-user-3917688.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.profile_button.setIcon(icon)
		self.profile_button.setIconSize(QtCore.QSize(40, 40))
		self.profile_button.setObjectName("profile_button")
		self.horizontalLayout.addWidget(self.profile_button)
		self.notes_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		self.notes_button.setText("")
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap("img/free-icon-font-edit-3917361.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.notes_button.setIcon(icon1)
		self.notes_button.setIconSize(QtCore.QSize(40, 40))
		self.notes_button.setObjectName("notes_button")
		self.horizontalLayout.addWidget(self.notes_button)
		self.info_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		self.info_button.setText("")
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap("img/free-icon-font-info-3916699.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.info_button.setIcon(icon2)
		self.info_button.setIconSize(QtCore.QSize(40, 40))
		self.info_button.setObjectName("info_button")
		self.horizontalLayout.addWidget(self.info_button)
		self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(270, 60, 287, 461))
		self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.verticalLayout.addWidget(self.label)
		self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label_2.setFont(font)
		self.label_2.setObjectName("label_2")
		self.verticalLayout.addWidget(self.label_2)
		self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label_3.setFont(font)
		self.label_3.setObjectName("label_3")
		self.verticalLayout.addWidget(self.label_3)
		self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label_4.setFont(font)
		self.label_4.setObjectName("label_4")
		self.verticalLayout.addWidget(self.label_4)
		self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label_5.setFont(font)
		self.label_5.setObjectName("label_5")
		self.verticalLayout.addWidget(self.label_5)
		self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label_6.setFont(font)
		self.label_6.setObjectName("label_6")
		self.verticalLayout.addWidget(self.label_6)
		self.leave_button = QtWidgets.QPushButton(self.centralwidget)
		self.leave_button.setGeometry(QtCore.QRect(0, 560, 121, 41))
		font = QtGui.QFont()
		font.setPointSize(16)
		self.leave_button.setFont(font)
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap("img/free-icon-font-exit-3917349.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.leave_button.setIcon(icon3)
		self.leave_button.setObjectName("leave_button")
		self.nameEdit = QtWidgets.QLineEdit(self.centralwidget)
		self.nameEdit.setGeometry(QtCore.QRect(560, 70, 231, 41))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.nameEdit.setFont(font)
		self.nameEdit.setText("")
		self.nameEdit.setObjectName("nameEdit")
		self.loginEdit = QtWidgets.QLineEdit(self.centralwidget)
		self.loginEdit.setGeometry(QtCore.QRect(560, 150, 231, 41))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.loginEdit.setFont(font)
		self.loginEdit.setDragEnabled(False)
		self.loginEdit.setReadOnly(True)
		self.loginEdit.setObjectName("loginEdit")
		self.dateEdit = QtWidgets.QLineEdit(self.centralwidget)
		self.dateEdit.setGeometry(QtCore.QRect(560, 230, 231, 41))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.dateEdit.setFont(font)
		self.dateEdit.setReadOnly(True)
		self.dateEdit.setObjectName("dateEdit")
		self.countnotesEdit = QtWidgets.QLineEdit(self.centralwidget)
		self.countnotesEdit.setGeometry(QtCore.QRect(560, 310, 231, 41))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.countnotesEdit.setFont(font)
		self.countnotesEdit.setReadOnly(True)
		self.countnotesEdit.setObjectName("countnotesEdit")
		self.lastnoteEdit = QtWidgets.QLineEdit(self.centralwidget)
		self.lastnoteEdit.setGeometry(QtCore.QRect(560, 460, 231, 41))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.lastnoteEdit.setFont(font)
		self.lastnoteEdit.setReadOnly(True)
		self.lastnoteEdit.setObjectName("lastnoteEdit")
		self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
		self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(560, 380, 231, 61))
		self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
		self.update_gender_radio = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
		self.update_gender_radio.setContentsMargins(0, 0, 0, 0)
		self.update_gender_radio.setObjectName("update_gender_radio")
		self.male_radio = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
		font = QtGui.QFont()
		font.setPointSize(12)
		self.male_radio.setFont(font)
		self.male_radio.setObjectName("male_radio")
		self.update_gender_radio.addWidget(self.male_radio)
		self.female_radio = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
		font = QtGui.QFont()
		font.setPointSize(12)
		self.female_radio.setFont(font)
		self.female_radio.setObjectName("female_radio")
		self.update_gender_radio.addWidget(self.female_radio)
		self.save_button = QtWidgets.QPushButton(self.centralwidget)
		self.save_button.setGeometry(QtCore.QRect(560, 520, 231, 71))
		font = QtGui.QFont()
		font.setPointSize(18)
		self.save_button.setFont(font)
		icon4 = QtGui.QIcon()
		icon4.addPixmap(QtGui.QPixmap("img/free-icon-font-check-3917084.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.save_button.setIcon(icon4)
		self.save_button.setObjectName("save_button")
		self.update_photo = QtWidgets.QPushButton(self.centralwidget)
		self.update_photo.setGeometry(QtCore.QRect(10, 310, 251, 51))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.update_photo.setFont(font)
		icon5 = QtGui.QIcon()
		icon5.addPixmap(QtGui.QPixmap("img/free-icon-font-picture-3917317.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.update_photo.setIcon(icon5)
		self.update_photo.setObjectName("update_photo")
		self.avatar_label = QtWidgets.QLabel(self.centralwidget)
		self.avatar_label.setGeometry(QtCore.QRect(10, 80, 231, 221))
		self.avatar_label.setText("")
		self.avatar_label.setObjectName("avatar_label")
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.label.setText(_translate("MainWindow", "Имя:"))
		self.label_2.setText(_translate("MainWindow", "Логин:"))
		self.label_3.setText(_translate("MainWindow", "Дата регистрации:"))
		self.label_4.setText(_translate("MainWindow", "Всего заметок:"))
		self.label_5.setText(_translate("MainWindow", "Пол:"))
		self.label_6.setText(_translate("MainWindow", "Последняя заметка:"))
		self.leave_button.setText(_translate("MainWindow", "Выйти"))
		self.male_radio.setText(_translate("MainWindow", "М"))
		self.female_radio.setText(_translate("MainWindow", "Ж"))
		self.save_button.setText(_translate("MainWindow", "Сохранить"))
		self.update_photo.setText(_translate("MainWindow", "Загрузить аватарку"))


class Ui_Login(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(800, 599)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(280, 30, 181, 81))
		font = QtGui.QFont()
		font.setPointSize(48)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.label_4 = QtWidgets.QLabel(self.centralwidget)
		self.label_4.setGeometry(QtCore.QRect(100, 250, 121, 41))
		font = QtGui.QFont()
		font.setPointSize(18)
		self.label_4.setFont(font)
		self.label_4.setObjectName("label_4")
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(120, 200, 121, 31))
		font = QtGui.QFont()
		font.setPointSize(18)
		self.label_3.setFont(font)
		self.label_3.setObjectName("label_3")
		self.loginEdit = QtWidgets.QTextEdit(self.centralwidget)
		self.loginEdit.setGeometry(QtCore.QRect(270, 200, 271, 31))
		self.loginEdit.setObjectName("loginEdit")
		self.passwordEdit = QtWidgets.QTextEdit(self.centralwidget)
		self.passwordEdit.setGeometry(QtCore.QRect(270, 260, 271, 31))
		self.passwordEdit.setObjectName("passwordEdit")
		self.login_button = QtWidgets.QPushButton(self.centralwidget)
		self.login_button.setGeometry(QtCore.QRect(270, 340, 251, 41))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.login_button.setFont(font)
		self.login_button.setObjectName("login_button")
		self.reg_button = QtWidgets.QPushButton(self.centralwidget)
		self.reg_button.setGeometry(QtCore.QRect(620, 510, 171, 41))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.reg_button.setFont(font)
		self.reg_button.setObjectName("reg_button")
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.label.setText(_translate("MainWindow", "Вход"))
		self.label_4.setText(_translate("MainWindow", "Пароль:"))
		self.label_3.setText(_translate("MainWindow", "Логин:"))
		self.loginEdit.setHtml(_translate("MainWindow",
										  "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
										  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
										  "p, li { white-space: pre-wrap; }\n"
										  "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
										  "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
		self.passwordEdit.setHtml(_translate("MainWindow",
											 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
											 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
											 "p, li { white-space: pre-wrap; }\n"
											 "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
											 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
		self.login_button.setText(_translate("MainWindow", "Войти"))
		self.reg_button.setText(_translate("MainWindow", "Регистрация"))


class Ui_Reg(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(800, 583)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.nameEdit = QtWidgets.QTextEdit(self.centralwidget)
		self.nameEdit.setGeometry(QtCore.QRect(280, 140, 271, 31))
		self.nameEdit.setObjectName("nameEdit")
		self.passwordEdit = QtWidgets.QTextEdit(self.centralwidget)
		self.passwordEdit.setGeometry(QtCore.QRect(280, 260, 271, 31))
		self.passwordEdit.setObjectName("passwordEdit")
		self.loginEdit = QtWidgets.QTextEdit(self.centralwidget)
		self.loginEdit.setGeometry(QtCore.QRect(280, 200, 271, 31))
		self.loginEdit.setObjectName("loginEdit")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(170, 10, 481, 111))
		font = QtGui.QFont()
		font.setPointSize(48)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(170, 130, 91, 41))
		font = QtGui.QFont()
		font.setPointSize(18)
		self.label_2.setFont(font)
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(140, 200, 121, 31))
		font = QtGui.QFont()
		font.setPointSize(18)
		self.label_3.setFont(font)
		self.label_3.setObjectName("label_3")
		self.label_4 = QtWidgets.QLabel(self.centralwidget)
		self.label_4.setGeometry(QtCore.QRect(120, 250, 121, 41))
		font = QtGui.QFont()
		font.setPointSize(18)
		self.label_4.setFont(font)
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(self.centralwidget)
		self.label_5.setGeometry(QtCore.QRect(170, 330, 81, 41))
		font = QtGui.QFont()
		font.setPointSize(18)
		self.label_5.setFont(font)
		self.label_5.setObjectName("label_5")
		self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
		self.horizontalLayoutWidget.setGeometry(QtCore.QRect(290, 320, 160, 80))
		self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
		self.genderlayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
		self.genderlayout.setContentsMargins(0, 0, 0, 0)
		self.genderlayout.setObjectName("genderlayout")
		self.male = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
		font = QtGui.QFont()
		font.setPointSize(12)
		self.male.setFont(font)
		self.male.setObjectName("male")
		self.genderlayout.addWidget(self.male)
		self.female = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
		font = QtGui.QFont()
		font.setPointSize(12)
		self.female.setFont(font)
		self.female.setObjectName("female")
		self.genderlayout.addWidget(self.female)
		self.login_button = QtWidgets.QPushButton(self.centralwidget)
		self.login_button.setGeometry(QtCore.QRect(620, 520, 171, 41))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.login_button.setFont(font)
		self.login_button.setObjectName("login_button")
		self.reg_button2 = QtWidgets.QPushButton(self.centralwidget)
		self.reg_button2.setGeometry(QtCore.QRect(250, 430, 251, 41))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.reg_button2.setFont(font)
		self.reg_button2.setObjectName("reg_button2")
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.nameEdit.setHtml(_translate("MainWindow",
										 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
										 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
										 "p, li { white-space: pre-wrap; }\n"
										 "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
										 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
		self.passwordEdit.setHtml(_translate("MainWindow",
											 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
											 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
											 "p, li { white-space: pre-wrap; }\n"
											 "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
											 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
		self.loginEdit.setHtml(_translate("MainWindow",
										  "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
										  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
										  "p, li { white-space: pre-wrap; }\n"
										  "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
										  "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
		self.label.setText(_translate("MainWindow", "Регистрация"))
		self.label_2.setText(_translate("MainWindow", "Имя:"))
		self.label_3.setText(_translate("MainWindow", "Логин:"))
		self.label_4.setText(_translate("MainWindow", "Пароль:"))
		self.label_5.setText(_translate("MainWindow", "Пол:"))
		self.male.setText(_translate("MainWindow", "М"))
		self.female.setText(_translate("MainWindow", "Ж"))
		self.login_button.setText(_translate("MainWindow", "Вход"))
		self.reg_button2.setText(_translate("MainWindow", "Зарегистрироваться"))


class Dada(QMainWindow):
	def __init__(self):
		super().__init__()

		# Создаем QStackedWidget для управления несколькими экранами
		self.stacked_widget = QStackedWidget(self)

		# Создаем экраны и добавляем их в QStackedWidget
		self.screen1 = Register()
		self.stacked_widget.addWidget(self.screen1)

		self.screen2 = Login()
		self.stacked_widget.addWidget(self.screen2)

		self.screen3 = Profile()
		self.stacked_widget.addWidget(self.screen3)

		self.screen4 = Notes()
		self.stacked_widget.addWidget(self.screen4)

		self.screen5 = Info()
		self.stacked_widget.addWidget(self.screen5)

		self.setCentralWidget(self.stacked_widget)


class MyWidget(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("YandexNotes")
		self.setFixedSize(800, 599)
		self.dada = Dada()
		self.setCentralWidget(self.dada)


class Profile(QMainWindow, Ui_Profile):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.avatar_label.setGeometry(
			50, 100, 200, 200
		)  # Установка размеров и позиции для метки с аватаркой
		self.avatar_label.setScaledContents(
			True
		)  # Установка масштабирования содержимого метки
		self.notes_button.clicked.connect(
			self.show_widget3
		)  # Установка действия по нажатию на кнопку "Заметки"
		self.info_button.clicked.connect(
			self.show_widget4
		)  # Установка действия по нажатию на кнопку "Информация"
		self.save_button.clicked.connect(
			self.save_new_info_user
		)  # Установка действия по нажатию на кнопку "Сохранить"
		self.leave_button.clicked.connect(
			self.leave_account
		)  # Установка действия по нажатию на кнопку "Выйти"
		self.update_photo.clicked.connect(
			self.upload_avatar
		)  # Установка действия по нажатию на кнопку "Обновить фото"

	def save_new_info_user(self):
		# Функция сохраняет новую информацию о пользователе
		if self.male_radio.isChecked():  # Проверка выбранного пола (мужской/женский)
			gender = "Мужской"
		else:
			gender = "Женский"
		new_name = (
			self.nameEdit.text()
		)  # Получение нового имени пользователя из текстового поля
		login = open(
			"login_online.txt", "r"
		).read()  # Получение текущего логина из файла
		self.con = sqlite3.connect("main.db")  # Подключение к базе данных
		self.cur = self.con.cursor()
		self.cur.execute(
			f'''UPDATE users SET name = "{new_name}" WHERE login = "{login}"'''
		)  # Обновление имени пользователя в базе данных
		self.cur.execute(
			f'''UPDATE users SET gender = "{gender}" WHERE login = "{login}"'''
		)  # Обновление пола пользователя в базе данных
		self.con.commit()  # Сохранение изменений в базе данных
		self.con.close()  # Закрытие соединения с базой данных

	def leave_account(self):
		# Функция выхода из аккаунта
		self.parent().parent().stacked_widget.setCurrentIndex(
			0
		)  # Переключение на главный виджет

	def get_profile(self):
		# Функция получения профиля пользователя
		self.con = sqlite3.connect("main.db")  # Подключение к базе данных
		self.cur = self.con.cursor()
		login = open(
			"login_online.txt", "r"
		).read()  # Получение текущего логина из файла
		user = self.cur.execute(
			f"SELECT * FROM users WHERE login='{login}'"
		).fetchone()  # Получение информации о пользователе из базы данных
		notes = self.cur.execute(
			f'''SELECT * FROM notes WHERE login="{login}"'''
		).fetchall()  # Получение заметок пользователя из базы данных
		self.nameEdit.setText(
			str(user[4])
		)  # Установка имени пользователя в текстовое поле
		self.loginEdit.setText(
			str(user[0])
		)  # Установка логина пользователя в текстовое поле
		self.dateEdit.setText(
			str(user[2])
		)  # Установка даты регистрации пользователя в текстовое поле
		self.countnotesEdit.setText(
			str(len(notes))
		)  # Установка количества заметок пользователя в текстовое поле
		if len(notes) != 0:
			self.lastnoteEdit.setText(
				str(notes[-1][3])
			)  # Установка последней заметки пользователя в текстовое поле
		if user[3] == "Мужской":  # Проверка пола пользователя
			self.male_radio.setChecked(
				True
			)  # Установка переключателя пола пользователя в положение "Мужской"
		else:
			self.female_radio.setChecked(
				True
			)  # Установка переключателя пола пользователя в положение "Женский"
		if user[5] != "":
			try:
				pixmap = QPixmap(user[5])  # Загрузка фото пользователя
				self.avatar_label.setPixmap(
					pixmap
				)  # Установка фото пользователя на метку
			except FileNotFoundError:
				pass
		self.con.close()  # Закрытие соединения с базой данных

	def upload_avatar(self):
		# Функция загружает аватар пользователя изображением
		file_dialog = QFileDialog()  # Создание диалогового окна выбора файла
		file_path, _ = file_dialog.getOpenFileName(
			self, "Select Avatar Image", "", "Image Files (*.png *.jpg *.jpeg)"
		)  # Получение выбранного пути к файлу
		if file_path:
			self.display_avatar(file_path)  # Отображение выбранного изображения аватара

	def display_avatar(self, file_path):
		# Функция отображает выбранное изображение аватара
		self.con = sqlite3.connect("main.db")  # Подключение к базе данных SQLite
		self.cur = self.con.cursor()
		login = open(
			"login_online.txt", "r"
		).read()  # Чтение логина пользователя из файла
		self.cur.execute(
			f'''UPDATE users SET photo_path = "{file_path}" WHERE login = "{login}"'''
		)  # Обновление пути к файлу аватара в базе данных
		self.con.commit()  # Фиксация изменений в базе данных
		self.con.close()  # Закрытие соединения с базой данных
		pixmap = QPixmap(file_path)  # Создание объекта QPixmap с выбранным изображением
		self.avatar_label.setPixmap(
			pixmap
		)  # Установка выбранного изображения в метку аватара

	def show_widget3(self):
		# Функция переключает отображение на экран "Заметки"
		self.parent().parent().screen4.all_history()  # Вызов функции на экране "Заметки" для обновления истории заметок
		self.parent().parent().stacked_widget.setCurrentIndex(
			3
		)  # Установка отображения текущего экрана на экран "Заметки"

	def show_widget4(self):
		# Функция переключает отображение на экран "Информация"
		self.parent().parent().screen5.update_info()  # Вызов функции на экране "Информация" для обновления информации
		self.parent().parent().stacked_widget.setCurrentIndex(
			4
		)  # Установка отображения текущего экрана на экран "Информация"


class Info(QMainWindow, Ui_Info):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.profile_button.clicked.connect(
			self.show_widget2
		)  # Установка действия по нажатию на кнопку "Профиль"
		self.notes_button.clicked.connect(
			self.show_widget3
		)  # Установка действия по нажатию на кнопку "Заметки"
		self.info_button.clicked.connect(
			self.show_widget4
		)  # Установка действия по нажатию на кнопку "Информация"
		self.save_csv_button.clicked.connect(
			self.get_csv
		)  # Установка действия по нажатию на кнопку "Сохранить в CSV"
		self.telegram_button.clicked.connect(
			self.telegram_link
		)  # Установка действия по нажатию на кнопку "Telegram"

	def update_info(self):
		self.con = sqlite3.connect("main.db")  # Подключаемся к базе данных "main.db"
		self.cur = self.con.cursor()  # Создаем курсор для выполнения SQL-запросов
		all_users = self.cur.execute(
			f"""SELECT * FROM users"""
		).fetchall()  # Извлекаем всех пользователей из таблицы "users"
		all_notes = self.cur.execute(
			f"""SELECT * FROM notes"""
		).fetchall()  # Извлекаем все заметки из таблицы "notes"
		self.statsBrowser.setHtml(
			'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
			'<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
			"p, li { white-space: pre-wrap; }\n"
			"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
			'<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt; font-weight:600;">Статистика</span></p>\n'
			f'<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">Всего пользователей: {len(all_users)}</span></p>\n'
			f'<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">Всего заметок: {len(all_notes)}</span></p></body></html>'
		)

	def telegram_link(self):
		url = QUrl(
			"https://t.me/by_KoDi"
		)  # Создаем объект URL со ссылкой на Telegram-создателя
		QDesktopServices.openUrl(url)  # Открываем ссылку в браузере

	def get_csv(self):
		try:
			with open("YandexNotes.csv", "w", newline="") as file:
				self.con = sqlite3.connect(
					"main.db"
				)  # Подключение к базе данных "main.db"
				self.cur = (
					self.con.cursor()
				)  # Создание объекта курсора для выполнения SQL-запросов
				data = self.cur.execute(
					f"""SELECT * FROM notes"""
				)  # Выполнение SQL-запроса для получения данных из таблицы "notes"
				writer = csv.writer(
					file
				)  # Создание объекта для записи данных в CSV-файл
				writer.writerows(data)  # Запись данных из запроса в CSV-файл
			dialog = QDialog(self)
			dialog.setWindowTitle("Сохранено!")
			layout = QVBoxLayout(dialog)
			label = QLabel(
				".csv успешно сохранено под названием YandexNotes.csv", dialog
			)
			layout.addWidget(label)
			dialog.exec_()
		except Exception as ex:  # Обработка исключения
			dialog = QDialog(self)
			dialog.setWindowTitle("Ошибка!")
			layout = QVBoxLayout(dialog)
			label = QLabel(f"Произошла ошибка - {ex}", dialog)
			layout.addWidget(label)
			dialog.exec_()

	def show_widget2(self):
		self.parent().parent().screen3.get_profile()  # Вызов метода "get_profile()" экрана "screen3"
		self.parent().parent().stacked_widget.setCurrentIndex(
			2
		)  # Установка текущего индекса виджета "stacked_widget" в 2

	def show_widget3(self):
		self.parent().parent().screen4.all_history()  # Вызов метода "all_history()" экрана "screen4"
		self.parent().parent().stacked_widget.setCurrentIndex(
			3
		)  # Установка текущего индекса виджета "stacked_widget" в 3

	def show_widget4(self):
		self.parent().parent().screen5.update_info()  # Вызов метода "update_info()" экрана "screen5"
		self.parent().parent().stacked_widget.setCurrentIndex(
			4
		)  # Установка текущего индекса виджета "stacked_widget" в 4


class Notes(QMainWindow, Ui_Notes):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.profile_button.clicked.connect(
			self.show_widget2
		)  # Привязка нажатия кнопки "profile_button" к методу "show_widget2"
		self.notes_button.clicked.connect(
			self.show_widget3
		)  # Привязка нажатия кнопки "notes_button" к методу "show_widget3"
		self.info_button.clicked.connect(
			self.show_widget4
		)  # Привязка нажатия кнопки "info_button" к методу "show_widget4"
		self.add_button.clicked.connect(
			self.add_note
		)  # Привязка нажатия кнопки "add_button" к методу "add_note"
		self.upload_button.clicked.connect(
			self.upload_txt
		)  # Привязка нажатия кнопки "upload_button" к методу "upload_txt"
		self.delete_button.clicked.connect(
			self.del_note
		)  # Привязка нажатия кнопки "delete_button" к методу "del_note"

	def show_widget2(self):
		self.parent().parent().screen3.get_profile()  # Вызов метода "get_profile()" экрана "screen3" у родительского родительского виджета
		self.parent().parent().stacked_widget.setCurrentIndex(
			2
		)  # Установка текущего индекса виджета "stacked_widget" в 2

	def show_widget3(self):
		self.parent().parent().screen4.all_history()  # Вызов метода "all_history()" экрана "screen4" у родительского родительского виджета
		self.parent().parent().stacked_widget.setCurrentIndex(
			3
		)  # Установка текущего индекса виджета "stacked_widget" в 3

	def show_widget4(self):
		self.parent().parent().screen5.update_info()  # Вызов метода "update_info()" экрана "screen5" у родительского родительского виджета
		self.parent().parent().stacked_widget.setCurrentIndex(
			4
		)  # Установка текущего индекса виджета "stacked_widget" в 4

	def add_note(self):
		# Получение выбранной пользователем даты из виджета календаря
		year = self.calendarWidget.selectedDate().year()
		month = (
			self.calendarWidget.selectedDate().month()
			if len(str(self.calendarWidget.selectedDate().month())) == 2
			else "0" + str(self.calendarWidget.selectedDate().month())
		)
		day = (
			self.calendarWidget.selectedDate().day()
			if len(str(self.calendarWidget.selectedDate().day())) == 2
			else "0" + str(self.calendarWidget.selectedDate().day())
		)

		# Создание строки с полной датой в формате "гггг-мм-дд"
		all_year = f"{year}-{month}-{day}"

		# Подключение к базе данных и получение последнего использованного идентификатора
		self.con = sqlite3.connect("main.db")
		self.cur = self.con.cursor()
		self.cur.execute("SELECT MAX(id) FROM ids")
		last_id = self.cur.fetchone()[0]

		# Формирование текста заметки с добавлением идентификатора и полной даты
		text_note = f"{last_id + 1}) {all_year} - {self.noteEdit.toPlainText()}"

		# Обновление идентификатора в базе данных
		self.cur.execute(f'''UPDATE ids SET id = "{int(last_id) + 1}"''')

		# Добавление текста заметки к списку заметок в пользовательском интерфейсе
		self.notes.addItem(text_note)

		# Получение имени пользователя из файла login_online.txt
		f = open("login_online.txt", "r").read()

		# Формирование данных для добавления в базу данных
		data = (last_id + 1, f, self.noteEdit.toPlainText(), all_year)

		# Выполнение запроса на добавление заметки в базу данных
		self.cur.execute("INSERT INTO notes VALUES (?, ?, ?, ?)", data)

		# Очистка поля ввода новой заметки
		self.noteEdit.clear()

		# Применение изменений в базе данных и закрытие соединения
		self.con.commit()
		self.con.close()

	def upload_txt(self):
		# Открытие диалогового окна для выбора файла txt
		file_dialog = QFileDialog()
		file_dialog.setNameFilters(["Text files (*.txt)"])
		file_dialog.exec_()
		selected_file = file_dialog.selectedFiles()[0]

		# Чтение содержимого выбранного файла и добавление его в поле ввода заметки
		f = open(selected_file, "r").read()
		self.noteEdit.clear()
		self.noteEdit.appendPlainText(str(f))

	def del_note(self):
		# Получение выбранных пользователем элементов списка заметок
		selected_items = self.notes.selectedItems()

		# Удаление каждого выбранного элемента из базы данных и списка заметок
		for item in selected_items:
			self.con = sqlite3.connect("main.db")
			self.cur = self.con.cursor()

			# Получение идентификатора заметки для удаления
			id = item.text().find(")")
			idd = item.text()[:id]

			# Выполнение запроса на удаление заметки из базы данных
			self.cur.execute(f"""DELETE FROM notes WHERE id = {idd}""")

			# Применение изменений в базе данных и закрытие соединения
			self.con.commit()
			self.con.close()

			# Удаление выбранной заметки из списка заметок в пользовательском интерфейсе
			self.notes.takeItem(self.notes.row(item))

	def all_history(self):
		# Чтение логина пользователя из файла login_online.txt
		login = open("login_online.txt", "r").read()

		# Подключение к базе данных
		self.con = sqlite3.connect("main.db")
		self.cur = self.con.cursor()

		# Получение всех записей пользователя из таблицы notes
		all_notes = self.cur.execute(
			f'''SELECT * FROM notes WHERE login="{login}"'''
		).fetchall()

		# Если есть записи
		if len(all_notes) != 0:
			# Очистка текстового поля для заметок и списка заметок
			self.noteEdit.clear()
			self.notes.clear()

			# Добавление каждой заметки в список заметок
			for note in all_notes:
				text_note = f"{note[0]}) {note[3]} - {note[2]}"
				self.notes.addItem(text_note)


class Login(QMainWindow, Ui_Login):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.status_bar = QStatusBar()
		self.setStatusBar(self.status_bar)
		self.reg_button.clicked.connect(self.show_widget2)
		self.login_button.clicked.connect(self.login_user)

	def login_user(self):
		# Подключение к базе данных
		self.con = sqlite3.connect("main.db")
		self.cur = self.con.cursor()

		# Получение пользователя по логину из таблицы users
		user = self.cur.execute(
			f"SELECT * FROM users WHERE login='{self.loginEdit.toPlainText()}'"
		).fetchone()

		if user is not None:
			# Получение пароля пользователя
			password = self.cur.execute(
				f'''SELECT password FROM users WHERE login="{self.loginEdit.toPlainText()}"'''
			).fetchone()
			if self.passwordEdit.toPlainText() == password[0]:
				# Запись логина в файл login_online.txt
				f = open("login_online.txt", "w")
				f.write(self.loginEdit.toPlainText())
				f.close()

				# Получение профиля пользователя
				self.parent().parent().screen3.get_profile()

				# Переход на главный экран
				self.parent().parent().stacked_widget.setCurrentIndex(2)

				# Очистка полей ввода логина и пароля
				self.loginEdit.clear()
				self.passwordEdit.clear()
				self.con.close()
			else:
				self.status_bar.showMessage("Пароль неверный!")
		else:
			self.status_bar.showMessage(
				"Пользователя с таким логином не существует. Сначала создайте новый аккаунт!"
			)

	def show_widget2(self):
		# Переход к экрану регистрации
		self.parent().parent().stacked_widget.setCurrentIndex(0)


class Register(QMainWindow, Ui_Reg):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.status_bar = QStatusBar()
		self.setStatusBar(self.status_bar)
		self.login_button.clicked.connect(
			self.show_widget1
		)  # При нажатии на кнопку login_button вызывается функция show_widget1
		self.reg_button2.clicked.connect(
			self.register_user
		)  # При нажатии на кнопку reg_button2 вызывается функция register_user

	def register_user(self):
		# Проверка, чтобы все поля были заполнены и не было выбрано ни одного значения из группы кнопок male и female
		if (
				self.nameEdit.toPlainText() != ""
				and self.loginEdit.toPlainText() != ""
				and self.passwordEdit.toPlainText() != ""
				and (not self.male.isChecked() or not self.female.isChecked())
		):
			self.con = sqlite3.connect("main.db")
			self.cur = self.con.cursor()
			# Проверка, существует ли пользователь с таким логином в базе данных
			user = self.cur.execute(
				f"SELECT * FROM users WHERE login='{self.loginEdit.toPlainText()}'"
			).fetchone()
			if user is not None:
				self.status_bar.showMessage("Пользователь с таким логином уже есть")
			else:
				# Получение текущей даты
				startdate = datetime.today().strftime("%Y-%m-%d")
				# Создание кортежа с данными нового пользователя
				data = (
					self.loginEdit.toPlainText(),
					self.passwordEdit.toPlainText(),
					startdate,
					"Мужской" if self.male.isChecked() else "Женский",
					self.nameEdit.toPlainText(),
					"",
				)
				# Добавление нового пользователя в таблицу users
				self.cur.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)", data)
				self.con.commit()
				f = open("login_online.txt", "w")
				f.write(self.loginEdit.toPlainText())
				f.close()
				# Получение данных зарегистрированного пользователя из базы данных
				self.parent().parent().screen3.get_profile()
				# Переключение на экран профиля
				self.parent().parent().stacked_widget.setCurrentIndex(2)
				self.nameEdit.clear()
				self.loginEdit.clear()
				self.passwordEdit.clear()
				self.con.close()
		else:
			self.status_bar.showMessage("Вы заполнили не все данные")

	def show_widget1(self):
		self.parent().parent().stacked_widget.setCurrentIndex(1)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = MyWidget()
	ex.show()
	sys.exit(app.exec_())
