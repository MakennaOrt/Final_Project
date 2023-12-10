from PyQt5.QtWidgets import QApplication
from Order_system import OrderSystemApp

def main():
    app = QApplication([])
    window = OrderSystemApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
