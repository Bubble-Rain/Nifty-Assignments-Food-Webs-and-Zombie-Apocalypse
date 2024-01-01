# Nifty-Assignments-Food-Webs-and-Zombie-Apocalypse
Implementation of http://nifty.stanford.edu/2022/stephenson-hudson-food-web-zombies/ both the Food Web and Zombies assignments. This was done by creating a more generic Directed Acyclic Graph with an accompnaying series of tests. Assignments required the main data structure to be a dictionary with key as the node and the connections as a list. The generic implementation assumed that the value list in the dictionary was the predecessors of the node. Thus for the Zombie implementation the DAG is actually inverted.

This assignment was used to implment the teachings from Part 1 of Grokking Simplicity. Namely the principles of Functional Programming and Stratified Design. Data is treated as immutable, side-effects managed, and splitting of functions into layers. Respectively Zombies.py and FoodWeb.py are treated as the Abstraction Barrier for stratified design purposes. Leaving it possible to use a different implementation of the DAG.

To use type in System console "python 'Main File' 'File Path of Input File' 'Implementation' ". Where the "Implementation" argument can be left default blank.
Main File: "zombie_main.py" or "foodWeb_main.py"
File Path of Input File: e.g. "foodwebFiles/AnotherFoodWeb.txt"
Implementation: "dDAG"
