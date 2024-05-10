from random import choice


class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            stepx = self.get_step()
            stepy = self.get_step()
            x = self.x_values[-1] + stepx
            y = self.y_values[-1] + stepy
            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        """Calculate a single step in the walk."""
        direction = choice([-1, 1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance

        return step