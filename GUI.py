import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget,QPushButton

class HelloWindow(QMainWindow):  # Inherits from / is a Main Window
    def __init__(self):
        QMainWindow.__init__(self)  

        centralWidget = QWidget(self)  # create central widget
        self.setCentralWidget(centralWidget)   # assign it to main window

        vLayout = QVBoxLayout(self)  # Layout   
        centralWidget.setLayout(vLayout)  # add layout to central widget

        title = QLabel("Is there any Pearson correlation?\n"
                       "red means no\n"
                       "Green means yes\n"
                       "press button to change the state", self)  # make text label
        vLayout.addWidget(title)  # add text label to layout

        self.setGeometry(800, 800, 1600, 400)



        # creating a push button
        self.button = QPushButton("No Correlation", self)

        # setting geometry of button
        self.button.setGeometry(200, 50, 1200, 300)

        # setting checkable to true
        self.button.setCheckable(True)

        # setting calling method by button
        self.button.clicked.connect(self.changeColor)

        # setting default color of button to red
        self.button.setStyleSheet("background-color : red")

        self.slider = QtWidgets.QSlider(self)
        self.slider.setGeometry(QtCore.QRect(190, 100, 160, 16))
        self.slider.setOrientation(QtCore.Qt.Horizontal)

        # After each value change, slot "scaletext" will get invoked.
        self.slider.valueChanged.connect(self.scaletext)



    def changeColor(self):

            # if button is checked
            if self.button.isChecked():

                # setting background color to green
                self.button.setStyleSheet("background-color : green")
                self.button.setText("Correlation")
            # if it is unchecked
            else:

                # set background color back to Red
                self.button.setStyleSheet("background-color : red")
                self.button.setText("No Correlation")


    def scaletext(self, value):
        # Change font size of label. Size value could
        # be anything consistent with the dimension of label.
        self.font.setPointSize(7 + value // 2)
        self.label.setFont(self.font)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # start app
    mainWin = HelloWindow()  # create main window
    mainWin.show()  # show it
    sys.exit( app.exec_() )  # close app when main window closed