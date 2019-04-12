import sys
from time import gmtime, strftime
import os
import copy
import random
import argparse

from utils import Board, RandomRobot


class Evolution:
    def __init__(self, population_size = 40, n_boards = 100, mess = .05, steps=50):
        self.population_size = population_size
        self.steps = steps
        self.n_boards = n_boards
        self.mess = mess
        self.init_generation = [ RandomRobot() for i in range(population_size)]
        self.name = strftime("%Y-%m-%dT%H:%M:%S", gmtime()) + 'steps=%i_mess_perc=%i' % (self.steps, self.mess*100)
        if not os.path.exists(self.name):
            os.mkdir(self.name)
        with open(self.name + '/learn_curve.csv', 'w') as fp:
            fp.write('generation, cans\n')
        self.evolution = []
        
    def selection(self, population):
        robot_cans = []
        for r in population:
            r_bag = 0
            for i in range(self.n_boards):
                b = Board()
                r_bag += r.run(b, N = self.steps)
            robot_cans.append((r, float(r_bag)/self.n_boards))
        robot_cans.sort(key=lambda x: x[1], reverse=True)
        return robot_cans[:5]
    
    def reproduction(self, parents, k=8):
        offspring = []
        for r in parents:
            for i in range(k):
                child = copy.deepcopy(r)
                c = child.chromosome
                idx = random.sample(range(len(c)),int(len(c) * self.mess))
                for j in idx:
                    gene, d = c[j]
                    new_d = child.choose_direction(dict(zip(['P','R','U','L','D'], gene)))
                    c[j] = gene, new_d                
                offspring.append(child)   
        return offspring
    
    def log_last(self):
        results = [v for r,v in self.evolution[-1]]
        print('Epoch: %s, best5 result: %s' % (len(self.evolution)-1, str(results)))
        
    def evaluate(self, n_epochs=15):
        best5 = self.selection(self.init_generation)
        self.evolution.append(best5)
        self.log_last()
        
        for t in range(n_epochs):
            new_generation = self.reproduction([robot for robot,cans in best5])
            best5 = self.selection(new_generation)
            self.evolution.append(best5)
            self.log_last()
            r, result = best5[0]
            if t % 20 == 0:
                r.save(os.path.join(self.name, 'epoch%i' % (t+1)))
            with open(self.name + '/learn_curve.csv', 'a') as fp:
                fp.write('%i, %f\n' % (t, result))
            
    def ith_best(self, i=1):
        return [ k[i-1] for k in self.evolution]
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--steps', '-s', help="number of steps on the boards", type= int, default=50)
    parser.add_argument('--mess', '-m', help="fraction of muttations", type= float, default=0.05)
    parser.add_argument('--n_epochs', '-n', help="number of generations", type= int, default=500)
    args = parser.parse_args()

    e1 = Evolution(steps=args.steps, mess = args.mess)
    e1.evaluate(args.n_epochs)
