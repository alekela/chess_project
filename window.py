from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from figures import *

WHITE = 0
BLACK = 1


class Field(QWidget):
    def __init__(self):
        super().__init__()

        self.cell_size = 50
        self.board = QLabel(self)
        self.board.resize(self.cell_size * 8, self.cell_size * 8)
        self.board.move(self.cell_size, self.cell_size)
        self.board.setPixmap(QPixmap('board.png'))
        self.setFixedSize(50 * 10, 50 * 10)
        self.setWindowTitle('Шахматы')

        self.result = QLabel(self)
        self.result.resize(300, 30)
        self.result.move(100, 460)
        self.result.setText('')

        self.initpicture()
        self.initfield()

        self.start_btn = QPushButton('Начать новую игру', self)
        self.start_btn.resize(200, 30)
        self.start_btn.move(150, 10)
        self.start_btn.clicked.connect(self.startgame)

    def startgame(self):
        self.initfield()
        self.result.setText('')

    def initfield(self):
        self.end = False
        self.color = WHITE
        self.field = [[None for _ in range(8)] for _ in range(8)]
        for i in range(8):
            self.field[1][i] = Pawn(1, i, WHITE, 'pictures/pawnw.png')
            self.field[6][i] = Pawn(6, i, BLACK, 'pictures/pawnb.png')
        self.field[0][0] = Rook(0, 0, WHITE, 'pictures/rookw.png')
        self.field[0][1] = Knight(0, 1, WHITE, 'pictures/knightw.png')
        self.field[0][2] = Bishop(0, 2, WHITE, 'pictures/bishopw.png')
        self.field[0][3] = King(0, 3, WHITE, 'pictures/kingw.png')
        self.field[0][4] = Queen(0, 4, WHITE, 'pictures/queenw.png')
        self.field[0][5] = Bishop(0, 5, WHITE, 'pictures/bishopw.png')
        self.field[0][6] = Knight(0, 6, WHITE, 'pictures/knightw.png')
        self.field[0][7] = Rook(0, 7, WHITE, 'pictures/rookw.png')
        self.field[7][0] = Rook(7, 0, BLACK, 'pictures/rookb.png')
        self.field[7][1] = Knight(7, 1, BLACK, 'pictures/knightb.png')
        self.field[7][2] = Bishop(7, 2, BLACK, 'pictures/bishopb.png')
        self.field[7][3] = King(7, 3, BLACK, 'pictures/kingb.png')
        self.field[7][4] = Queen(7, 4, BLACK, 'pictures/queenb.png')
        self.field[7][5] = Bishop(7, 5, BLACK, 'pictures/bishopb.png')
        self.field[7][6] = Knight(7, 6, BLACK, 'pictures/knightb.png')
        self.field[7][7] = Rook(7, 7, BLACK, 'pictures/rookb.png')

        self.draw_field()

    def place_figure(self, row, col, figure):
        if not self.field[row][col]:
            self.field[row][col] = figure
            return True
        else:
            return False

    def current_player_color(self):
        return self.color

    def change_player(self):
        self.color = BLACK if self.color == WHITE else WHITE

    def move_figure(self, old, new):
        piece = self.field[old[0]][old[1]]
        self.field[old[0]][old[1]] = None  # Снять фигуру.
        self.field[new[0]][new[1]] = piece  # Поставить на новое место.
        piece.set_position(*new)

    def is_under_attack(self, pos, color):
        for line in self.field:
            for fig in line:
                if fig and fig.get_color() != color:
                    if pos in fig.possible_moves(self.field):
                        return True
        return False

    def check_mat(self, figure):
        for move in figure.possible_moves(self.field):
            if not self.is_under_attack(move, figure.get_color()):
                return False
        return True

    def find_kings(self):
        pos = []
        for line in self.field:
            for fig in line:
                if type(fig) == King:
                    pos.append(fig.get_position())
        return pos

    def initpicture(self):
        self.log = []

        self.cells = [[QLabel(self) for _ in range(8)] for _ in range(8)]
        for rowp in range(8):
            for colp in range(8):
                self.cells[rowp][colp].setText('')
                self.cells[rowp][colp].resize(self.cell_size, self.cell_size)
                self.cells[rowp][colp].move(self.cell_size * (colp + 1), self.cell_size * (rowp + 1))

    def mousePressEvent(self, event):
        if self.end:
            self.startgame()
        col = event.x() // 50 - 1
        row = event.y() // 50 - 1
        if 8 > col >= 0 and 8 > row >= 0:
            fig = self.field[row][col]
            if len(self.log) == 0:
                if fig and fig.get_color() == self.color:
                    self.log.append((row, col))
            elif len(self.log) == 1:
                if fig and self.field[self.log[0][0]][self.log[0][1]].get_color() == fig.get_color():
                    self.log.pop()
                    self.log.append((row, col))
                elif (row, col) in self.field[self.log[0][0]][self.log[0][1]].possible_moves(self.field):
                    self.log.append((row, col))
                    self.move_figure(*self.log)
                    self.log = []
                    self.change_player()
                    self.draw_field()

            res = None
            pos_of_kings = [*self.find_kings()]
            if len(pos_of_kings) < 2:
                king = self.field[pos_of_kings[0][0]][pos_of_kings[0][1]]
                self.endgame('Победа', king.get_color())
            for pos in pos_of_kings:
                king = self.field[pos[0]][pos[1]]
                if self.check_mat(king):
                    res = 'Шах и мат'
                    color = king.get_color()
                    break
                else:
                    res = None
            if res:
                self.endgame(res, color)

    def draw_field(self):
        for i in range(8):
            for j in range(8):
                self.clean_cell(self.cells[i][j])
                self.draw_cell(self.field[i][j])

    def draw_cell(self, figure):
        if figure:
            self.cells[figure.row][figure.column].setPixmap(QPixmap(figure.picture))

    def clean_cell(self, cell):
        cell.setPixmap(QPixmap())

    def endgame(self, res, color):
        if color == WHITE:
            self.result.setText(f'{res} королю Белого цвета!')
        else:
            self.result.setText(f'{res} королю Чёрного цвета!')
        self.end = True
