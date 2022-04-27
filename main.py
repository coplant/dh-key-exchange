from random import randrange, getrandbits, randint

from PySide6.QtWidgets import *
from ui_mainwindow import Ui_MainWindow


class Primes:
    @staticmethod
    def is_prime(n, k=128):
        if n == 2 or n == 3:
            return True
        if n <= 1 or n % 2 == 0:
            return False
        s = 0
        r = n - 1
        while r & 1 == 0:
            s += 1
            r //= 2
        for _ in range(k):
            a = randrange(2, n - 1)
            x = pow(a, r, n)
            if x != 1 and x != n - 1:
                j = 1
                while j < s and x != n - 1:
                    x = pow(x, 2, n)
                    if x == 1:
                        return False
                    j += 1
                if x != n - 1:
                    return False
        return True

    @staticmethod
    def __get_number(length):
        p = getrandbits(length)
        p |= (1 << length - 1) | 1
        return p

    @staticmethod
    def get_prime(length=1024):
        p = 4
        while not Primes.is_prime(p, 128):
            p = Primes.__get_number(length)
        return p


class GUI(QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.btn_generate.clicked.connect(self.generate)
        self.ui.btn_clear.clicked.connect(lambda: self.clear("FULL"))
        self.ui.btn_calc.clicked.connect(self.calc)
        self.P = None
        self.A = None
        self.Q = None

    def generate(self):
        if self.ui.line_P.text():
            if not Primes.is_prime(int(self.ui.line_P.text())):
                QMessageBox.information(self, "Error", "A's P is not Prime!", QMessageBox.Ok)
                return
        else:
            self.clear()
            while not Primes.is_prime(int(self.P or 0)):
                self.Q = Primes.get_prime(length=256)
                self.P = 2 * self.Q + 1
            self.ui.line_P.setText(str(self.P))
            self.A = randint(2, self.P - 2)
            while not pow(self.A, self.Q, self.P) != 1:
                self.A = randint(2, self.P - 2)
            self.ui.line_A.setText(str(self.A))

    def clear(self, *args):
        self.P = None
        self.A = None
        self.Q = None
        if args:
            self.ui.line_P.clear()
            self.ui.line_A.clear()
            self.ui.a_line_X.clear()
            self.ui.a_line_Y1.clear()
            self.ui.a_line_Y2.clear()
            self.ui.a_line_Z.clear()
            self.ui.b_line_X.clear()
            self.ui.b_line_Y1.clear()
            self.ui.b_line_Y2.clear()
            self.ui.b_line_Z.clear()

    def calc(self):
        if self.ui.line_P.text() and self.ui.a_line_X.text() and self.ui.b_line_X.text():
            try:
                P = int(self.ui.line_P.text())
                A = int(self.ui.line_A.text())
            except:
                QMessageBox.information(self, "Error", "Is not a number!", QMessageBox.Ok)
                return
            if self.swap(P, A, option=0) and self.swap(P, A, option=1):
                self.ui.a_line_Y2.setText(self.ui.b_line_Y2.text())
                self.ui.b_line_Y1.setText(self.ui.a_line_Y1.text())
                self.ui.a_line_Z.setText(str(pow(int(self.ui.a_line_Y2.text()), int(self.ui.a_line_X.text()), P)))
                self.ui.b_line_Z.setText(str(pow(int(self.ui.b_line_Y1.text()), int(self.ui.b_line_X.text()), P)))
        else:
            QMessageBox.information(self, "Error", "Empty fields found!", QMessageBox.Ok)
            return

    def validator(self, option, p):
        try:
            x = int(self.ui.a_line_X.text() if not option else self.ui.b_line_X.text())
        except:
            QMessageBox.information(self, "Error", "Is not a number!", QMessageBox.Ok)
            return False
        if x < p:
            return x
        else:
            QMessageBox.information(self, "Error", "X must be lower than P!", QMessageBox.Ok)
            return

    def swap(self, p, a, option):
        x = self.validator(option, p)
        if x:
            y = pow(a, x, p)
            self.ui.a_line_Y1.setText(str(y)) if not option else self.ui.b_line_Y2.setText(str(y))
            return True


def main():
    app = QApplication()
    window = GUI()
    app.exec()


if __name__ == '__main__':
    main()
