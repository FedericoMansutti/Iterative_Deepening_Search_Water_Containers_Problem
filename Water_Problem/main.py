from problem import *
from search import *

problem = Problem([12, 8, 3], 10)
print(path_states(iterative_deepening_search(problem)))
print(path_actions(iterative_deepening_search(problem)))
