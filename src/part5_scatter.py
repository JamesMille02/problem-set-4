import seaborn as sns
import matplotlib.pyplot as plt

def plot_scatter_felony_vs_nonfelony(pred_universe):
    """saves scatter plot for the likelihood a felon and misdemeanor would commit each crime again
    
    Args: 
        pre_universe(dataframe): dataframe of prediction results
    """
    sns.lmplot(data=pred_universe, 
               x='prediction_felony', 
               y='prediction_nonfelony', 
               hue='has_felony_charge', 
               aspect=1.5)
    plt.title('Scatter Plot of Felony vs Non-Felony Rearrest Predictions')
    plt.savefig('data/part5_plots/scatter_felony_vs_nonfelony.png', bbox_inches='tight')
    plt.close()
    print('the group on the right have commited a felony and are more likely to '+
          'commit another felony but less likey to commit a misdomeanor comparitavely.')



def plot_scatter_prediction_vs_actual(pred_universe):
    """saves cat plot for to compare the predicted values and actual values for rearrest 
    
    Args: 
        pre_universe(dataframe): dataframe of prediction results
    """
    sns.scatterplot(data=pred_universe, 
                    x='prediction_felony', 
                    y='y_felony')
    plt.title('Scatter Plot of Felony Rearrest Prediction vs Actual Rearrest')
    plt.savefig('data/part5_plots/scatter_prediction_vs_actual.png', bbox_inches='tight')
    plt.close()
    print('the plot is not calibrated because it is not understandable. The possible '+\
          'values are 1 and 0 so all the dots are on the top and bottom. This makes the graph not understandable' +
          'to calibrate the graph you could do the number of rearrests and it may be better '+ 
          'but with the current setup it is unreadable')

