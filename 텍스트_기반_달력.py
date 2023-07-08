import sys
from PyQt5.QtWidgets import*
from PyQt5 import QtGui
from PyQt5 import uic

form_class = uic.loadUiType("main_Window.xml")[0]
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
# 윤년인지 아닌지 확인하는 함수
def leapyear(y):
    if((y % 4 == 0 and y% 100 !=0)or y % 400 ==0):
        return True
    else:
        return False
# 구하고자하는 달이 총 며칠인지 구하는 함수
def WhatMonthy(y,m):
    numOfDays = 31
    if(m in [4,6,9,11]):
        numOfDays = 30
    if (m==2):
        if(leapyear(y)):
            numOfDays = 29
        else:
            numOfDays = 28
    return numOfDays
numOfmonth = WhatMonthy(year,month)
#구하고자하는 일이 몇요일인지 구하는 함수
def WhatWeek(y, m ,d):
    # 전 년도 구하기 함수
    t1 = y - (14 - m) // 12
    # 전 년도 포함 전 년도까지의 날짜 구하기(윤년 포함)
    t2 = t1 +(t1//4) -(t1 // 100)+ (t1//400) 
    t3= m + 12*((14-m)//12)-2
    return(d+t2+(31*t3//12))%7
# def week():
#     weekk = ''
#     for day in weekdays:
#         str_n =(' ' + day + ' ')
#         weekk += str_n
#     return weekk
def day(y,m):
    dayy = ' '
    numOfmonth = WhatMonthy(y,m)
    what_week = WhatWeek(y,m,1)

    for i in range(what_week):
        dayy  += '         '
    for day in range(1, numOfmonth +1):
        if(day<10):
            str_d = ('   0' + str(day) + '   ')
            dayy += str_d
        else:
            dayy += ('   '+str(day)+'   ')
        if ((what_week+day)%7 == 0):
            dayy += ('\n')
    return dayy

class DemoForm(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def done(self):
        new_year = int(self.lineEdit.text())
        new_month = int(self.lineEdit_2.text())
        leapyear(new_year)
        WhatMonthy(new_year,new_month)
        day(new_year,new_month)
        self.label.setText(str(new_year)+'년 '+str(new_month)+'월')
        self.label.setFont(QtGui.QFont("굴림",20))
        self.label_7.setText(갑자(new_year))
        self.label_7.setFont(QtGui.QFont("궁서",15))
        self.label_8.setText(갑자_anymal(new_year))
        self.label_8.setFont(QtGui.QFont("궁서",15))
        self.label_2.setText('일')
        self.label_9.setText('월')
        self.label_10.setText('화')
        self.label_11.setText('수')
        self.label_12.setText('목')
        self.label_13.setText('금')
        self.label_14.setText('토')
        self.label_9.setFont(QtGui.QFont("궁서",15))
        self.label_10.setFont(QtGui.QFont("궁서",15))
        self.label_11.setFont(QtGui.QFont("궁서",15))
        self.label_12.setFont(QtGui.QFont("궁서",15))
        self.label_13.setFont(QtGui.QFont("궁서",15))
        self.label_14.setFont(QtGui.QFont("궁서",15))
        self.label_2.setFont(QtGui.QFont("궁서",15))
        self.label_2.setStyleSheet("Color : red")
        self.label_14.setStyleSheet("Color : blue")
        self.label_3.setText(day(new_year,new_month))
        self.label_3.setFont(QtGui.QFont("궁서",15))
 
if __name__ == "__main__" :

    app = QApplication(sys.argv) 

    demoWindow = DemoForm() 

    demoWindow.show()

    app.exec_()