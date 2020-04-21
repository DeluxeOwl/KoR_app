#!/usr/bin/python3


import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton


def main():
    """Simple Hello World example with PyQt5."""

    # 1. Import `QApplication` and all the required widgets
    # 2. Create an instance of QApplication
    app = QApplication(sys.argv)

    # 3. Create an instance of your application's GUI
    window = QWidget()
    window.setWindowTitle('PyQt5 App')
    window.setGeometry(450, 450, 300, 300)
    window.move(60, 15)

    hello_msg = QLabel('<h1>Hello World!</h1>', parent=window)
    hello_msg.move(60, 15)

    register_button = QPushButton('Register', parent=window)

    # 4. Show your application's GUI
    window.show()

    # 5. Run your application's event loop (or main loop)
    sys.exit(app.exec_())


if __name__ == "__main__":
    # execute only if run as a script
    main()
