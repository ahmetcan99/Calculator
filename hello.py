import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QMainWindow, QPushButton
from random import choice

window_titles = [    
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0
        
        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.ButtonWasClicked)

        self.windowTitleChanged.connect(self.WindowTitleChanged)

        self.setCentralWidget(self.button)

    def ButtonWasClicked(self):
        print("Clicked!")
        new_window_title = choice(window_titles)
        print("Setting Title: %s" % new_window_title)
        self.setWindowTitle(new_window_title)

    def WindowTitleChanged(self, window_title):
        print("Window title has changed: %s" % window_title)

        if window_title == 'Something went wrong':
            self.button.setDisabled(True)

app = QApplication([])

window = MainWindow()
window.show()

sys.exit(app.exec())