from PyQt5.Qt import *
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ui练习")
        self.resize(500,500)
        self.setUpUi()
    def setUpUi(self):
        print(123)
if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())