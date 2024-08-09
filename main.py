import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt, QTime, QTimer


def format_time(time):
    hours = time.hour()
    minutes = time.minute()
    seconds = time.second()
    milliseconds = time.msec() // 10
    return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel('00:00:00.00', self)
        self.start_button = QPushButton('Start', self)
        self.stop_button = QPushButton('Stop', self)
        self.reset_button = QPushButton('Reset', self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("STOPWATCH")

        vbox = QVBoxLayout()

        vbox.addWidget(self.time_label)

        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()

        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.start_button.setObjectName('start_button')
        self.stop_button.setObjectName('stop_button')
        self.reset_button.setObjectName('reset_button')

        self.setStyleSheet("""
            QPushButton, QLabel{
                padding: 20px;
                font-weight: bold;
                font-family: calibri;
            }

            QPushButton{
                font-size: 50px;
                border-radius: 15px;
            }
            QPushButton#start_button{
                background-color: hsl(128, 97%, 62%);
            }
            QPushButton#stop_button{
                background-color: hsl(11, 97%, 62%);
            }
            QPushButton#reset_button{
                background-color: hsl(63, 97%, 62%);
            }
            QPushButton#start_button:hover{
                background-color: hsl(128, 97%, 82%);
            }
            QPushButton#stop_button:hover{
                background-color: hsl(11, 97%, 82%);
            }
            QPushButton#reset_button:hover{
                background-color: hsl(63, 97%, 82%);
            }
            QLabel{
                font-size: 120px;
                background-color: hsl(200, 100%, 85%);
                border-radius: 20px;
            }
        """)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(format_time(self.time))

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(format_time(self.time))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())
