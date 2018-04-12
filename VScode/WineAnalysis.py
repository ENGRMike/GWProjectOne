#imports
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

wine_data = pd.read_csv('winemag-data-130k-v2.csv')

#wines we are searching for
white_wines = ['Riesling','Sauvignon Blanc','White Blend','Chardonnay']
red_wines = ['Merlot', 'Sangiovese', 'Red Blend', 'Pinot Noir']

white_data = wine_data.loc[wine_data['variety'].isin(white_wines)]
red_data = wine_data.loc[wine_data['variety'].isin(red_wines)]
top_range = 95

top_white_wines = white_data[white_data['points'] >= top_range]
top_red_wines = red_data[red_data['points'] >= top_range]
top_wines = wine_data[wine_data['points'] >= top_range]

sns.lmplot(x='price',y='points', data = white_data, hue = 'variety', fit_reg = False, scatter_kws={'alpha':0.6}, legend=False)
plt.legend(loc='upper right')
plt.title('White Wine Rating vs. Price')
plt.savefig('White_Wines.png', bbox_inches='tight')
plt.clf()

sns.lmplot(x='price',y='points', data = red_data, hue = 'variety', fit_reg = False, scatter_kws={'alpha':0.6}, legend=False)
plt.legend(loc='lower right')
plt.title('Red Wine Rating vs. Price')
plt.savefig('Red_Wines.png', bbox_inches='tight')
plt.clf()

top_white_plot = sns.stripplot(x='country', y = 'points', data = top_white_wines, jitter = True)
top_white_plot.set_title('White Wine Quality vs. Country')
top_white_plot.set_xticklabels(top_white_plot.get_xticklabels(), rotation = 90)
plt.savefig('White_points_Country.png', bbox_inches='tight')
plt.clf()

price_white_plot = sns.stripplot(x='country', y = 'price', data = top_white_wines)
price_white_plot.set_title('White Wine Price vs. Country')
price_white_plot.set_xticklabels(price_white_plot.get_xticklabels(), rotation = 90)
plt.savefig('White_price_Country.png', bbox_inches='tight')
plt.clf()

top_red_plot = sns.stripplot(x='country', y = 'points', data = top_red_wines, jitter = True)
top_red_plot.set_title('Red Wine Quality vs. Country')
top_red_plot.set_xticklabels(top_red_plot.get_xticklabels(), rotation = 90)
plt.savefig('Red_points_Country.png', bbox_inches='tight')
plt.clf()

price_red_plot = sns.stripplot(x='country', y = 'price', data = top_red_wines)
price_red_plot.set_title('Red Wine Price vs. Country')
price_red_plot.set_xticklabels(price_red_plot.get_xticklabels(), rotation = 90)
plt.savefig('red_price_Country.png', bbox_inches='tight')
plt.clf()

top_countries_plot = sns.countplot(x='country', data = top_wines)
top_countries_plot.set_xticklabels(top_countries_plot.get_xticklabels(), rotation = 90)
top_countries_plot.set_title(f'Total Wines rated over {top_range} per country')
plt.savefig('top_countries.png', bbox_inches='tight')