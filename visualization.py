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
    plt.figure(figsize=(20, 15))
    plt.title(title, size=20)
    patches, texts, autotexts = plt.pie(y, labels=x, colors=c, autopct='%1.1f%%', shadow=True, startangle=140)

    # Improve legend placement
    plt.legend(patches, x, loc="best", fontsize=12, bbox_to_anchor=(1.2, 0.5), title="Countries", title_fontsize='14')

    for text, autotext in zip(texts, autotexts):
        text.set_size(12)
        autotext.set_size(12)

    plt.show()

#Unique countries for confirmed cases , deaths, recovery and active cases
unique_countries =  list(cases['Country'].unique())
unique_countries1 = list(cases['Country'].unique())
unique_countries2 = list(cases['Country'].unique())
unique_countries3 = list(cases['Country'].unique())

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

no_cases1 =[]
for i in unique_countries1:
    cases2 = cases[cases['Country']==i]['Deaths'].sum()
    if cases2 > 0:
        country_death_cases.append(cases2)
    else:
        no_cases1.append(i)
        
for i in no_cases1:
    unique_countries1.remove(i)

no_cases2 =[]
for i in unique_countries2:
    cases3 = cases[cases['Country']==i]['Recovered'].sum()
    if cases3 > 0:
        country_recovered_cases.append(cases3)
    else:
        no_cases2.append(i)
        
for i in no_cases2:
    unique_countries2.remove(i)

no_cases3 =[]
for i in unique_countries3:
    cases4 = cases[cases['Country']==i]['Active'].sum()
    if cases4 > 0:
        country_active_cases.append(cases4)
    else:
        no_cases3.append(i)
        
for i in no_cases3:
    unique_countries3.remove(i)

# sort countries by the number of confirmed cases
unique_countries = [k for k, v in sorted(zip(unique_countries, country_confirmed_cases), key=operator.itemgetter(1), reverse=True)]
for i in range(len(unique_countries)):
    country_confirmed_cases[i] = cases[cases['Country']==unique_countries[i]]['Confirmed'].sum()


#sort countries by the number of confirmed deaths
unique_countries1 = [k for k, v in sorted(zip(unique_countries1, country_death_cases), key=operator.itemgetter(1), reverse=True)]
for i in range(len(unique_countries1)):
    country_death_cases[i] = cases[cases['Country']==unique_countries1[i]]['Deaths'].sum()

#sort countries by the number of recoveries
unique_countries2 = [k for k, v in sorted(zip(unique_countries2, country_recovered_cases), key=operator.itemgetter(1), reverse=True)]
for i in range(len(unique_countries2)):
    country_recovered_cases[i] = cases[cases['Country']==unique_countries2[i]]['Recovered'].sum()

#sort countries by the number of active cases
unique_countries3 = [k for k, v in sorted(zip(unique_countries3, country_active_cases), key=operator.itemgetter(1), reverse=True)]
for i in range(len(unique_countries3)):
    country_active_cases[i] = cases[cases['Country']==unique_countries3[i]]['Active'].sum()

#Visualizing list of different cases
visual_confirmed_cases = []
visual_confirmed_deaths = []
visual_confirmed_active =[]
visual_confirmed_recovered=[]

#Other countries apart from the highest selected ones
others = np.sum(country_confirmed_cases[10:])
others1 = np.sum(country_death_cases[10:])
others2 = np.sum(country_recovered_cases[10:])
others3 = np.sum(country_active_cases[10:])


visual_unique_countries = [] 
for i in range(len(country_confirmed_cases[:10])):
    visual_unique_countries.append(unique_countries[i])
    visual_confirmed_cases.append(country_confirmed_cases[i])

visual_unique_countries1 = [] 
for i in range(len(country_death_cases[:10])):
    visual_unique_countries1.append(unique_countries1[i])
    visual_confirmed_deaths.append(country_death_cases[i])


visual_unique_countries2 = [] 
for i in range(len(country_recovered_cases[:10])):
    visual_unique_countries2.append(unique_countries2[i])
    visual_confirmed_recovered.append(country_recovered_cases[i])


visual_unique_countries3 = [] 
for i in range(len(country_active_cases[:10])):
    visual_unique_countries3.append(unique_countries3[i])
    visual_confirmed_active.append(country_active_cases[i])

#appending other cases than the top 10
visual_unique_countries.append('Others')
visual_confirmed_cases.append(others)
visual_unique_countries1.append('Others')
visual_confirmed_deaths.append(others1)
visual_unique_countries2.append('Others')
visual_confirmed_recovered.append(others2)
visual_unique_countries3.append('Others')
visual_confirmed_active.append(others3)
    

#bar and pie graph for confirmed cases
plot_bar_graphs(visual_unique_countries, visual_confirmed_cases, 'No. of Covid-19 Confirmed Cases in Countries')
plot_pie_charts(visual_unique_countries, visual_confirmed_cases, 'Covid-19 Confirmed Cases per Country')

#bar and pie chart for deaths
plot_bar_graphs(visual_unique_countries1, visual_confirmed_deaths, 'No. of Covid-19 Confirmed Deaths in Countries')
plot_pie_charts(visual_unique_countries1, visual_confirmed_deaths, 'Covid-19 Confirmed Deaths per Country')

#bar and pie chart for recovered cases
plot_bar_graphs(visual_unique_countries2, visual_confirmed_recovered, 'No. of Covid-19 Recovered cases in Countries')
plot_pie_charts(visual_unique_countries2, visual_confirmed_recovered, 'Covid-19 Recovered cases per Country')

#bnar and pie chart for active cases
plot_bar_graphs(visual_unique_countries3, visual_confirmed_active, 'No. of Covid-19 Active Cases in Countries')
plot_pie_charts(visual_unique_countries3, visual_confirmed_active, 'Covid-19 Active cases per Country')
