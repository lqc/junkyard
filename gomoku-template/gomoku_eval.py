class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Piece(object):
    def __init__(self, color, pos):
        self.vg = self.hg = self.lrg = self.grl = None
        self.color = color
        self.pos = pos

class Group(object):
    def __init__(self):
        self.pieces = []
        self.length = 0

    def addPiece(self, piece, propname):
        self.pieces[self.length] = {'piece':piece, 'prop': propname}
        self.length += 1
        piece[propname] = self

    def addGroup(self, other):
        i = 0;
        while(i < other.length):
            pieces[self.length] = other.pieces[i]
            pieces[self.length].piece[pieces[self.length].prop] = self
            length += 1;
            i += 1;

    def splitGroup(self, p):
        rem = Group()
        i = 0
        while(i < self.length):
            if (self.pieces[i].pos.y < p.pos.y) or ((self.pieces[i].pos.y == p.pos.y) \
             and (self.pieces[i].pos.x < p.pos.x)):
                i += 1;
                continue

            if self.pieces[i] == p:
                self.pieces[i] = self.pieces[self.length-1]
                self.pieces[self.length-1] = null
                self.length -= 1
                i -= 1
                i += 1
                continue

            x = self.pieces[i]
            self.pieces[i] = self.pieces[self.length-1]
            self.pieces[self.pieces-1] = null
            rem.pieces[rem.length] = x
            rem.length += 1
            self.length -= 1
            i -= 1
            i += 1

        return rem

BLACK = 0
WHITE = 1
SIZE = 13
CHARMAP = { None: '.', 0:'X', 1:'O' }

board = [None for _ in xrange(0,SIZE*SIZE)]
groups = [{1:0, 2:0, 3:0, 4:0, 5:0} for x in xrange(0,2)]

def print_board(board):
    for y in xrange(0,SIZE):
        for x in xrange(0,SIZE):
            print CHARMAP[board[y*SIZE+x]],
        print ''

def print_groups_and_board(board, groups):
    print "* BOARD *"
    print_board(board)

def make_move(color, point):
    board[point.y*SIZE + point.x] = color

if __name__ == '__main__':
    
    print_board(board)

    make_move(BLACK, Point(4, 12))
    print_groups_and_board(board, groups)
    make_move(WHITE, Point(3, 12))
    print_groups_and_board(board, groups)
    make_move(BLACK, Point(4, 11))
    print_groups_and_board(board, groups)
    make_move(WHITE, Point(5, 10))
    print_groups_and_board(board, groups)
    make_move(BLACK, Point(4, 10))
    print_groups_and_board(board, groups)
    make_move(WHITE, Point(6, 11))
    print_groups_and_board(board, groups)
    make_move(BLACK, Point(4, 9))
    print_groups_and_board(board, groups)
    make_move(WHITE, Point(4, 8))
    print_groups_and_board(board, groups)
    make_move(BLACK, Point(5, 9))
    print_groups_and_board(board, groups)
    make_move(WHITE, Point(3, 9))
    print_groups_and_board(board, groups)
    make_move(BLACK, Point(2, 10))
    print_groups_and_board(board, groups)
    make_move(WHITE, Point(7, 11))
    print_groups_and_board(board, groups)
    make_move(BLACK, Point(3, 10))
    print_groups_and_board(board, groups)
    make_move(WHITE, Point(7, 10))
    print_groups_and_board(board, groups)
    make_move(BLACK, Point(5, 8))
    print_groups_and_board(board, groups)
    make_move(WHITE, Point(6, 7))
    print_groups_and_board(board, groups)
    make_move(BLACK, Point(1, 10))
    print_groups_and_board(board, groups)
    make_move(WHITE, Point(0, 11))