import sys
from PySide6 import QtWidgets, QtCore

from UI.MainWindow import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    accessToken = str()
    accessTokenFile = QtCore.QFile("accessToken.txt")
    if accessTokenFile.open(QtCore.QIODevice.ReadOnly):
        textStream = QtCore.QTextStream(accessTokenFile)
        accessToken = textStream.readAll()

    if accessToken:
        mainWindow = MainWindow(accessToken)
        mainWindow.setWindowTitle("Picture Machine")
        mainWindow.show()
        sys.exit(app.exec())
    else:
        print("Cannot find access token in accessToken.txt")
        sys.exit(0)
