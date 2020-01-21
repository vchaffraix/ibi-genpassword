from Individu import Password
from Population import Population
import params

if __name__ == "__main__":
    pop = Population(Password, params.N)
    while True:
        print(pop.nextGen())

