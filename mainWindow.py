# https://stackoverflow.com/questions/58599351/integrate-qt-designer-and-pycharm

################################################################################
## Form generated from reading UI file 'MainUI.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
################################################################################

from PIL import Image
import numpy
from math import ceil

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, Slot, QTranslator as tr, QDir)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
                               QPushButton, QSizePolicy, QStatusBar, QWidget, QFileDialog)

filename = ''
pixelatedImg = None
pxlFilePath = ''



def pixelate(img):
    global pixelatedImg
    x, y = img.size
    if x == 1 or y == 1:
        return None

    a = numpy.array(img)
    # print(len(a))

    pixel_rate = 3


    t = 1

    try:
        a = numpy.delete(a, list(range(t, a.shape[0], pixel_rate)), axis=0)
    except IndexError:
        return None
    try:
        a = numpy.delete(a, list(range(t, a.shape[1], pixel_rate)), axis=1)
    except IndexError:
        return None
    # print(a.shape[0], a.shape[1])

    if t == 0:
        t = 1
    else:
        t = 0

    pixelatedImg = Image.fromarray(a)
    return pixelatedImg


class Ui_PixelateImg(object):
    def setupUi(self, PixelateImg):
        if not PixelateImg.objectName():
            PixelateImg.setObjectName(u"PixelateImg")
        PixelateImg.resize(1116, 746)
        self.centralwidget = QWidget(PixelateImg)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 30, 251, 31))
        font = QFont()
        font.setFamilies([u"Hack"])
        font.setPointSize(16)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(710, 30, 271, 31))
        self.label_2.setFont(font)
        self.uploadImgButton = QPushButton(self.centralwidget)
        self.uploadImgButton.setObjectName(u"uploadImgButton")
        self.uploadImgButton.setGeometry(QRect(50, 530, 111, 31))

        font1 = QFont()
        font1.setFamilies([u"Hack"])
        self.uploadImgButton.setFont(font1)
        self.pixelateButton = QPushButton(self.centralwidget)
        self.pixelateButton.setObjectName(u"pixelateButton")
        self.pixelateButton.setGeometry(QRect(440, 550, 231, 121))
        self.pixelateButton.setFont(font)
        self.imageLabelPrePixel = QLabel(self.centralwidget)
        self.imageLabelPrePixel.setObjectName(u"imageLabelPrePixel")
        self.imageLabelPrePixel.setGeometry(QRect(40, 70, 461, 421))
        self.imageLabelPostPixel = QLabel(self.centralwidget)
        self.imageLabelPostPixel.setObjectName(u"imageLabelPostPixel")
        self.imageLabelPostPixel.setGeometry(QRect(610, 70, 461, 421))
        PixelateImg.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PixelateImg)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1116, 22))
        PixelateImg.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PixelateImg)
        self.statusbar.setObjectName(u"statusbar")
        PixelateImg.setStatusBar(self.statusbar)

        self.retranslateUi(PixelateImg)

        QMetaObject.connectSlotsByName(PixelateImg)
        self.uploadImgButton.clicked.connect(self.setPreImage)
        self.pixelateButton.clicked.connect(self.setPixelImg)

    # setupUi

    def retranslateUi(self, PixelateImg):
        PixelateImg.setWindowTitle(QCoreApplication.translate("PixelateImg", u"PixelateImg", None))
        self.label.setText(QCoreApplication.translate("PixelateImg", u"Pre-Pixelated Image", None))
        self.label_2.setText(QCoreApplication.translate("PixelateImg", u"Post-Pixelated Image", None))
        self.uploadImgButton.setText(QCoreApplication.translate("PixelateImg", u"Upload Image", None))
        self.pixelateButton.setText(QCoreApplication.translate("PixelateImg", u"PIXELATE", None))
        self.imageLabelPrePixel.setText("")
        self.imageLabelPostPixel.setText("")

    # retranslateUi

    def setPreImage(self):
        global pixelatedImg  # reset the pixelated image
        pixelatedImg = None
        self.imageLabelPostPixel.clear()

        global filename
        filename, _ = QFileDialog.getOpenFileName(None, 'Select Image', '', 'Image Files (*.jpg, *.jpeg, *.png)')
        if filename:
            print(filename)
            pixmap = QPixmap(filename)
            pixmap = pixmap.scaled(self.imageLabelPrePixel.width(), self.imageLabelPrePixel.height(),
                                   Qt.KeepAspectRatio)
            self.imageLabelPrePixel.setPixmap(pixmap)
            self.imageLabelPrePixel.setAlignment(Qt.AlignCenter)

    def setPixelImg(self):
        global pixelatedImg
        global filename
        global pxlFilePath
        if filename:  # check if there is already an image loaded to pixelate
            if not pixelatedImg:  # check if there is already a pixelated image
                image = Image.open(filename)
            else:
                image = pixelatedImg
            toPixelate = image.copy()
            pixelized = pixelate(toPixelate)
            if pixelized is None:
                print("image has reached maximum pixelization")
                return
            pxlfilepath = Put your filepath here where you want the pixelated image to be saved
            pixelized.save(pxlfilepath, quality=95)
            pixmap = QPixmap(pxlfilepath)
            pixmap = pixmap.scaled(self.imageLabelPostPixel.width(), self.imageLabelPostPixel.height(),
                                   Qt.KeepAspectRatio)
            self.imageLabelPostPixel.setPixmap(pixmap)
            self.imageLabelPostPixel.setAlignment(Qt.AlignCenter)
        else:
            print('no filename')
