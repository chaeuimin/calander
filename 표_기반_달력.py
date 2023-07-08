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
def 갑자(year):
    갑자 = str(간[int(str(year)[-1])]+간지[year%12])+'년'
    간_자 = str(간자[int(str(year)[-1])]+간지_자[year%12])+'年'
    return 갑자 +'  '+ 간_자
def 갑자_anymal(year):
    갑자_anymal = str(간_색[int(str(year)[-1])]+간지_동물[year%12])
    return 갑자_anymal
def leapyear(y):
    if((y % 4 == 0 and y% 100 !=0)or y % 400 ==0):
        return True
    else:
        return False
def WhatMonthy(y,m):
    numOfDays = 31
    if(m in [4,6,9,11]):
        numOfDays = 30
    if (m==2):
        if(leapyear(year)):
            numOfDays = 29
        else:
            numOfDays = 28
    return numOfDays
def WhatWeek(y, m ,d):
    # 전 년도 구하기 함수
    t1 = y - (14 - m) // 12
    # 전 년도 포함 전 년도까지의 날짜 구하기(윤년 포함)
    t2 = t1 +(t1//4) -(t1 // 100)+ (t1//400) 
    t3= m + 12*((14-m)//12)-2
    return(d+t2+(31*t3//12))%7
def day(y,m):
    dayy = ' '

class DemoForm(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def send(self):
        new_year = int(self.lineEdit.text())
        new_month = int(self.lineEdit_2.text())
        self.label.setText(갑자(new_year))
        self.label.setFont(QtGui.QFont("궁서",15))
        self.label_2.setText(갑자_anymal(new_year))
        self.label_2.setFont(QtGui.QFont("궁서",15))
        leapyear(new_year)
        WhatMonthy(new_year,new_month)
        day(new_year,new_month)
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
        numOfmonth = WhatMonthy(new_year,new_month)
        what_week = WhatWeek(new_year,new_month,1)
        i=0
        while i < numOfmonth:
            table.setItem(0,what_week+i,QtWidgets.QTableWidgetItem(str(i+1)))
            i += 1
        table.setFont(QtGui.QFont("궁서",13))
        table.show()
if __name__ == "__main__" :

    app = QApplication(sys.argv) 

    demoWindow = DemoForm() 

    demoWindow.show()

    app.exec_()