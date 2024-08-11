'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def seaborn_settings():
    '''
    Applies the default seaborn theme and sets the default figure size
    '''
    sns.set_theme()
    sns.set(rc={'figure.figsize':(6, 4)})

# 1. Using the pre_universe data frame, create a bar plot for the fta column.
def plot_fta_bar(pre_universe):
    """saves bar plot for fta column
    
    Args: 
        pre_universe(dataframe): dataframe of prediction results
    """
    plt.figure(figsize=(10, 6))
    sns.countplot(x='fta', data=pre_universe)
    plt.title('Bar Plot of FTA')
    plt.xlabel('FTA')
    plt.ylabel('Count')
    plt.savefig('data/part3_plots/fta_bar_plot.png')
    plt.close()

# 2. Hue the previous barplot by sex
def plot_fta_bar_hue(pre_universe):
    """saves bar plot for sex with hue
    
    Args: 
        pre_universe(dataframe): dataframe of prediction results
    """
    plt.figure(figsize=(10, 6))
    sns.countplot(x='fta', hue='sex', data=pre_universe)
    plt.title('Bar Plot of FTA by Sex')
    plt.xlabel('FTA')
    plt.ylabel('Count')
    plt.savefig('data/part3_plots/fta_bar_plot_hue.png')
    plt.close()


# 3. Plot a histogram of age_at_arrest
def plot_age_histogram(pre_universe):
    """saves bar plot for age at arrest
    
    Args: 
        pre_universe(dataframe): dataframe of prediction results
    """
    plt.figure(figsize=(10, 6))
    plt.hist(pre_universe['age_at_arrest'].dropna(), bins=30, edgecolor='k')
    plt.title('Histogram of Age at Arrest')
    plt.xlabel('Age at Arrest')
    plt.ylabel('Frequency')
    plt.savefig('data/part3_plots/age_histogram.png')
    plt.close()

# 4. Plot the same histogram, but create bins that represent the following age groups 
#  - 18 to 21
#  - 21 to 30
#  - 30 to 40
#  - 40 to 100 

def plot_age_histogram_custom_bins(pred_universe):
    """saves bar plot for ages with custom bins
    
    Args: 
        pre_universe(dataframe): dataframe of prediction results
    """
    sns.reset_defaults()
    seaborn_settings()

    sns.histplot(data=pred_universe, 
                 x='age_at_arrest', 
                 bins=[18, 21, 30, 40, 100])
    plt.savefig('./data/part3_plots/age_histogram_specific_bins.png', bbox_inches='tight')

    plt.close()