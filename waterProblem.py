class WaterProblem:

    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def is_goal(self, s):
        ""
        for count, _ in enumerate(self.initial):
            if s[count] == 1:
                return True

        return False