import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
cubes = [1, 8, 27, 64, 125]

plt.style.use('seaborn-v0_8')
one, two = plt.subplots()

two.scatter(x, cubes, s=80)
two.set_title("Cubes", fontsize=20)
two.set_xlabel('Value', fontsize=15)
two.set_ylabel('Cube of Value', fontsize=15)
two.tick_params(axis='both', labelsize=15)

plt.show()

xx = range(1, 5001)
yy = [x**3 for x in xx]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.scatter(xx, yy, c=yy, cmap=plt.cm.Blues, s=50)
ax.set_title("Cubes", fontsize=20)
ax.set_xlabel('Value', fontsize=15)
ax.set_ylabel('Cube of Value', fontsize=15)
ax.tick_params(axis='both', labelsize=15)

plt.show()