import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.colors as mcolors
import pandas as pd 

import operator 
import warnings

warnings.filterwarnings("ignore")

cases = pd.read_csv('country_wise_latest.csv')

#function to plot the bar graph 
def plot_bar_graphs(x, y, title):
    plt.figure(figsize=(16, 12))
    plt.barh(x, y)
    plt.title(title, size=20)
    plt.xticks(size=20)
    plt.yticks(size=20)
    plt.show()

#function to plot pie chart
def plot_pie_charts(x, y, title):
    # more muted color 
    c = ['lightcoral', 'rosybrown', 'sandybrown', 'navajowhite', 'gold',
        'khaki', 'lightskyblue', 'turquoise', 'lightslategrey', 'thistle', 'pink']
    plt.figure(figsize=(20,15))
    plt.title(title, size=20)
    plt.pie(y, colors=c,shadow=True)
    plt.legend(x, loc='best', fontsize=12)
    plt.show()

#Unique countries for confirmed cases
unique_countries =  list(cases['Country'].unique())

country_confirmed_cases = []
country_death_cases = [] 
country_active_cases = []
country_recovered_cases = [] 


no_cases = []
for i in unique_countries:
    cases1 = cases[cases['Country']==i]['Confirmed'].sum()
    if cases1 > 0:
        country_confirmed_cases.append(cases1)
    else:
        no_cases.append(i)
        
for i in no_cases:
    unique_countries.remove(i)

# sort countries by the number of confirmed cases
unique_countries = [k for k, v in sorted(zip(unique_countries, country_confirmed_cases), key=operator.itemgetter(1), reverse=True)]
for i in range(len(unique_countries)):
    country_confirmed_cases[i] = cases[cases['Country']==unique_countries[i]]['Confirmed'].sum()

    
visual_confirmed_cases = []
visual_confirmed_deaths = []
visual_confirmed_active =[]
visual_confirmed_recovered=[]

#Other countries apart from the highest selected ones
others = np.sum(country_confirmed_cases[10:])

visual_unique_countries = [] 
for i in range(len(country_confirmed_cases[:10])):
    visual_unique_countries.append(unique_countries[i])
    visual_confirmed_cases.append(country_confirmed_cases[i])


visual_unique_countries.append('Others')
visual_confirmed_cases.append(others)


    
plot_bar_graphs(visual_unique_countries, visual_confirmed_cases, 'No. of Covid-19 Confirmed Cases in Countries')
plot_pie_charts(visual_unique_countries, visual_confirmed_cases, 'Covid-19 Confirmed Cases per Country')

