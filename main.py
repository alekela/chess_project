from window import Field
from PyQt5.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
board = Field()
board.show()
sys.exit(app.exec())
