import numpy as np


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
        
    def reshape(self, i):
        b = pd.DataFrame(self.board).unstack()
        b = b.reset_index()
        b.columns = ['x','y','cans']
        b.index = [i] * b.shape[0]
        return b
    
    def __repr__(self):
        return str(self.board)
    