import plotly.express as px
from die import Die

die = Die(8)
die1 = Die(8)
results = []

for roll_num in range(50_000):
    result = die.roll() + die1.roll()
    results.append(result)
    
frequencies = []
max_result = die.num_sides + die1.num_sides
poss_results = range(2, max_result+1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "Results of 50,000 die rolls"
labels = {'x': 'Results', 'y': 'average of which result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

fig.update_layout(xaxis_dtick=1)

fig.show()
