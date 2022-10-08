class Problem:

    def __init__(self, initial, goal):
        "sets the inital and goal state of the problem"
        self.initial = initial
        self.goal = goal

    def is_goal(self, s):
        "comapares the water value of the containers against the goal"
        if s[0] == self.goal or s[1] == self.goal or s[2] == self.goal:
            return True
        return False

    def actions(self, s):
        "returns allowed actions in state s"
        allowed = []

        if s[0] < 12: allowed.append("Fill12")
        if s[1] < 8: allowed.append("Fill8")
        if s[2] < 3: allowed.append("Fill3")

        if s[0] > 0: allowed.append("Empty12")
        if s[1] > 0: allowed.append("Empty8")
        if s[2] > 0: allowed.append("Empty3")

        if s[0] > 0 and s[1] < 8: allowed.append("Pour12-8")
        if s[0] > 0 and s[1] < 3: allowed.append("Pour12-3")
        if s[1] > 0 and s[0] < 12: allowed.append("Pour8-12")
        if s[1] > 0 and s[2] < 3: allowed.append("Pour8-3")
        if s[2] > 0 and s[0] < 12: allowed.append("Pour3-12")
        if s[2] > 0 and s[1] < 8: allowed.append("Pour3-8")

        return allowed


    def result(self, s, a):
        "applies the action and returns the new state"
        if a == "Fill12": return [12, s[1], s[2]]
        elif a == "Fill8": return [s[0], 8, s[2]]
        elif a == "Fill3": return [s[0], s[1], 3]

        elif a == "Empty12": return [0, s[1], s[2]]
        elif a == "Empty8": return [s[0], 0, s[2]]
        elif a == "Empty3": return [s[0], s[1], 0]

        elif a == "Pour12-8": return [s[0] - min(s[0], 8 - s[1]), s[1] + min(s[0], 8 - s[1]), s[2]]
        elif a == "Pour12-3": return [s[0] - min(s[0], 3 - s[2]), s[1], s[2] + min(s[0], 3 - s[2])]
        elif a == "Pour8-12": return [s[0] + min(s[1], 12 - s[0]), s[1] - min(s[1], 12 - s[0]), s[2]]
        elif a == "Pour8-3": return [s[0], s[1] - min(s[1], 3 - s[2]), s[2] + min(s[1], 3 - s[2])]
        elif a == "Pour3-12": return [s[0] + min(s[2], 12 - s[0]), s[1], s[2] - min(s[2], 12 - s[0])]
        elif a == "Pour3-8": return [s[0], s[1] + min(s[2], 8 - s[1]), s[2] - min(s[2], 8 - s[1])]

    def action_cost(self, s, a):
        "each action: fill, pour, empty costs 1"
        return 1


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __len__(self):
        return 0 if self.parent is None else (1+len(self.parent))


def path_states(node):
    "returns the visited states in order"
    if node.parent is None:
        return []
    return path_states(node.parent) + [node.state]


def path_actions(node):
    "returns the performed actions in order"
    if node.parent is None:
        return []
    return path_actions(node.parent) + [node.action]
