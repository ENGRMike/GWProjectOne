#imports
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

wine_data = pd.read_csv('winemag-data-130k-v2.csv')

#wines we are searching for
target_wines = ['Pinot Noir','Riesling','Sauvignon Blanc','Sangiovese','White Blend','Red Blend','Merlot','Chardonnay']
white_wines = ['Riesling','Sauvignon Blanc','White Blend','Chardonnay']
red_wines = ['Merlot', 'Sangiovese', 'Red Blend', 'Pinot Noir']

# for wine in white_wines:
#     # data = wine_data[wine_data['variety'] == wine]
#     # sns.lmplot(x='price', y = 'points', data = data, fit_reg = False)
#     # plt.grid()
#     # plt.title(f'{wine} price vs rating')
#     # plt.savefig(f'{wine}points.png')

white_data = wine_data.loc[wine_data['variety'].isin(white_wines)]
red_data = wine_data.loc[wine_data['variety'].isin(red_wines)]

# plt.rcParams['figure.figsize'] = 10,10
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.lmplot(x='price',y='points', data = white_data, hue = 'variety', fit_reg = False, scatter_kws={'alpha':0.4}, legend=False)
plt.legend(loc='upper right')
plt.tight_layout()
plt.title('White Wine Rating vs. Price')
plt.savefig('White_Wines.png', bbox_inches='tight')

sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.lmplot(x='price',y='points', data = red_data, hue = 'variety', fit_reg = False, scatter_kws={'alpha':0.4}, legend=False)
plt.legend(loc='lower right')
plt.tight_layout()
plt.title('White Wine Rating vs. Price')
plt.savefig('Red_Wines.png', bbox_inches='tight')