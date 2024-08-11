import seaborn as sns
import matplotlib.pyplot as plt

def plot_catplot_felony(pred_universe):
    """saves cat plot for the likelihood a felon would commit another felony
    
    Args: 
        pre_universe(dataframe): dataframe of prediction results
    """
    sns.catplot(data=pred_universe, 
                x='has_felony_charge', 
                y='prediction_felony', 
                kind='bar')
    plt.title('Felony Rearrest Prediction by Charge Degree')
    plt.savefig('data/part4_plots/catplot_felony.png', bbox_inches='tight')
    plt.close()

def plot_catplot_nonfelony(pred_universe):
    """saves cat plot for the likelihood a non-felon would commit another crime
    
    Args: 
        pre_universe(dataframe): dataframe of prediction results
    """
    sns.catplot(data=pred_universe, 
                x='has_felony_charge', 
                y='prediction_nonfelony', 
                kind='bar')
    plt.title('Non-Felony Rearrest Prediction by Charge Degree')
    plt.savefig('data/part4_plots/catplot_nonfelony.png', bbox_inches='tight')
    plt.close()
print('the difference in the plots can be explained by the longer terms for felonies.' +
      ' Misdomeanors can carry no time so those individuals have a chance of commiting another crime' + 
      ' while the felony individuals are in jail.')

def plot_catplot_felony_with_hue(pred_universe):
    """saves cat plot for the likelihood a felon would commit another felony with hue
    
    Args: 
        pre_universe(dataframe): dataframe of prediction results
    """
    sns.catplot(data=pred_universe, 
                x='has_felony_charge', 
                y='prediction_felony', 
                hue='y_felony', 
                kind='bar')
    plt.title('Felony Rearrest Prediction by Charge Degree and Actual Felony Rearrest')
    plt.savefig('data/part4_plots/catplot_felony_hue.png', bbox_inches='tight')
    plt.close()


print('The prediction means that individuals that have committed a felony are more likely '+
      'to commit the same level crime. Meanwhile, misdemeanor charges are a grade below '+ 
      'a felony charge. This means they would have to commit a worse crime.')