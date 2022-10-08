import math
from problem import *


def expand(problem, node):
    "Generates nodes one by one"
    s = node.state
    for action in problem.actions(s):
        s1 = problem.result(s, action)
        path_cost = node.path_cost + problem.action_cost(s, action)
        yield Node(s1, node, action, path_cost)


def iterative_deepening_search(problem):
    "bounded depth first search with increasing bound"
    depth = 1
    while True:
        result = depth_limited_search(problem, depth)
        depth += 1

        if result != "cutoff":
            return result


def depth_limited_search(problem, depth):
    frontier = list([Node(problem.initial)])
    result = "failure"

    while frontier:
        node = frontier.pop()
        if problem.is_goal(node.state):
            return node
        if node.path_cost >= depth:
            result = "cutoff"
        elif not is_cycle(node):
            for child in expand(problem, node):
                frontier.append(child)

    return result


def is_cycle(node):
    "checks the parents to see if the new node is a cycle"
    if node.parent is None:
        return False
    if node.parent.state == node.state:
        return True
    return is_cycle(node.parent)
