from window import *


class Figure:
    def __init__(self, row, column, color, picture):
        self.row = row
        self.column = column
        self.color = color
        self.name = ''
        self.picture = picture

    def set_position(self, row, col):
        self.row = row
        self.column = col

    def get_position(self):
        return self.row, self.column

    def possible_moves(self, field):
        pass

    def get_color(self):
        return self.color

    def char(self):
        return self.name


class Pawn(Figure):
    def __init__(self, row, column, color, picture):
        super().__init__(row, column, color, picture)
        self.name = 'P'
        self.first_act = True

    def set_position(self, row, col):
        self.row = row
        self.column = col
        if self.first_act:
            self.first_act = False

    def possible_moves(self, field):
        r = self.row
        c = self.column
        moves = []
        if self.get_color() == WHITE:
            if self.first_act and not field[r + 2][c]:
                moves.append((r + 2, c))
            if r + 1 <= 7 and not field[r + 1][c]:
                moves.append((r + 1, c))
            if r + 1 <= 7 and c + 1 <= 7 and field[r + 1][c + 1] and field[r + 1][c + 1].get_color() != self.color:
                moves.append((r + 1, c + 1))
            if r + 1 <= 7 and c - 1 >= 0 and field[r + 1][c - 1] and field[r + 1][c - 1].get_color() != self.color:
                moves.append((r + 1, c - 1))
        else:
            if self.first_act and not field[r - 2][c]:
                moves.append((r - 2, c))
            if r - 1 >= 0 and not field[r - 1][c]:
                moves.append((r - 1, c))
            if r - 1 >= 0 and c + 1 <= 7 and field[r - 1][c + 1] and field[r - 1][c + 1].get_color() != self.color:
                moves.append((r - 1, c + 1))
            if r - 1 >= 0 and c - 1 >= 0 and field[r - 1][c - 1] and field[r - 1][c - 1].get_color() != self.color:
                moves.append((r - 1, c - 1))
        return moves


class Rook(Figure):
    def __init__(self, row, column, color, picture):
        super().__init__(row, column, color, picture)
        self.name = 'R'

    def possible_moves(self, field):
        r = self.row
        c = self.column
        moves = []
        for dr in range(1, 8):
            moves.append((r + dr, c))
            if r + dr >= 7 or field[r + dr][c]:
                break
        for dr in range(-1, -8, -1):
            moves.append((r + dr, c))
            if r + dr <= 0 or field[r + dr][c]:
                break
        for dc in range(1, 8):
            moves.append((r, c + dc))
            if c + dc >= 7 or field[r][c + dc]:
                break
        for dc in range(-1, -8, -1):
            moves.append((r, c + dc))
            if c + dc <= 0 or field[r][c + dc]:
                break
        return moves


class Knight(Figure):
    def __init__(self, row, column, color, picture):
        super().__init__(row, column, color, picture)
        self.name = 'N'

    def possible_moves(self, field):
        r = self.row
        c = self.column
        moves = [(r + 2, c + 1), (r + 2, c - 1), (r - 2, c + 1), (r - 2, c - 1),
                 (r + 1, c + 2), (r + 1, c - 2), (r - 1, c + 2), (r - 1, c - 2)]
        nmoves = []
        for move in moves:
            if 0 <= move[0] <= 7 and 0 <= move[1] <= 7:
                nmoves.append(move)
        return nmoves


class Bishop(Figure):
    def __init__(self, row, column, color, picture):
        super().__init__(row, column, color, picture)
        self.name = 'B'

    def possible_moves(self, field):
        r = self.row
        c = self.column
        moves = []
        for d in range(1, 8):
            moves.append((r - d, c - d))
            if r - d <= 0 or c - d <= 0 or field[r - d][c - d]:
                break
        for d in range(1, 8):
            moves.append((r + d, c - d))
            if r + d >= 7 or c - d <= 0 or field[r + d][c - d]:
                break
        for d in range(1, 8):
            moves.append((r - d, c + d))
            if r - d <= 0 or c + d >= 7 or field[r - d][c + d]:
                break
        for d in range(1, 8):
            moves.append((r + d, c + d))
            if r + d >= 7 or c + d >= 7 or field[r + d][c + d]:
                break
        return moves


class Queen(Figure):
    def __init__(self, row, column, color, picture):
        super().__init__(row, column, color, picture)
        self.name = 'Q'

    def possible_moves(self, field):
        r = self.row
        c = self.column
        moves = []
        for dr in range(1, 8):
            moves.append((r + dr, c))
            if r + dr >= 7 or field[r + dr][c]:
                break
        for dr in range(-1, -8, -1):
            moves.append((r + dr, c))
            if r + dr <= 0 or field[r + dr][c]:
                break
        for dc in range(1, 8):
            moves.append((r, c + dc))
            if c + dc >= 7 or field[r][c + dc]:
                break
        for dc in range(-1, -8, -1):
            moves.append((r, c + dc))
            if c + dc <= 0 or field[r][c + dc]:
                break
        for d in range(1, 8):
            moves.append((r - d, c - d))
            if r - d <= 0 or c - d <= 0 or field[r - d][c - d]:
                break
        for d in range(1, 8):
            moves.append((r + d, c - d))
            if r + d >= 7 or c - d <= 0 or field[r + d][c - d]:
                break
        for d in range(1, 8):
            moves.append((r - d, c + d))
            if r - d <= 0 or c + d >= 7 or field[r - d][c + d]:
                break
        for d in range(1, 8):
            moves.append((r + d, c + d))
            if r + d >= 7 or c + d >= 7 or field[r + d][c + d]:
                break
        return moves


class King(Figure):
    def __init__(self, row, column, color, picture):
        super().__init__(row, column, color, picture)
        self.name = 'K'

    def possible_moves(self, field):
        r = self.row
        c = self.column
        moves = [(r + i, c + j) for i in range(-1, 2) for j in range(-1, 2)]
        nmoves = []
        for move in moves:
            if 0 <= move[0] <= 7 and 0 <= move[1] <= 7:
                if not field[move[0]][move[1]] or (
                        field[move[0]][move[1]] and field[move[0]][move[1]].get_color() != self.color):
                    nmoves.append(move)
        nmoves.append((r, c))
        return nmoves


WHITE = 0
BLACK = 1


class Board:
    def __init__(self):
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

    def check_mat(self, figure):
        for move in figure.possible_moves(self.field):
            if not self.is_under_attack(move, figure.get_color()):
                return False
        return True

    def is_under_attack(self, pos, color):
        for line in self.field:
            for fig in line:
                if fig and fig.get_color() != color:
                    if pos in fig.possible_moves(self.field):
                        return True
        return False

    def find_kings(self):
        pos = []
        for line in self.field:
            for fig in line:
                if type(fig) == King:
                    pos.append(fig.get_position())
        return pos
