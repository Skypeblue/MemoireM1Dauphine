# MemoireM1Dauphine

Pour lancer le processus TCP Window size, on lance dans un terminal :

<code>python3.7 AIMD.py delta</code>

avec delta, la dirac qu'on associe au processus AIMD. Ce nombre doit être compris entre 0 et 1 pour correspondre avec l'étude du rapport.  
Le programme suit simplement l'algo standard du processus AIMD. On a enlevé l'histogramme du processus AIMD, car il s'agissait d'un cas particulier du processus AIMD pour $delta_i=0$, on n'aurait pas eu une exponentielle de paramètre 1/rate qui suivrait l'histogramme associé au processus AIMD.


Pour lancer le billard stochastique dans un cercle, on lance dans un terminal :
<code>python3.7 markov_circ.py iter x_0 filename</code>

avec x_0 le point de départ de la chaine de Markov discrète, iter le nombre de point de la chaîne de Markov incluse qu'on veut simuler et filename pour le nom de l'image produite finale

Ce programme simule donc un billard stochastique dans un disque avec un histogramme dynamique. On peut changer la loi de réflexion, il suffit de choisir le "fun" qu'on veut qui correspond à la loi de réflexion. Ici ber, ter, arr représentent des lois discrètes fournissant des rosaces déterministes selon x_0 pour un iter avoisinant 30. Il y a aussi la loi du cosinus surélevé en utilisant la bibliothèque scipy.stat mais par défaut, la loi de réflexion suit une uniforme.

Pour lancer le billard stochastique dans un polygone convexe, on lance dans un terminal :
<code>python3.7 poly.py iter filename</code>

avec iter le nombre de point de la chaîne de Markov qu'on veut simuler et filename pour le nom de l'image produite finale

Ce programme simule un billard stochastique dans un polygone caractérisé par le tableau vertices. Pour avoir un polygone qu'on veut, on doit malheureusement préciser les sommets dans ce tableau vertices(Par un souci de temps, la possibilité de créer un polygone aléatoire n'a pas été réalisé). À la fin, on produit un processus AIMD des points du billard stochastique, crée de la manière suivante :
Entre deux points A et B de la frontière du polygone, on se crée une liste de points décrit à l'instar du processus décrit en page 16 à l'aide de la fonction linspace de numpy. Ensuite pour chaque point I de cette liste de points, on calcule la distance entre A et I. Une fois qu'on arrive à B, on ajoute un et on recommence ainsi de suite. D'où, on voit un processus qui augmente linéairement puis descend brutalement lorsqu'on arrive à un nouveau point de la frontière, ce qui correspond à un processus AIMD. On a mis en place ce procédé, pour établir un lien entre les deux processus mais sans succès.


<code>python3.7 disk.py iter x_0 filename</code>

Le programme disk.py lance aussi un billard stochastique dans un disque, toutefois, on se concentre sur le processus continu et on observe sa répartition dans le disque. D'où, on segmente le disque comme une pizza et on compte le nombre de point pour chaque région et on en fait un histogramme dynamique. À la fin du programme, la console affiche le nombre de point pour chaque région. Pour changer le nombre de région, on influe sur la variable nb, par défaut elle vaut 4 et cela correspond au nombre de droites, si on trace les 4 droites, on a 8 régions
