from random import Random

from PySide6 import QtCore, QtWidgets, QtGui
from PIL.ImageQt import ImageQt

from Model.ImageGenerator import ImageGenerator, PretrainedModelName

from UI.QGeneratedImageLabel import QGeneratedImageLabel

class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.m_maxRandomNumber = 1000000000
        self.randomNumberGenerator = Random()

        #Model
        self.m_imageGenerator = ImageGenerator()

        # Prompt Line & model combo box
        self.m_promptLineEdit = QtWidgets.QLineEdit()
        self.m_promptLineEdit.setPlaceholderText("Example: a photograph of an astronaut riding a horse")
        self.m_modelNameComboBox = QtWidgets.QComboBox()
        for model in list(PretrainedModelName):    
            self.m_modelNameComboBox.addItem(model.value, model)
        self.m_promptLayout = QtWidgets.QHBoxLayout()
        self.m_promptLayout.addWidget(self.m_promptLineEdit)
        self.m_promptLayout.addWidget(self.m_modelNameComboBox)

        # Image Size Widgets
        self.m_imageWidthSpinBox = QtWidgets.QSpinBox()
        self.m_imageWidthSpinBox.setRange(1, 2048)
        self.m_imageWidthSpinBox.setValue(768)
        self.m_imageHeightSpinBox = QtWidgets.QSpinBox()
        self.m_imageHeightSpinBox.setRange(1, 2048)
        self.m_imageHeightSpinBox.setValue(768)

        # Options Widgets
        self.m_numInferenceStepsSpinBox = QtWidgets.QSpinBox()
        self.m_numInferenceStepsSpinBox.setRange(1, 256)
        self.m_numInferenceStepsSpinBox.setValue(50)
        self.m_guidanceScaleDoubleSpinBox = QtWidgets.QDoubleSpinBox()
        self.m_guidanceScaleDoubleSpinBox.setRange(1.0, 10.0)
        self.m_guidanceScaleDoubleSpinBox.setValue(7.5)
        self.m_seedSpinBox = QtWidgets.QSpinBox()
        self.m_seedSpinBox.setRange(0, self.m_maxRandomNumber)
        self.m_seedSpinBox.setValue(self.generateRandomNumber())
        self.m_generateRandomNumberPushButton = QtWidgets.QPushButton("Generate random seed")
        self.m_generateRandomNumberPushButton.clicked.connect(self.onGenerateRandomNumberPushButtonClicked)

        # Options Layouts
        self.m_imageWidthLabel = QtWidgets.QLabel("Width:")
        self.m_imageHeightLabel = QtWidgets.QLabel("Height:")
        self.m_numInferenceStepsLabel = QtWidgets.QLabel("Iteration steps:")
        self.m_guidanceScaleLabel = QtWidgets.QLabel("Guidance scale:")
        self.m_standardOptionsLayout = QtWidgets.QGridLayout()
        self.m_standardOptionsLayout.addWidget(self.m_imageWidthLabel, 0, 0)
        self.m_standardOptionsLayout.addWidget(self.m_imageWidthSpinBox, 0, 1)
        self.m_standardOptionsLayout.addWidget(self.m_imageHeightLabel, 0, 2)
        self.m_standardOptionsLayout.addWidget(self.m_imageHeightSpinBox, 0, 3)
        self.m_standardOptionsLayout.addWidget(self.m_numInferenceStepsLabel, 1, 0)
        self.m_standardOptionsLayout.addWidget(self.m_numInferenceStepsSpinBox, 1, 1)
        self.m_standardOptionsLayout.addWidget(self.m_guidanceScaleLabel, 1, 2)
        self.m_standardOptionsLayout.addWidget(self.m_guidanceScaleDoubleSpinBox, 1, 3)

        self.m_seedOptionsLayout = QtWidgets.QHBoxLayout()
        self.m_seedOptionsLayout.addWidget(self.m_seedSpinBox)
        self.m_seedOptionsLayout.addWidget(self.m_generateRandomNumberPushButton)
        self.m_seedGroupBox = QtWidgets.QGroupBox(" Use custom seed ")
        self.m_seedGroupBox.setCheckable(True)
        self.m_seedGroupBox.setChecked(False)
        self.m_seedGroupBox.setLayout(self.m_seedOptionsLayout)

        # Generate Button
        self.m_generateImagePushButton = QtWidgets.QPushButton("Generate image")
        self.m_generateImagePushButton.clicked.connect(self.onGenerateImagePushButtonClicked)

        # Image Label
        self.m_resultImageLabel = QGeneratedImageLabel()

        # Main Layout
        mainLayout = QtWidgets.QVBoxLayout(self)
        mainLayout.addLayout(self.m_promptLayout)
        mainLayout.addLayout(self.m_standardOptionsLayout)
        mainLayout.addWidget(self.m_seedGroupBox)
        mainLayout.addWidget(self.m_generateImagePushButton)
        mainLayout.addWidget(self.m_resultImageLabel)
        mainLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.setLayout(mainLayout)

    def generateRandomNumber(self):
        return self.randomNumberGenerator.randint(0, self.m_maxRandomNumber)

    @QtCore.Slot()
    def onGenerateRandomNumberPushButtonClicked(self):
        self.m_seedSpinBox.setValue(self.generateRandomNumber())

    @QtCore.Slot()
    def onGenerateImagePushButtonClicked(self):
        promptString = self.m_promptLineEdit.text()
        if promptString:
            width = self.m_imageWidthSpinBox.value()
            height = self.m_imageHeightSpinBox.value()
            numInferenceSteps = self.m_numInferenceStepsSpinBox.value()
            guidanceScale = self.m_guidanceScaleDoubleSpinBox.value()

            seed = self.generateRandomNumber()
            if self.m_seedGroupBox.isChecked():
                seed = self.m_seedSpinBox.value()
            else:
                self.m_seedSpinBox.setValue(seed)

            self.m_resultImageLabel.loadWaitingImage(width, height)
            self.repaint()
            QtWidgets.QApplication.processEvents()

            model = self.m_modelNameComboBox.currentData()
            image = self.m_imageGenerator.generateImage(modelName=model, prompt=promptString, width=width, height=height, numInferenceSteps=numInferenceSteps, guidanceScale=guidanceScale, seed=seed)
            imageQt = ImageQt(image)
            self.m_resultImageLabel.setPixmap(QtGui.QPixmap.fromImage(imageQt))
        