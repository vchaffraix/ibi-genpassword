import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.ticker import MaxNLocator
from Individu import Password
from Population import Population
from tqdm import tqdm
import params
import sys
import time
import argparse
import json


def updateParams(p):
    params.GROUP_ID = p["GROUP_ID"]
    params.N = p["N"]
    params.e = p["e"]
    params.p_cross = p["p_cross"]
    params.p_mut = p["p_mut"]
    params.SELECT_FUNCTION = p["SELECT_FUNCTION"]
    params.TOURNAMENT_SIZE = p["TOURNAMENT_SIZE"]
    params.TOURNAMENT_P = p["TOURNAMENT_P"]
    params.CROSS_FUNCTION = p["CROSS_FUNCTION"]

class Algo:
    def __init__(self):
        self.pop = Population(Password, params.N)
        self.index = 0
        self.t = 0
        self.x_vals = [self.index]
        self.best_vals = [self.pop.best.fitness()]
        self.mean_vals = [self.pop.fitsum/params.N]
        self.done = False
    def step(self):
        self.index += 1
        self.x_vals.append(self.index)
        t_0 = time.time()
        out = self.pop.nextGen()
        self.t += time.time() - t_0
        self.best_vals.append(out[0])
        self.mean_vals.append(out[1])
        if(out[0]==1):
            self.done = True
    def results(self):
        return {
            "group_id":params.GROUP_ID,
            "password":alg.pop.best.password,
            "best_fitness":alg.best_vals,
            "average_fitness":alg.mean_vals,
            "time":alg.t,
            "n_generations":alg.index
        }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=None)
    parser.add_argument("--benchmark", action="store_true", help="Enregistre les résults")
    parser.add_argument("-p", "--params", action="store", help="Charge les paramètres à tester")
    args = parser.parse_args()

    benchmarks = []

    if(args.benchmark):
        if(args.params is None):
            n_test = 1
        else:
            benchmark_params = json.load(open(args.params, "r"))
            n_test = len(benchmark_params)
        pbar = tqdm(total=params.MAXGEN*n_test)
        for i in range(n_test):
            updateParams(benchmark_params[i])
            alg = Algo()
            while not(alg.done):
                alg.step()
                pbar.update(1)
            pbar.update(params.MAXGEN - alg.index)
            benchmarks.append(alg.results())
        f = open("results.json", "w")
        json.dump(benchmarks, f)

    else:
        plt.style.use("ggplot")
        alg = Algo()
        def animate(i):
            if(not(alg.done)):
                alg.step()
                sys.stdout.flush()
                l = (max(params.PASS_LENGTH) - len(alg.pop.best.password))
                sys.stdout.write("\r"+"|" + "."*5 + alg.pop.best.password + "*"*l + "."*3 + "|")
                # print(pop.best.password)
                plt.cla()

                if(alg.done):
                    sys.stdout.flush()
                    sys.stdout.write("\r"+"|" + "."*(4+l//2) + alg.pop.best.password + "."*(l//2) + "."*4 + "|\n")
                    print("|" + "-"*(8+max(params.PASS_LENGTH)) + "|")
                    print("Time : " + str(alg.t) + "s")
                    print("Number of generation : " + str(alg.index))
                    plt.scatter(alg.x_vals[alg.index], alg.best_vals[alg.index], marker="x")
                # plt.legend(loc="upper left")
                plt.plot(alg.x_vals, alg.best_vals, "crimson")
                plt.plot(alg.x_vals, alg.mean_vals, "tab:purple")
                plt.gca().legend(("Best fitness", "Average fitness"))
                plt.gcf().suptitle("Évolution de la fitness au cours des générations", fontsize=12)
                plt.xlabel("Génération")
                plt.ylabel("Fitness")

        print("|" + "-"*5 + "CRACKING THE CODE" + "-"*4 + "|")
        print("|" + "-"*(10+max(params.PASS_LENGTH) - 2) + "|")
        anim = animation.FuncAnimation(plt.gcf(), animate, interval=1)
        plt.gcf().canvas.set_window_title("password-gen")
        plt.show()

