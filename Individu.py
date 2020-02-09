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
        self.fitness_val = check(params.GROUP_ID, self.password)
    # La fitness est donnée par la similarité avec le bon mot de passe
    def fitness(self):
        return self.fitness_val
    # Fonction de mutation d'un mot de passe
    def mutate(self, p):
        i=0
        while i<len(self.password):
            tirage = random.random()
            if p>=tirage:
                empty_char = []
                if(len(self.password)>min(params.PASS_LENGTH)):
                    empty_char.append("")
                new_pass = self.password[:i] + random.choice(list(params.CHARS)+empty_char)
                if random.random() < 0.5 and self.length<max(params.PASS_LENGTH):
                    new_pass += self.password[i:]
                    i += 1
                elif i<self.length-1:
                    new_pass += self.password[i+1:]
                self.password = new_pass
            i += 1
        self.length = len(self.password)
        self.fitness_val = check(params.GROUP_ID, self.password)

    def cross_slice(self, p2):
        l1 = self.length
        l2 = p2.length
        breakpoint = random.randrange(min(l1, l2))
        crossed1 = self.password[:breakpoint] + p2.password[breakpoint:]
        crossed2 = p2.password[:breakpoint] + self.password[breakpoint:]
        return (Password(crossed1), Password(crossed2))
    def cross_merge(self, p2):
        l1 = self.length
        l2 = p2.length
        crossed1 = ""
        crossed2 = ""
        for i in range(max(l1,l2)):
            if i<l1:
                c1 = self.password[i]
            else:
                c1 = ""
            if i<l2:
                c2 = p2.password[i]
            else:
                c2 = ""

            if random.random() < 0.5:
                crossed1 += c1
                crossed2 += c2
            else:
                crossed1 += c2
                crossed2 += c1
        return (Password(crossed1), Password(crossed2))


    # On utilise la fonction de sélection définie dans params
    CROSS_FUNCTIONS = {
        "slice": cross_slice,
        "merge": cross_merge
    }
    # Fonction de cross-over de deux mots de passe
    def cross(self, p2):
        return self.CROSS_FUNCTIONS[params.CROSS_FUNCTION](self, p2)
