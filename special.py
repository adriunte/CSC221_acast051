import pandas as pd
import matplotlib.pyplot as plt


data_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
covid_data = pd.read_csv(data_url)
india_data = covid_data[covid_data['Country/Region'] == 'India']
india_cases = india_data.iloc[:, 4:].sum()
dates = pd.to_datetime(india_cases.index)

plt.figure(figsize=(10, 6))  
plt.plot(dates, india_cases, marker='o', linestyle='-') 
plt.title('Daily COVID-19 Cases in India')  
plt.xlabel('Date')  
plt.ylabel('Number of Cases') 
plt.grid(True)  
plt.xticks(rotation=45)  
plt.tight_layout()  

plt.savefig('special.png')
plt.show()