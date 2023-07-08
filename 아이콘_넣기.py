# 필요한 모듈 불러오기
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 창 제목 설정
        self.setWindowTitle('icon')
        # 아이콘 설정__Qicon이 필요
        self.setWindowIcon(QIcon('디지몬_아구몬.png'))
        # 앞의 두 매개변수는 창의 x, y 위치를 결정하고, 뒤의 두 매개변수는 각각 창의 너비와 높이를 결정합니다.
        self.setGeometry(400,200,300,200)
        # 위젯을 스크린에 보여준다
        self.show()

# '__name__'은 현재 모듈의 이름이 저장되는 내장 변수입니다.
if __name__ == '__main__':
    #모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야 합니다.
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())