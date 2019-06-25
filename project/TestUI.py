from PySide2 import QtWidgets
import main, for_GUI as fg

class MyApp(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.analyze)

    def analyze(self):
        self.textEdit.setPlainText(fg.stream_tweets("python", "textt.csv"))


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyApp()
    qt_app.show()
    app.exec_()
