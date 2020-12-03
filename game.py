from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QLabel, QHBoxLayout, QMessageBox

import re

from updown import Updown
from numtry import Numtry
from number import Number


class UpdownGame(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.number = Number()
        self.startInput = 0
        self.endInput = 999

        # Display widget for recording number with Up and Down
        self.recordWindow = QTextEdit()
        self.recordWindow.setReadOnly(True)
        self.recordWindow.setAlignment(Qt.AlignLeft)
        self.recordWindow.setPlaceholderText('*** Up & Down Record ***')

        recordLayout = QGridLayout()
        recordLayout.addWidget(self.recordWindow, 0, 0)

        showLayout = QGridLayout()

        # Display widget for remaining opportunity
        self.opportunityWindow = QLineEdit()
        self.opportunityWindow.setReadOnly(True)
        self.opportunityWindow.setAlignment(Qt.AlignCenter)
        self.opportunityWindow.setFixedSize(180, 25)
        showLayout.addWidget(self.opportunityWindow, 0, 0)

        # Display widget for status
        self.updownWindow = QTextEdit()
        self.updownWindow.setReadOnly(True)
        self.updownWindow.setAlignment(Qt.AlignCenter)
        self.updownWindow.setFixedSize(180, 180)
        showLayout.addWidget(self.updownWindow, 1, 0)

        # Display widget for message output
        self.message = QLineEdit()
        self.message.setReadOnly(True)
        self.message.setAlignment(Qt.AlignRight)
        showLayout.addWidget(self.message, 2, 0)

        rangeLayout = QHBoxLayout()

        # Input widget for setting range, start number
        self.startRangeInput = QLineEdit()
        self.startRangeInput.setPlaceholderText("Start Number (default : 0)")
        rangeLayout.addWidget(self.startRangeInput, 4)

        # Display widget '~'
        self.rangeLabel = QLabel()
        self.rangeLabel.setText("~")
        self.rangeLabel.setAlignment(Qt.AlignCenter)
        rangeLayout.addWidget(self.rangeLabel, 1)

        # Input widget for setting range, end number
        self.endRangeInput = QLineEdit()
        self.endRangeInput.setPlaceholderText("End Number (default : 999)")
        rangeLayout.addWidget(self.endRangeInput, 4)

        # Button for setting random number's range
        self.setButton = QToolButton()
        self.setButton.setText("set")
        self.setButton.clicked.connect(self.setClicked)
        rangeLayout.addWidget(self.setButton, 3)

        inputLayout = QGridLayout()

        # Display widget 'Input Number : '
        self.numLabel = QLabel()
        self.numLabel.setText("Input Number : ")
        inputLayout.addWidget(self.numLabel, 0, 0)

        # Input widget for user selected number
        self.tryNumber = QLineEdit()
        self.tryNumber.setMaxLength(3)
        self.tryNumber.setAlignment(Qt.AlignRight)
        inputLayout.addWidget(self.tryNumber, 0, 1)

        # Button for submitting a number
        self.tryButton = QToolButton()
        self.tryButton.setText('Give it a try')
        self.tryButton.clicked.connect(self.tryClicked)
        inputLayout.addWidget(self.tryButton, 0, 2)

        # Button for a new game
        self.newGameButton = QToolButton()
        self.newGameButton.setText('New Game')
        self.newGameButton.clicked.connect(self.newClicked)
        inputLayout.addWidget(self.newGameButton, 1, 2)

        # Layout placement
        adminLayout = QGridLayout()
        adminLayout.addLayout(recordLayout, 0, 0)
        adminLayout.addLayout(showLayout, 0, 1)
        adminLayout.setContentsMargins(20, 20, 20, 5)

        userLayout = QGridLayout()
        userLayout.addLayout(rangeLayout, 0, 0)
        userLayout.addLayout(inputLayout, 1, 0)
        userLayout.setContentsMargins(20, 0, 20, 0)

        mainLayout = QGridLayout()
        mainLayout.addLayout(adminLayout, 0, 0)
        mainLayout.addLayout(userLayout, 1, 0)

        self.setLayout(mainLayout)

        self.setWindowTitle('Up & Down Game')

        # Start a new game on application launch!
        self.startGame()

    def startGame(self):
        self.updown = Updown()
        self.numtry = Numtry(self.number.randomNum)
        self.gameOver = False
        self.opportunityWindow.setText(self.updown.currentOpportunity())
        self.message.clear()

    def newClicked(self):
        self.updown = Updown()
        self.numtry = Numtry(self.number.randomNumber())
        self.gameOver = False
        self.opportunityWindow.setText(self.updown.currentOpportunity())
        self.recordWindow.clear()
        self.updownWindow.clear()
        self.startRangeInput.clear()
        self.endRangeInput.clear()
        self.message.clear()

    def setClicked(self):
        p = re.compile(r'\b[0-9]+\b')
        if(p.match(self.startRangeInput.text())!=None and p.match(self.endRangeInput.text())!=None):
            self.updown = Updown()
            self.startInput = int(self.startRangeInput.text())
            self.endInput = int(self.endRangeInput.text())

            self.numtry = Numtry(self.number.rangeNumber(self.startInput, self.endInput))
            self.gameOver = False
            self.opportunityWindow.setText(self.updown.currentOpportunity())
            self.recordWindow.clear()
            self.updownWindow.clear()
            self.message.clear()

            # Case : User input wrong range, start number > end number
            if self.startInput > self.endInput:
                self.message.setText("Input right range.")
                return
        else:
            QMessageBox.about(self, 'NOTICE', 'Range value must be NUMBER.')
            self.startRangeInput.clear()
            self.endRangeInput.clear()

    def tryClicked(self):
        p = re.compile(r'\b[0-9]+\b')
        tryNum = self.tryNumber.text()
        self.tryNumber.clear()
        self.message.clear()
        if(p.match(tryNum)!=None):
            if int(tryNum) in range(self.startInput, self.endInput+1):
                if self.gameOver == True:
                    self.message.setText("Game Over!")
                    return

                if len(tryNum) > 3 or len(tryNum) < 1:
                    self.message.setText("Put number 0 to 999.")
                    return

                if int(tryNum) in self.numtry.recordNums:
                    self.message.setText("You already have it.")
                    return

                if int(tryNum) not in self.numtry.recordNums:
                    self.message.setText("Keep Going.")

                case = self.numtry.numtry(int(tryNum))

                # Case : input number < secret number
                if case == 0:
                    self.updown.decreaseOpportunity()
                    self.message.setText("Up!")
                    self.numtry.updownTry(tryNum + " : Up" + "\n")
                    self.recordWindow.setText(self.numtry.getRecordUpdown())
                    self.updownWindow.setText(self.updown.getUpDisplay())
                    self.opportunityWindow.setText(self.updown.currentOpportunity())

                # Case : input number > secret number
                if case == 1:
                    self.updown.decreaseOpportunity()
                    self.message.setText("Down!")
                    self.numtry.updownTry(tryNum + " : Down" + "\n")
                    self.recordWindow.setText(self.numtry.getRecordUpdown())
                    self.updownWindow.setText(self.updown.getDownDisplay())
                    self.opportunityWindow.setText(self.updown.currentOpportunity())

                # Case for success, input number == secret number
                if self.numtry.finished():
                    self.message.setText("Success! Answer is " + str(self.numtry.secretNumber) + ".")
                    self.gameOver = True
                    self.updownWindow.setText(self.updown.getSuccessDisplay())

                # Case for game over, No opportunity
                elif self.updown.getOpportunity() == 0:
                    self.message.setText("Fail! Answer was " + str(self.numtry.secretNumber) + ".")
                    self.gameOver = True
                    self.updownWindow.setText(self.updown.getGameoverDisplay())
            else:
                QMessageBox.about(self, 'NOTICE', 'Please check the RANGE you set.')

        else:
            QMessageBox.about(self, 'NOTICE', 'Please input only NUMBER.')


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    game = UpdownGame()
    game.show()
    sys.exit(app.exec_())
