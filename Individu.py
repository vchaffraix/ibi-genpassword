from abc import ABC, abstractmethod
from blackbox37 import check
import random
import params

# Interface d'un individu
class Individu(ABC):
    def __init__(self):
        super().__init__()
    @abstractmethod
    def fitness(self):
        pass
    @abstractmethod
    def mutate(self, p):
        pass
    @abstractmethod
    def cross(self, i):
        pass

# Les mots de passe sont des individus
class Password(Individu):
    def __init__(self, password=None):
        super().__init__()
        if(password!=None):
            self.length = len(password)
            self.password = password
        else:
            self.length = random.choice(params.PASS_LENGTH)
            self.password = "".join(random.choices(params.CHARS, k=self.length))
    # La fitness est donnée par la similarité avec le bon mot de passe
    def fitness(self):
        return check(params.GROUP_ID, self.password)
    # Fonction de mutation d'un mot de passe
    def mutate(self, p):
        for i, c in enumerate(self.password):
            tirage = random.random()
            if p>=tirage:
                new_pass = self.password[:i] + random.choice(params.CHARS)
                if i<self.length-1:
                    new_pass += self.password[i+1:]
                self.password = new_pass
    # Fonction de cross-over de deux mots de passe
    def cross(self, p2):
        l1 = self.length
        l2 = p2.length
        breakpoint = random.randrange(min(l1, l2))
        crossed1 = self.password[:breakpoint] + p2.password[breakpoint:]
        crossed2 = p2.password[:breakpoint] + self.password[breakpoint:]
        return (Password(crossed1), Password(crossed2))
