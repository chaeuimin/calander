from email.mime import application
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon\



class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        
        exitAction =QAction(QIcon('exit.png'),'Exit',self)
        #주석 달기
        exitAction.setShortcut('Ctrl+Q')
        # 상태바에 나타날 상태팁 설정
        exitAction.setStatusTip('Exit application')
        # 이 동작을 선택했을때 생선된(triggered) 시그널이 QApplication위젯의 quit()메서드에 연결되고, 어플리케이션을 종료시키게됩니다.
        exitAction.triggered.connect(qApp.quit)
       
        self.statusBar()
        # 메뉴바 생성
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        # 단축키 설정
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        self.setWindowTitle('Menubar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())