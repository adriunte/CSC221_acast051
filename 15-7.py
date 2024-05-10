import plotly.express as px
from die import Die

die = Die()
die1 = Die()
die2 = Die()
results = []

for roll_num in range(50_000):
    result = die.roll() + die1.roll() + die2.roll()
    results.append(result)

averages = []
max_result = die.num_sides + die1.num_sides + die2.num_sides
poss_results = range(3, max_result+1)

for value in poss_results:
    average = results.count(value) / len(results)
    averages.append(average)

title = "Results of 50,000 die rolls"
x_label = "Results"
y_label = "Average of each Result"
fig = px.bar(x=poss_results, y=averages, title=title, labels={'x': x_label, 'y': y_label})
fig.update_layout(xaxis_dtick=1)

fig.show()
