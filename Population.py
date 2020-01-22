from Individu import Individu
import random
import params
import copy
import time



class Population():
    # IND : classe des individus pour l'instanciation
    # n : nombre d'individus dans une population
    def __init__(self, IND, n):
        super().__init__()
        if(issubclass(IND, Individu)):
            self.IND = IND
        else:
            raise Exception(IND + " : n'est pas un type d'individu.")

        self.n = n
        self.pop = []
        for i in range(n):
            self.pop.append(self.IND())
        self.fitsum = sum(i.fitness() for i in self.pop)
        self.best = None

    # Tri de la population par fitness et calcul du max
    # def preselect(self):
        # self.pop.sort(key=lambda x: x.fitness(), reverse=True)
        # self.fitsum = sum(i.fitness() for i in self.pop)
    # Sélection par "roulette"
    def wheel_pick(self):
        tirage = random.random()
        sum_ = 0
        for i in self.pop:
            sum_ += i.fitness()/self.fitsum
            if sum_ >= tirage:
                return i
        return i
    # Sélection par "tournoi"
    def tournament_pick(self):
        tn = random.sample(self.pop, params.TOURNAMENT_SIZE)
        while True:
            winner = max(tn, key=lambda x:x.fitness())
            if len(tn)==1 or random.random() < params.TOURNAMENT_P:
                break
            tn.remove(winner)
        return winner 
    # On utilise la fonction de sélection définie dans params
    SELECT_FUNCTIONS = {
        "wheel": wheel_pick,
        "tournament": tournament_pick
    }
    def pick(self):
        return self.SELECT_FUNCTIONS[params.SELECT_FUNCTION](self)

    def nextGen(self):
        n_desc = 0
        desc_pop = []
        # Élitisme
        if(params.e>0):
            elit = self.pop[:params.e]
            max_fit = elit[0].fitness()
        else:
            elit = []
            max_fit = 0

        while n_desc<self.n-10:
            p1 = copy.copy(self.pick())
            p2 = copy.copy(self.pick())
            tirage = random.random()
            if params.p_cross>=tirage:
                p1, p2 = p1.cross(p2)
            p1.mutate(params.p_mut)
            p2.mutate(params.p_mut)
            n_desc += 2
            max_fit = max(max_fit, p1.fitness(), p2.fitness())
            desc_pop.extend((p1, p2))
        for i in range(10):
            p = self.IND()
            max_fit = max(max_fit, p.fitness())
            desc_pop.append(p)
            n_desc += 1
        desc_pop.extend(elit)
        self.pop = sorted(desc_pop, key=lambda x: x.fitness(), reverse=True)
        self.fitsum = sum(i.fitness() for i in self.pop)
        self.best = self.pop[0]
        return (max_fit, self.fitsum/n_desc)
