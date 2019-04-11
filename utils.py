import numpy as np
import random
import pandas as pd


class Board:
    def __init__(self, n = 10, k=15):
        self.n = n
        self.k = k
        self.board = np.array([ [0]*n for i in range(n)])
        self.cans = random.sample([(i,j) for i in range(n) for j in range(n)], k)
        for coords in self.cans:
            self.board[coords[0], coords[1]] = 1
            
    def loc(self, x):
        i,j = x
        if (0 <= i < self.n) and (0 <= j < self.n):
            return self.board[i,j]
        else:
            return -1
    
    def __repr__(self):
        return str(self.board)
    
    
class RobotEngine: 
    def __init__(self):
        self.chromosome = []
        
    def L(self):
        return self.x, self.y-1
    
    def D(self):
        return  self.x+1, self.y
    
    def P(self):
        return self.x, self.y
        
    def U(self):
        return self.x-1, self.y
    
    def R(self):
        return self.x, self.y+1
    
    def screen(self):
        g = {}
        g['L'] = self.board.loc(self.L())
        g['D'] = self.board.loc(self.D())
        g['P'] = self.board.loc(self.P())
        g['U'] = self.board.loc(self.U())
        g['R'] = self.board.loc(self.R())
        return g
    
    def action(self, a='P'):
        if a == 'P':
            val = self.board.loc((self.x, self.y))
            self.bag += max(0, val)
            if val > 0:
                self.board.board[self.x, self.y] = 0
        else:
            self.x, self.y = eval('self.%s()' % a)
    
    def move(self):
        d = self.decision()
        self.action(d)
        
    def run(self, init_board, N=50):
        self.n = init_board.n - 1
        self.x, self.y = [ np.random.randint(self.n) for i in range(2) ]
        self.board_states = [init_board.board.copy()]
        self.board = init_board
        self.bag = 0
        self.path = [(self.x, self.y)]
          
        for i in range(N):
            self.move()
            self.path.append((self.x, self.y))
            bs = self.board.board.copy()
            self.board_states.append(bs)
        return self.bag            
    
    
    def reshape(self, board, i):
        b = pd.DataFrame(board).unstack()
        b = b.reset_index()
        b.columns = ['y','x','cans']
        b.index = [i] * b.shape[0]
        return b

    def save(self, filename):
        np.savetxt(filename + '_path.csv', np.array(self.path), delimiter=",", fmt = '%.1f')
        to_save = []
        for i,br in enumerate(self.board_states):
            to_save.append(self.reshape(br, i))
        to_save = pd.concat(to_save, axis=0)
        to_save.index.name = 'step'
        to_save.to_csv(filename + '_board.csv', header=True)
    
class RandomRobot(RobotEngine):
    
    def choose_direction(self, possibilities):
        omit_wall = [ k for k,v in possibilities.iteritems() if not v == -1]
        return np.random.choice(omit_wall)
    
    def decision(self):
        possibilities = self.screen()
        if possibilities.values() not in [ gene for gene,d in self.chromosome ]:
            decision = self.choose_direction(possibilities)
            self.chromosome += zip([possibilities.values()],decision)
        else:
            decision = [ d for gene,d in self.chromosome if gene == possibilities.values() ][0]
        return decision