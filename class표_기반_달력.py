import sys
from PyQt5.QtWidgets import*
from PyQt5 import QtGui, QtWidgets
from PyQt5 import uic

form_class = uic.loadUiType("main_window2.xml")[0]
weekdays = ['일','월','화','수','목','금','토']
간 = ['경','신','임','계','갑','을','병','정','무','기']
간자 = ["庚","辛","壬","癸","甲","乙","丙","丁","戊","己"]
간_색 = ['흰','흰','검은','검은','푸른','푸른','붉은','붉은','황금','황금']
간지 = ['신','유','술','해','자','축','인','묘','진','사','오','미']
간지_자 =["申","酉","戌","亥","子","丑","寅","卯","辰","巳","午","未"]
간지_동물 = ['원숭이','닭','개','돼지','쥐','소','호랑이','토끼','용','뱀','말','양']
year = 1
month= 1
class calander:
    def __init__(self,year_1,month_1):
        self.year_1 = year_1
        self.month_1 = month_1
    def 갑자(self):
        갑자 = str(간[int(str(self.year_1)[-1])]+간지[self.year_1%12])+'년'
        간_자 = str(간자[int(str(self.year_1)[-1])]+간지_자[self.year_1%12])+'年'
        return 갑자 +'  '+ 간_자
    def 갑자_anymal(self):
        갑자_anymal = str(간_색[int(str(self.year_1)[-1])]+간지_동물[self.year_1%12])
        return 갑자_anymal
    def leapyear(self):
        if((self.year_1 % 4 == 0 and self.year_1% 100 !=0)or self.year_1 % 400 ==0):
            return True
        else:
            return False
    def WhatMonthy(self):
        numOfDays = 31
        if(self.month_1 in [4,6,9,11]):
            numOfDays = 30
        if (self.month_1==2):
            if(self.leapyear()):
                numOfDays = 29
            else:
                numOfDays = 28
        return numOfDays
    def WhatWeek(self,d):
        self.d =d
        # 전 년도 구하기 함수
        t1 = self.year_1 - (14 - self.month_1) // 12
        # 전 년도 포함 전 년도까지의 날짜 구하기(윤년 포함)
        t2 = t1 +(t1//4) -(t1 // 100)+ (t1//400) 
        t3= self.month_1 + 12*((14-self.month_1)//12)-2
        return(d+t2+(31*t3//12))%7

class DemoForm(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def send(self):
        new_year = int(self.lineEdit.text())
        new_month = int(self.lineEdit_2.text())
        달력 = calander(new_year,new_month)
        self.label.setText(달력.갑자())
        self.label.setFont(QtGui.QFont("궁서",15))
        self.label_2.setText(달력.갑자_anymal())
        self.label_2.setFont(QtGui.QFont("궁서",15))
        달력.leapyear()
        달력.WhatMonthy()
        table = QtWidgets.QTableWidget(self)
        table.resize(900,270)
        table.move(10,250)
        # 표의 크기를 지정
        table.setColumnCount(7)
        table.setRowCount(6)
        # 열 제목 지정
        table.setHorizontalHeaderLabels(
            ['일','월','화','수','목','금','토']
        )
        numOfmonth = 달력.WhatMonthy()
        what_week = 달력.WhatWeek(1)
        i=0
        while i < numOfmonth:
            table.setItem(0,what_week+i,QtWidgets.QTableWidgetItem(str(i+1)))
            i += 1
        # table.setStyleSheet(0,0,QtWidgets,"Color : red")
        # table.setStyleSheet(0,6,QtWidgets,"Color : red")
        table.setFont(QtGui.QFont("궁서",13))
        table.show()
if __name__ == "__main__" :

    app = QApplication(sys.argv) 

    demoWindow = DemoForm() 

    demoWindow.show()

    app.exec_()