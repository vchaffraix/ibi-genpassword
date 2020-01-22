import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.ticker import MaxNLocator

from Individu import Password
from Population import Population
import params
import sys



if __name__ == "__main__":
    plt.style.use("ggplot")

    pop = Population(Password, params.N)
    index = 0
    x_vals = [index]
    best_vals = [pop.best.fitness()]
    mean_vals = [pop.fitsum/params.N]
    stop = False
    def animate(i):
        global stop
        if(not(stop)):
            global index
            index += 1
            x_vals.append(index)
            out = pop.nextGen()
            best_vals.append(out[0])
            mean_vals.append(out[1])
            # print(out)
            sys.stdout.flush()
            l = (max(params.PASS_LENGTH) - len(pop.best.password))
            sys.stdout.write("\r"+"|" + "."*5 + pop.best.password + "*"*l + "."*3 + "|")
            # print(pop.best.password)
            if(out[0]==1):
                stop = True
                sys.stdout.flush()
                sys.stdout.write("\r"+"|" + "."*(4+l//2) + pop.best.password + "."*(l//2) + "."*4 + "|\n")
                print("|" + "-"*(8+max(params.PASS_LENGTH)) + "|")
            plt.cla()
            # plt.legend(loc="upper left")
            plt.plot(x_vals, best_vals, "crimson")
            plt.plot(x_vals, mean_vals, "tab:purple")
            plt.gca().legend(("Best fitness", "Average fitness"))
            plt.gcf().suptitle("Évolution de la fitness au cours des générations", fontsize=12)
            plt.xlabel("Génération")
            plt.ylabel("Fitness")

    print("|" + "-"*5 + "CRACKING THE CODE" + "-"*4 + "|")
    print("|" + "-"*(10+max(params.PASS_LENGTH) - 2) + "|")
    anim = animation.FuncAnimation(plt.gcf(), animate, interval=200)
    plt.gcf().canvas.set_window_title("password-gen")
    plt.show()

