import sys

class Cube():

    def __init__(self):
        # 0 = correct, 1 = incorrect orientation
        # edge order: U, L, R, D
        self.edges = [0, 0, 0, 0]

        # UL = 1, UR = 2, DL = 3, DR = 4
        self.corners = [1, 2, 3, 4]

    '''Returns True if cube is solved, False otherwise'''
    def isSolved(self):
        if self.edges == [0,0,0,0] and self.corners == [1, 2, 3, 4]:
            return True
        else:
            return False

    def swapCorners(self, c1, c2):
        tmp = self.corners[c1]
        self.corners[c1] = self.corners[c2]
        self.corners[c2] = tmp

    def U(self):
        # swap UL and UR corners
        self.swapCorners(0,1)

        # flip U edge
        self.edges[0] = (self.edges[0] + 1) % 2

    def D(self):
        # swap DL and DR corners
        self.swapCorners(2,3)

        # flip D edge
        self.edges[3] = (self.edges[3] + 1) % 2

    def R(self):
        # swap DR and UR corners
        self.swapCorners(3,1)

        # flip R edge
        self.edges[2] = (self.edges[2] + 1) % 2

    def L(self):
        # swap UL and DL corners
        self.swapCorners(0,2)

        # flip L edge
        self.edges[1] = (self.edges[1] + 1) % 2

    def shuffle(self):
        pass

    def cornerCoord(self, i):
        if i in [0, 1]:
            return 2 * i
        elif i in [2, 3]:
            return 2 * i + 2
        else:
            return -1

    def generateFullLayout(self):
        # edges depend on self.edges
        whiteSide = ['W'] * 9
        for i in range(len(self.edges)):
            if self.edges[i] == 1:
                # 0 -> 1, 1 -> 3, 2 -> 5, 3 -> 7
                whiteSide[i*2 + 1] = 'Y'
        
        # flip if a corner is outside of its diagonal
        for i in range(len(self.corners)):
            # Y for c1, c4 in 1,2 and for c2,c3 in 0,3
            if (self.corners[i] in [1,4] and i in [1,2]) or (self.corners[i] in [2,3] and i in [0,3]):
                # 0 -> 0, 1 -> 2, 2 -> 6, 3 -> 8
                whiteSide[self.cornerCoord(i)] = 'Y'

        # Yellow mirrors white
        yellowSide = ['Y'] * 9
        for i in range(len(whiteSide)):
            if whiteSide[i] == 'Y':
                yellowSide[i] = 'W'

        # corner orientations: 1: OG, 2: BO, 3: RG, 4: BR
        orangeSide = ['O'] * 3
        greenSide = ['G'] * 3
        blueSide = ['B'] * 3
        redSide = ['R'] * 3
        for i in range(2):
            # positions [0,1], pieces [3,4]
            if self.corners[i] in [3,4]:
                # 0 -> 0, 1 -> 2
                orangeSide[i * 2] = 'R'

            # positions [0,2], pieces [2,4]
            if self.corners[i * 2] in [2,4]:
                # 0 -> 0, 1 -> 2
                greenSide[i * 2] = 'B'

            # positions [1,3], pieces [1,3]
            if self.corners[i * 2 + 1] in [1,3]:
                # 0 -> 0, 1 -> 2
                blueSide[i * 2] = 'G'

            # positions [2,3], pieces [1,2]
            if self.corners[i + 2] in [1,2]:
                # 0 -> 0, 1 -> 2
                redSide[i * 2] = 'O'

        return (whiteSide, yellowSide, orangeSide, greenSide, blueSide, redSide)

    def __str__(self):
        w, y, o, g, b, r = self.generateFullLayout()
        rows = []
        rows.append(' ' + ''.join(o))
        rows.append(str(g[0]) + ''.join(w[:3]) + str(b[0]))
        rows.append(str(g[1]) + ''.join(w[3:6]) + str(b[1]))
        rows.append(str(g[2]) + ''.join(w[6:]) + str(b[2]))
        rows.append(' ' + ''.join(r))
        return '\n'.join(rows)



if __name__=="__main__":
    c = Cube()

    uMoves = ['U', 'u']
    dMoves = ['D', 'd']
    lMoves = ['L', 'l']
    rMoves = ['R', 'r']

    executedMoves = []
    # Parse and execute input
    for letter in sys.argv[1]:
        if letter in uMoves:
            c.U()
            executedMoves.append('U')
        elif letter in dMoves:
            c.D()
            executedMoves.append('D')
        elif letter in lMoves:
            c.L()
            executedMoves.append('L')
        elif letter in rMoves:
            c.R()
            executedMoves.append('R')


    # Print result
    print(c)
    print("".join(executedMoves))