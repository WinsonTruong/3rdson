# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# # EDA
# Given that our data has been precompiled and cleaned, it is an excellent candidate for EDA!
# 

# %%
# Set Up
import pandas as pd
import numpy as np

# Graphing
import matplotlib
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('fivethirtyeight')
plt.rcParams['figure.figsize'] = (10,10)
import seaborn as sns
import plotly.express as px

# These lines make warnings look nicer
import warnings
warnings.simplefilter('ignore', FutureWarning)

# %% [markdown]
# # Loading Data
# The following data comes from the 2010 US Census and contains n = 236,459 entries each representing homosexual married couples with the following attributes:
# * _at least_ two children
# * a father who has worked in the previous year
# * a mother between 21 and 35

# %%
sample = pd.read_csv('../data/sample.csv')
sample.head()


# %%
sample.columns.to_list()

# %% [markdown]
# # Let's begin visualizing motherly, fatherly, and family earnings

# %%
plt.figure(figsize = (3, 6))
sns.boxplot(sample['famearn'], orient = 'v')


# %%
sns.jointplot(data = sample, x = 'earningsm', y = 'earningsd', kind = 'kde')
plt.suptitle('Contour Plot of Motherly and Fatherly Earnings with a Gaussian Kernel', y = 1.05);


# %%
sns.jointplot(data = sample, x = 'earningsm', y = 'earningsd', kind = 'hex')
plt.suptitle('Hex of Motherly and Fatherly Earnings with a Gaussian Kernel');

# %% [markdown]
# Both of these plots are not a very easy to read due to many motherly earnings being 0. Let's remove the scatter/hex binning to just observe the univariate distributions.

# %%
sns.distplot(sample['earningsd'], label = 'father')
sns.distplot(sample['earningsm'], label = 'mother')
plt.title('Distributions of Motherly and Fatherly Earnings')
plt.xlabel('Earnings in USD')
plt.legend();

# %% [markdown]
# This makes sense from what we plotted above in the jointplots. Motherly earnings are skewed quite heavily to the right due to the phenomena that most mothers are the homemakers in the family. The father's tend to follow more normal-like observation. Let's consider what a log transformation would do on the families where both the mother and father are working.

# %%
working_subset = sample[(sample['earningsm'] > 0) & (sample['earningsd'] > 0)]

sns.distplot(np.log(working_subset['earningsd']), label = 'father')
sns.distplot(np.log(working_subset['earningsm']), label = 'mother')
plt.title('Distributions of Motherly and Fatherly Log Earnings where Both Parents are Working ')
plt.xlabel('Earnings in Log Wage')
plt.legend();

# %% [markdown]
# This is much easier to read. We can see that father's tend to make more which enforces the patriarchial stereotypes that men are the "breadwinners" of a household. Let's see what our jointplot looks like now.

# %%

working_subset['logearnings_m'] = np.log(working_subset['earningsm'])
working_subset['logearnings_d'] = np.log(working_subset['earningsd'])

sns.jointplot(data = working_subset, x = 'logearnings_m', y = 'logearnings_d', kind = 'kde')
plt.suptitle('Contour Plot of Motherly and Fatherly Logearnings with a Gaussian Kernel', y = 1.05);


# %%
sns.jointplot(data = working_subset, x = 'logearnings_m', y = 'logearnings_d', kind = 'hex', color = 'g')
plt.suptitle('Hex Plot of Motherly and Fatherly Logearnings with a Gaussian Kernel', y = 1.05);

# %% [markdown]
# After some cleaning these jointplots are much easier to interpret. Key obsevations
# * The most common combination of earnings seem to be mothers that make near 10 log wage points and fathers that make 11 wage points.
# %% [markdown]
# # Let's consider the effect of having more kids on family earnings as a whole.

# %%
morekids_subsample = sample[sample['morekids'] == 1]


# %%
sns.distplot(np.log(morekids_subsample['famearn']), label = 'More than 2 Children', color = 'orange')
sns.distplot(np.log(sample['famearn']), label = '2 or Less Children', color = 'lightgreen')
plt.title('Differences in Earnings Between the Amount of Children')
plt.legend();


# %%



