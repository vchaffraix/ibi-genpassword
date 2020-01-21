from Individu import Individu
import params


class Population():
    # IND : classe des individus pour l'instanciation
    # n : nombre d'individus dans une population
    def __init__(self, IND, n):
        super().__init__()
        if(isinstance(IND, Individu)):
            self.IND = IND
        else:
            raise Exception(IND + " : n'est pas un type d'individu.")

        self.n = n
        self.pop = []
        for i in range(n):
            self.pop.append(self.IND())
    # Tri de la population par fitness
    def sort(self):
        self.pop.sort(key=lambda x: x.fitness(), reverse=True)

