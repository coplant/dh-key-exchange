# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow_2.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 232)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(400, 232))
        MainWindow.setMaximumSize(QSize(400, 232))
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet(u"")
        self.action_open = QAction(MainWindow)
        self.action_open.setObjectName(u"action_open")
        self.action_save = QAction(MainWindow)
        self.action_save.setObjectName(u"action_save")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMaximumSize(QSize(100000, 100000))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_calc = QPushButton(self.centralwidget)
        self.btn_calc.setObjectName(u"btn_calc")

        self.horizontalLayout_3.addWidget(self.btn_calc)


        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setHorizontalSpacing(2)
        self.formLayout.setVerticalSpacing(6)
        self.P = QLabel(self.centralwidget)
        self.P.setObjectName(u"P")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.P)

        self.line_P = QLineEdit(self.centralwidget)
        self.line_P.setObjectName(u"line_P")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.line_P)

        self.A = QLabel(self.centralwidget)
        self.A.setObjectName(u"A")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.A)

        self.line_A = QLineEdit(self.centralwidget)
        self.line_A.setObjectName(u"line_A")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.line_A)


        self.horizontalLayout.addLayout(self.formLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.btn_generate = QPushButton(self.centralwidget)
        self.btn_generate.setObjectName(u"btn_generate")

        self.verticalLayout.addWidget(self.btn_generate)

        self.btn_clear = QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(u"btn_clear")

        self.verticalLayout.addWidget(self.btn_clear)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.a_X = QLabel(self.centralwidget)
        self.a_X.setObjectName(u"a_X")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.a_X)

        self.a_line_X = QLineEdit(self.centralwidget)
        self.a_line_X.setObjectName(u"a_line_X")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.a_line_X)

        self.a_Y = QLabel(self.centralwidget)
        self.a_Y.setObjectName(u"a_Y")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.a_Y)

        self.a_line_Y1 = QLineEdit(self.centralwidget)
        self.a_line_Y1.setObjectName(u"a_line_Y1")
        self.a_line_Y1.setReadOnly(True)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.a_line_Y1)

        self.a_Y_2 = QLabel(self.centralwidget)
        self.a_Y_2.setObjectName(u"a_Y_2")
        font = QFont()
        font.setPointSize(9)
        font.setItalic(False)
        font.setUnderline(False)
        self.a_Y_2.setFont(font)
        self.a_Y_2.setTextFormat(Qt.MarkdownText)

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.a_Y_2)

        self.a_line_Y2 = QLineEdit(self.centralwidget)
        self.a_line_Y2.setObjectName(u"a_line_Y2")
        self.a_line_Y2.setReadOnly(True)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.a_line_Y2)

        self.a_Z = QLabel(self.centralwidget)
        self.a_Z.setObjectName(u"a_Z")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.a_Z)

        self.a_line_Z = QLineEdit(self.centralwidget)
        self.a_line_Z.setObjectName(u"a_line_Z")
        self.a_line_Z.setReadOnly(True)

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.a_line_Z)


        self.horizontalLayout_2.addLayout(self.formLayout_4)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.b_X = QLabel(self.centralwidget)
        self.b_X.setObjectName(u"b_X")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.b_X)

        self.b_line_X = QLineEdit(self.centralwidget)
        self.b_line_X.setObjectName(u"b_line_X")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.b_line_X)

        self.b_Y = QLabel(self.centralwidget)
        self.b_Y.setObjectName(u"b_Y")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.b_Y)

        self.b_line_Y2 = QLineEdit(self.centralwidget)
        self.b_line_Y2.setObjectName(u"b_line_Y2")
        self.b_line_Y2.setReadOnly(True)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.b_line_Y2)

        self.b_Y_2 = QLabel(self.centralwidget)
        self.b_Y_2.setObjectName(u"b_Y_2")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.b_Y_2)

        self.b_line_Y1 = QLineEdit(self.centralwidget)
        self.b_line_Y1.setObjectName(u"b_line_Y1")
        self.b_line_Y1.setReadOnly(True)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.b_line_Y1)

        self.b_Z = QLabel(self.centralwidget)
        self.b_Z.setObjectName(u"b_Z")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.b_Z)

        self.b_line_Z = QLineEdit(self.centralwidget)
        self.b_line_Z.setObjectName(u"b_line_Z")
        self.b_line_Z.setReadOnly(True)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.b_line_Z)


        self.horizontalLayout_2.addLayout(self.formLayout_3)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.line_P, self.line_A)
        QWidget.setTabOrder(self.line_A, self.a_line_X)
        QWidget.setTabOrder(self.a_line_X, self.b_line_X)
        QWidget.setTabOrder(self.b_line_X, self.btn_generate)
        QWidget.setTabOrder(self.btn_generate, self.btn_clear)
        QWidget.setTabOrder(self.btn_clear, self.btn_calc)
        QWidget.setTabOrder(self.btn_calc, self.b_line_Z)
        QWidget.setTabOrder(self.b_line_Z, self.a_line_Z)
        QWidget.setTabOrder(self.a_line_Z, self.a_line_Y1)
        QWidget.setTabOrder(self.a_line_Y1, self.a_line_Y2)
        QWidget.setTabOrder(self.a_line_Y2, self.b_line_Y1)
        QWidget.setTabOrder(self.b_line_Y1, self.b_line_Y2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"lab_11: Deffie-Hellman", None))
        self.action_open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.action_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_calc.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.P.setText(QCoreApplication.translate("MainWindow", u"P: ", None))
        self.A.setText(QCoreApplication.translate("MainWindow", u"A: ", None))
        self.btn_generate.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.a_X.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.a_Y.setText(QCoreApplication.translate("MainWindow", u"Y1:", None))
        self.a_Y_2.setText(QCoreApplication.translate("MainWindow", u"Y2:", None))
        self.a_Z.setText(QCoreApplication.translate("MainWindow", u"Z:", None))
        self.b_X.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.b_Y.setText(QCoreApplication.translate("MainWindow", u"Y2:", None))
        self.b_Y_2.setText(QCoreApplication.translate("MainWindow", u"Y1:", None))
        self.b_Z.setText(QCoreApplication.translate("MainWindow", u"Z:", None))
    # retranslateUi

