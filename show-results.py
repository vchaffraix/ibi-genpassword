import json
import argparse



parser = argparse.ArgumentParser(description=None)
parser.add_argument("results", metavar="RESULTS", help="Fichier JSON qui contient les résultats")
args = parser.parse_args()

results = json.load(open(args.results, "r"))
i = 0
for res in results:
    i += 1
    print(str(i)+".")
    print("------------------------PARAMS-----------------------")
    for key in res["params"]:
        print("\t* "+ key + ":" + str(res["params"][key]))
    print("-----------------------RÉSULTAT----------------------")
    sum_n = 0
    sum_time = 0
    n_found = 0
    password = None
    for r in res["results"]:
        sum_n += r["n_generations"]
        sum_time += r["time"]
        if(r["found"]):
            password = r["password"]
            n_found += 1
    print("Nombre moyen de génération : " + str(round(sum_n/n_found,2)))
    print("Temps moyen d'exécution de l'algorithme : " + str(round(sum_time/n_found,2)) + "s")
    print("Mot de passe trouvé : " + str(n_found) + "/" + str(len(res["results"])))
    print("Mot de passe : " + password)
    print("-----------------------------------------------------")

