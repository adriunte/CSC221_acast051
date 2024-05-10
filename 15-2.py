import matplotlib.pyplot as plt

x = range(1, 5001)
y = [x**3 for x in x]

plt.style.use('seaborn-darkgrid')

one, two = plt.subplots() 

two.scatter(x, y, c=y, cmap=plt.cm.Blues, s=25) 
two.set_title("Cubes", fontsize=20)
two.set_xlabel('Value', fontsize=15)
two.set_ylabel('Cube of Value', fontsize=15)

two.tick_params(axis='both', labelsize=15)

plt.show()