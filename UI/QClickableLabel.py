from PySide6 import QtCore
from PySide6 import QtWidgets, QtGui

class QClickableLabel(QtWidgets.QLabel):
    mouseLeftButtonClickedSignal = QtCore.Signal()
    mouseRightButtonClickedSignal = QtCore.Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        if(event.button() == QtCore.Qt.MouseButton.LeftButton):
            self.mouseLeftButtonClickedSignal.emit()

        if(event.button() == QtCore.Qt.MouseButton.RightButton):
            self.mouseRightButtonClickedSignal.emit()

        return super().mouseReleaseEvent(event)
        