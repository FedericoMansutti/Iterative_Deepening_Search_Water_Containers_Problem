class WaterProblem:

    def __init__(self, initial, goal):
        "sets the inital and goal state of the problem"
        self.initial = initial
        self.goal = goal

    def is_goal(self, s):
        "comapares the water value of the containers against the goal"
        if s[0]==self.goal or s[1]==self.goal or s[2]==self.goal:
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

