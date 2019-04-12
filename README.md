# Genetic Algorithm in action


Generation 1 | Generation 21 | Generation 41
:--------------------:|:--------------------:|:--------------------:
<img alt='a' src="https://raw.githubusercontent.com/katsob/evolution/master/2019-04-12T15:04:13steps=50_mess_perc=3/animations/epoch1.gif" width="300"  /> | <img alt='a' src="https://raw.githubusercontent.com/katsob/evolution/master/2019-04-12T15:04:13steps=50_mess_perc=3/animations/epoch21.gif" width="300"  /> | <img alt='a' src="https://raw.githubusercontent.com/katsob/evolution/master/2019-04-12T15:04:13steps=50_mess_perc=3/animations/epoch41.gif" width="300"  />

Generation 101 | Generation 201  | Generation 281
:--------------------:|:--------------------:|:--------------------:
<img alt='a' src="https://raw.githubusercontent.com/katsob/evolution/master/2019-04-12T15:04:13steps=50_mess_perc=3/animations/epoch101.gif" width="300"  /> | <img alt='a' src="https://raw.githubusercontent.com/katsob/evolution/master/2019-04-12T15:04:13steps=50_mess_perc=3/animations/epoch201.gif" width="300"  /> | <img alt='a' src="https://raw.githubusercontent.com/katsob/evolution/master/2019-04-12T15:04:13steps=50_mess_perc=3/animations/epoch281.gif" width="300"  />

### Learning curves
Average number of the cans that was picked by the best robot in subsequent generations (plotted by different parameters)

![](https://raw.githubusercontent.com/katsob/evolution/master/learning_curves.png)

### Assumptions

* 1000 generations was trained.
* There is population of `40` robots in each generation.
* Each robot goes on `100` different boards and can do only `steps=50`.
* Each board contains 15 randomly distributed cans.
* Measure of success: mean number of collected cans (calculated over all different boards).
* `5` best robots was selected in each generation. Those robots were reproducted (`8` times each) to obtain new generation of `40` robots.
* Each robot has a _choromosome_. The _chromosome_ is a list of decisions to make in specific situations (_genes_). As a situation (_gene_) we mean whether or not fields on the left (a), right (b), in front of (c), behind (d) and current position of the robot (e) contain any can. The _gene_ is coded as a binary vector (a,b,c,d,e) - 1 if there is a can, 0 if not (additionaly: -1 for the wall). There can be 32 different situations on the board for each 5 different decisions can be made (go left (L), right (R), up (U), down (D) or pick up (P)). This gives us 160 possible genes. Example of _chromosome_:

```python
[
 (1,0,0,1,1)|U,
 (0,0,0,0,0)|D,
 (0,0,1,0,-1)|L,
 ...
 (1,1,0,0,0)|P
 ]
```
* _reproduction_ - means that each of 5 best robots is cloned 8 times with small chromosome mutations. Fraction of mutation is given as a parameter i.e. `mess = 0.05`. 


### Hyperparameters to fun with:

* `population_size = 40` - number of robots in each generation,
* `n_boards = 100` - number of boards to passed by each robot.
* `mess = .05` - mutations in chromosome.
* `steps = 50` - number of steps.

### Additional questions to solve

* Probability of picking `p` out of total `k=15` cans from the board having `n` possible steps to do.
* Is GA better then random walking? How much better?
* What the performance will be with different type of mutation (deletions)


### When robot has 75 steps to use

Generation 101 | Generation 201  | Generation 281
:--------------------:|:--------------------:|:--------------------:
<img alt='a' src="https://raw.githubusercontent.com/katsob/evolution/master/2019-04-12T15:13:01steps=75_mess_perc=3/animations/epoch101.gif" width="300"  /> | <img alt='a' src="https://raw.githubusercontent.com/katsob/evolution/master/2019-04-12T15:13:01steps=75_mess_perc=3/animations/epoch201.gif" width="300"  /> | <img alt='a' src="https://raw.githubusercontent.com/katsob/evolution/master/2019-04-12T15:13:01steps=75_mess_perc=3/animations/epoch281.gif" width="300"  />


### When robot has 99 steps to use

Generation 101 | Generation 201  | Generation 281
:--------------------:|:--------------------:|:--------------------:
<img alt='a' src="https://raw.githubusercontent.com/katsob/evolution/master/2019-04-12T18:50:14steps=99_mess_perc=3/animations/epoch101.gif" width="300"  /> | <img alt='a' src="https://raw.githubusercontent.com/katsob/evolution/master/2019-04-12T18:50:14steps=99_mess_perc=3/animations/epoch201.gif" width="300"  /> | <img alt='a' src="https://raw.githubusercontent.com/katsob/evolution/master/2019-04-12T18:50:14steps=99_mess_perc=3/animations/epoch281.gif" width="300"  />