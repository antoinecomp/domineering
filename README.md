# domineering
exercise from strategical game and heuristic learning

![8 times 8 checkerboard with pawns on ((b,8),(b,7)) and ((g,2),(h,2))](https://i.stack.imgur.com/14klB.png)


1. represent checkerboard and blows
2. find all possible blows
3. create a random game from the current situation
4. chose a blow with a Monte Carlo flow and do 20 simulation possible move
5. choose next possible blow for which we do a random game with
![equation](http://latex.codecogs.com/gif.latex?argmax_i%28%5Cmu_i&plus;0.4%5Csqrt%7B%5Cfrac%7B%5Clog%28n_%7Btotal%7D%7D%7Bn_i%7D%7D%29)
6. générer le fichier csv avec des positions and for each of them the best blow

## represent checkerboard and blows

Done in Python in an array

## find all possible blows

create a coupsPossibles function to test what are the possible attempts :
check if there is two continuous cell in the matrix and store them.
Do a for loop, and test for each cell if there is the one below and on the right is okay to play



