from PySide6 import QtCore, QtWidgets, QtGui
from PIL.ImageQt import ImageQt

from Model.ImageGenerator import ImageGenerator

from UI.QGeneratedImageLabel import QGeneratedImageLabel

class MainWindow(QtWidgets.QWidget):
    def __init__(self, accessToken:str, parent=None):
        super().__init__(parent)

        #Model
        print("Loading Image Generator in your GPU, please wait...")
        self.m_imageGenerator = ImageGenerator(accessToken)

        # UI
        self.m_promptLineEdit = QtWidgets.QLineEdit()
        self.m_promptLineEdit.setPlaceholderText("Example: a photograph of an astronaut riding a horse")
        self.m_imageWidthSpinBox = QtWidgets.QSpinBox()
        self.m_imageWidthSpinBox.setRange(1, 2048)
        self.m_imageWidthSpinBox.setValue(512)
        self.m_imageHeightSpinBox = QtWidgets.QSpinBox()
        self.m_imageHeightSpinBox.setRange(1, 2048)
        self.m_imageHeightSpinBox.setValue(512)
        self.m_numInferenceStepsSpinBox = QtWidgets.QSpinBox()
        self.m_numInferenceStepsSpinBox.setRange(1, 256)
        self.m_numInferenceStepsSpinBox.setValue(50)
        self.m_guidanceScaleDoubleSpinBox = QtWidgets.QDoubleSpinBox()
        self.m_guidanceScaleDoubleSpinBox.setRange(1.0, 10.0)
        self.m_guidanceScaleDoubleSpinBox.setValue(7.5)
        self.m_generateImageButton = QtWidgets.QPushButton("Generate Image")
        self.m_resultImageLabel = QGeneratedImageLabel()

        self.m_settingsLayout = QtWidgets.QFormLayout()
        self.m_settingsLayout.addRow("Width:", self.m_imageWidthSpinBox)
        self.m_settingsLayout.addRow("Height:", self.m_imageHeightSpinBox)
        self.m_settingsLayout.addRow("Iteration steps:", self.m_numInferenceStepsSpinBox)
        self.m_settingsLayout.addRow("Guidance scale:", self.m_guidanceScaleDoubleSpinBox)

        self.m_mainLayout = QtWidgets.QVBoxLayout(self)
        self.m_mainLayout.addWidget(self.m_promptLineEdit)
        self.m_mainLayout.addLayout(self.m_settingsLayout)
        self.m_mainLayout.addWidget(self.m_generateImageButton)
        self.m_mainLayout.addWidget(self.m_resultImageLabel)
        self.setLayout(self.m_mainLayout)

        self.m_generateImageButton.clicked.connect(self.onGenerateImageButtonClicked)

    @QtCore.Slot()
    def onGenerateImageButtonClicked(self):
        promptString = self.m_promptLineEdit.text()
        if promptString:
            self.m_resultImageLabel.loadWaitingImage()
            self.repaint()

            width = self.m_imageWidthSpinBox.value()
            height = self.m_imageHeightSpinBox.value()
            numInferenceSteps = self.m_numInferenceStepsSpinBox.value()
            guidanceScale = self.m_guidanceScaleDoubleSpinBox.value()
            image = self.m_imageGenerator.generateImage(promptString, width, height, numInferenceSteps, guidanceScale)
            imageQt = ImageQt(image)
            self.m_resultImageLabel.setPixmap(QtGui.QPixmap.fromImage(imageQt))
        