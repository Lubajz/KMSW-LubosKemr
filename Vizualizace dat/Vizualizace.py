import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import numpy as np

# Načtění CSV datového modelu
csv_path = r'C:\Users\lubos\OneDrive\Dokumenty\Škola\KMSW\PopulationDataNew.csv'
csvreader = pd.read_csv(csv_path, sep=';')
plt.figure(figsize=(20, 10))  # Nastavení defaultní velikosti okna

def formatter(axis, pos):
    return '{:,.0f}'.format(axis)

def barChart(year, sub_rows, sub_col, sub_index):
    # Filtrování dat podle roku 
    data = csvreader[csvreader['Year'] == year]

    # Převedení pole na numerické
    data['Total Population'] = data['Total Population'].astype(str).str.replace(',', '').astype(float)

    # Seřazení dat dle celkové populace
    data_sorted = data.sort_values(by='Total Population', ascending=False)

    #Přidání "podgrafu", pozice a velikost je určena proměnnými sub_rows, sub_col a sub_index
    plt.subplot(sub_rows, sub_col, sub_index)
    
    #Výběr top 10 zemí, které mají nejvyšší počet obyvatel
    top_10_data = data_sorted.head(10)
    
    #Vytvoření barového grafu a určení osy x a y
    plt.bar(top_10_data['Country'], top_10_data['Total Population'])
    #Nastavení nadpisů
    plt.xlabel('Country')
    plt.ylabel('Total Population')
    plt.title(f'Top 10 countries with highest population in {year}')
    plt.xticks(rotation=90)  # Rotace osy x k lepšímu přečtení delších hodnot
    plt.ticklabel_format(style='plain', axis='y')
    #Formátování hodnot osy y
    plt.gca().get_yaxis().set_major_formatter(ticker.FuncFormatter(formatter))

def lineChart(sub_rows, sub_col, sub_index):

    data_filtered = csvreader[(csvreader['Year'] >= 2018) & (csvreader['Year'] <= 2021)]

    data_filtered['Total Population'] = data_filtered['Total Population'].str.replace(',', '').astype(float)

    country_population = data_filtered.groupby('Country')['Total Population'].sum()

    top_10_countries = country_population.nlargest(10).index.tolist()

    plt.subplot(sub_rows, sub_col, sub_index)

    for country in top_10_countries:
        country_data = data_filtered[data_filtered['Country'] == country]
        plt.plot(country_data['Year'],country_data['Fertility Rate'], label=country)


    plt.xlabel('Year')
    plt.ylabel('Fertility Rate')
    plt.title(f'Fertility Rate for Top 10 Countries (2018-2021)')
    plt.ticklabel_format(style='plain', axis='y')
    plt.gca().get_yaxis().set_major_formatter(ticker.FuncFormatter(formatter))
    plt.xticks(range(2018, 2022))
    #Pozice legendy
    plt.legend(loc='upper right')


def pieChart(year, sub_rows, sub_col, sub_index):
    data_filtered = csvreader[csvreader['Year'] == year]

    data_filtered['Urban Population'] = data_filtered['Urban Population'].str.replace(',', '').astype(float)
    data_filtered['Total Population'] = data_filtered['Total Population'].astype(str).str.replace(',', '').astype(float)

    data_sorted = data_filtered .sort_values(by='Urban Population', ascending=False)

    plt.subplot(sub_rows, sub_col, sub_index)
    top_10_data = data_sorted.head(10)

    top_10_data['Urban Percentage'] = (top_10_data['Urban Population'] / top_10_data['Total Population']) * 100
    labels = [f"{country} - {percentage:.1f}%" for country, percentage in zip(top_10_data['Country'], top_10_data['Urban Percentage'])]
    plt.pie(top_10_data['Urban Percentage'],labels=labels, startangle=140)
    # Nastavení stejného poměru v koláčovém grafu
    plt.axis('equal')
    plt.title(f'Distribution of Urban Population in Top 10 Countries in {year}')


def scatter(year, country, sub_rows, sub_col, sub_index):
    data_filtered = csvreader[csvreader['Year'] == year]

    data_filtered['Total Population'] = data_filtered['Total Population'].str.replace(',', '').astype(float)

    data_sorted = data_filtered .sort_values(by='Total Population', ascending=False)

    plt.subplot(sub_rows, sub_col, sub_index)
    # Seznam barev pro jednotlivé země
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k','tab:orange', 'tab:purple', 'tab:brown']

    top_10_data = data_sorted.head(10)
    for i, (_, country_data) in enumerate(top_10_data.iterrows()):
        country = country_data['Country']
        x_value = country_data['Birth Rate']
        y_value = country_data['Death Rate']
        color = colors[i]
    # Přidání země do grafu dle jejích hodnot
        plt.scatter(x_value, y_value, color=color, label=country)

    plt.xlabel('Death Rate')
    plt.ylabel('Birth Rate')
    plt.title(f'Birth Rate vs Death Rate in {year}')
    plt.legend(loc='upper right')


def stacked(year, sub_rows, sub_col, sub_index):
    data_filtered = csvreader[csvreader['Year'] == year]

    data_filtered['Urban Population'] = data_filtered['Urban Population'].str.replace(',', '').astype(float)
    data_filtered['Rural Population'] = data_filtered['Rural Population'].str.replace(',', '').astype(float)
    data_filtered['Total Population'] = data_filtered['Total Population'].str.replace(',', '').astype(float)

    data_sorted = data_filtered.sort_values(by='Total Population', ascending=False)

    plt.subplot(sub_rows, sub_col, sub_index)
    top_10_data = data_sorted.head(10)

    # Vytvoření stacked grafu a nastavení jeho os a popisu. Alpha nastavuje průhlednost sloupců v grafu
    plt.barh(top_10_data['Country'], top_10_data['Urban Population'],label='Urban Population', alpha=0.7)
    plt.barh(top_10_data['Country'], top_10_data['Rural Population'],label='Rural Population', alpha=0.7, left=top_10_data['Urban Population'])

    plt.xlabel('Population')
    plt.ylabel('Country')
    plt.title(f'Urban vs. Rural Population in Top 10 Countries in {year}')
    plt.xticks(rotation=90)
    plt.legend(loc = 'upper right')
    plt.gca().get_xaxis().set_major_formatter(ticker.FuncFormatter(formatter))

   

barChart(2019, 2, 3, 1)
barChart(2021, 2, 3, 2)
lineChart(2,3,3)
pieChart(2020, 2, 3, 4)
scatter(2019, 'China', 2, 3, 5)
stacked(2021, 2, 3, 6)

#Nastavení layoutu, aby nedošlo k překrytí podgrafů
plt.tight_layout() 
plt.show()
