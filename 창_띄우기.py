# 필요한 모듈 불러오기
import sys
from PyQt5.QtWidgets import QApplication,QWidget


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 창 제목 설정
        self.setWindowTitle('My First Application')
        # 위젯을 스크린의 x=300px, y=200의 위치로 이동시킵니다.
        self.move(300,300)
        # 위젯의 크기를 너비 400px,높이200px로 조절합니다.
        self.resize(400,200)
        # 위젯을 스크린에 보여준다
        self.show()

# '__name__'은 현재 모듈의 이름이 저장되는 내장 변수입니다.
if __name__ == '__main__':
    #모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야 합니다.
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())