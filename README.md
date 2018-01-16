# domineering
exercise from strategical game and heuristic learning

1. represent checkerboard and blows
2. find all possible blows
3. create a random game from the current situation
4. chose a blow with a Monte Carlo flow and do 20 simulation possible move
5. choose next possible blow for which we do a random game with
argmax_i(\mu_i+0.4\sqrt{\frac{\log(n_{total}}{n_i}})
6. générer le fichier csv avec des positions and for each of them the best blow
