import sys
from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow
from CustomTextEdit import CustomTextEdit

def main():
    app = QApplication(sys.argv)
    editor = CustomTextEdit()
    window = MainWindow(editor)
    window.resize(800, 600)
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()