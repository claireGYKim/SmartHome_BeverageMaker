import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import RPi.GPIO as gpio
import time

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("maker.ui")[0]
gpio.setmode(gpio.BCM)
firsttime = 0
secondtime = 0
thirdtime = 0
fourthtime = 0
gpio.setup(17, gpio.OUT)
gpio.setup(18, gpio.OUT)
gpio.setup(22, gpio.OUT)
gpio.setup(23, gpio.OUT)

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.make.clicked.connect(self.makeFunction)
        self.spinBox_1.valueChanged.connect(self.setfirsttime)
        self.spinBox_2.valueChanged.connect(self.setsecondtime)
        self.spinBox_3.valueChanged.connect(self.setthirdtime)
        self.spinBox_4.valueChanged.connect(self.setfourthtime)

    def setfirsttime(self) :
        global firsttime
        firsttime = self.spinBox_1.value()
        print(firsttime)
    def setsecondtime(self) :
        global secondtime
        secondtime = self.spinBox_2.value()
        print(secondtime)
    def setthirdtime(self) :
        global thirdtime
        thirdtime = self.spinBox_3.value()
        print(thirdtime)
    def setfourthtime(self) :
        global fourthtime
        fourthtime = self.spinBox_4.value()
        print(fourthtime)
    
    def makeFunction(self) :
        if firsttime!=0 :
            gpio.output(17, gpio.HIGH)
            time.sleep(firsttime)
            gpio.output(17, gpio.LOW)
        if secondtime!=0 :
            gpio.output(18, gpio.HIGH)
            time.sleep(secondtime)
            gpio.output(18, gpio.LOW)
        if thirdtime!=0 :
            gpio.output(22, gpio.HIGH)
            time.sleep(thirdtime)
            gpio.output(22, gpio.LOW)
        if fourthtime!=0 :
            gpio.output(23, gpio.HIGH)
            time.sleep(fourthtime)
            gpio.output(23, gpio.LOW)
        print("make Clicked")


if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()