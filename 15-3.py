import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk(5000)
rw.fill_walk()

plt.style.use('seaborn-dark')

one, two = plt.subplots(figsize=(10, 6))

point_numbers = range(rw.num_points)
two.plot(rw.x_values, rw.y_values, linewidth=1)
two.set_aspect('equal')
two.scatter(0, 0, c='green', edgecolors='none', s=100)
two.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
two.get_xaxis().set_visible(False)
two.get_yaxis().set_visible(False)

plt.show()
