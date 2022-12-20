from PySide6 import QtCore
from PySide6 import QtWidgets, QtGui

from UI.QClickableLabel import QClickableLabel

class QGeneratedImageLabel(QClickableLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.loadPlaceholderImage()

        self.mouseLeftButtonClickedSignal.connect(self.onClicked)
        self.mouseRightButtonClickedSignal.connect(self.onClicked)

    def loadPlaceholderImage(self):
        self.loadImageWithText("Try to generate an image, it will be displayed here!")

    def loadWaitingImage(self, width=768, height=768):
        self.loadImageWithText("Generation in progress, please wait...", width, height)

    def loadImageWithText(self, text:str, width=768, height=768):
        image = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)
        
        painter = QtGui.QPainter()
        painter.begin(image)
        font = painter.font()
        font.setPixelSize(14)
        painter.setFont(font)
        imageRect = QtCore.QRectF(0, 0, width, height)
        textOptions = QtGui.QTextOption(QtGui.Qt.AlignCenter | QtGui.Qt.AlignVCenter)
        backgroundColor = QtGui.QColor.fromRgb(200, 200, 200)
        painter.fillRect(imageRect, backgroundColor)
        painter.setPen(QtGui.QPen(QtGui.QColor.fromRgb(150, 150, 150)))
        painter.drawText(imageRect, text, textOptions)
        painter.end()

        self.setPixmap(QtGui.QPixmap.fromImage(image))

    @QtCore.Slot()
    def onClicked(self):
        dir = QtCore.QDir.homePath()
        filename = QtWidgets.QFileDialog.getSaveFileName(self, "Save image...", dir, "Images (*.png)")
        if filename[0]:
            self.pixmap().toImage().save(filename[0], "PNG")
        