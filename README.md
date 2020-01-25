TP Intelligence Bio-Inspirée : Algorithmes génétiques
=====================================================

Dépendances
-----------
* Python 3.7

La liste des dépendances est diponible dans `requirements.txt` :
```
tqdm==4.41.0
matplotlib==3.1.2
```

Installation des dépendances avec pip :
```
pip3 install --user -r requirements.txt
```

Utilisation
-----------
### Exécution de l'algorithme
Pour lancer l'algorithme il suffit d'exécution le script `password-gen.py` :
```
python3.7 password-gen.py
```
On peut alors suivre l'évolution de la fitness en direct ainsi que le meilleur mot de passe de la génération actuelle.
### Modification des hyper-paramètres
La liste des hyper-paramètres utilisés par l'algorithme est modifiable dans le fichier `params.py`.

| Paramètre       | Description                                                                              |
|-----------------|------------------------------------------------------------------------------------------|
| GROUP_ID        | ID de groupe qui donne le mot de passe à trouver                                         |
| N               | Taille de la population principale                                                       |
| N_ENV2          | Taille de la population parallèle                                                        |
| FREQ_MIX        | Fréquence à laquelle les populations sont mélangées                                      |
| MAXGEN          | Nombre maximal de générations pour que l'algorithme s'arrête s'il n'a pas trouvé le code |
| e               | Nombre d'élites.                                                                         |
| p_cross         | Probabilité de cross-over.                                                               |
| p_mut           | Probabilité de mutation                                                                  |
| SELECT_FUNCTION | Fonction de sélection : `wheel` ou `tournament`                                          |
| TOURNAMENT_SIZE | Taille du tournoi si `tournament`                                                        |
| TOURNAMENT_P    | Probabilité de garder le gagnant du tournoi si `tournament`                              |
| CROSS_FUNCTION  | Fonction de cross-over : `slice` ou `merge`                                              |
| n_test          | Nombre de répétition du test de ces paramètres (en mode *benchmark*)                       |

### Mode benchmark
Pour exécuter en mode *benchmark* :
```
python3.7 password-gen.py --benchmark 
```
Dans ce mode on ne voit plus la courbe de fitness ni le mot de passe mais juste une barre de progression (ce qui accélère l'exécution). Une fois terminé les résultats sont enregistrés dans `results.json`.

On peut également tester plusieurs hyper-paramètres en les chargeant depuis un json :
```
python3.7 password-gen.py --benchmark -p params.json
```
#### Analyse des résultats
On peut avoir un résumé des résultats du benchmark en exécution le script `show-results.py` :
```
python3.7 show-results.py results.json
```

