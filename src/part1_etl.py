'''
PART 1: ETL
- This code sets up the datasets for Problem Set 4
- NOTE: You will update this code for PART 4: CATEGORICAL PLOTS
'''

import pandas as pd

def extract_transform():
    """
    Extracts and transforms data from arrest records for analysis

    Returns:
        - `pred_universe`: The dataframe containing prediction-related data for individuals
        - `arrest_events`: The dataframe containing arrest event data
        - `charge_counts`: A dataframe with counts of charges aggregated by charge degree
        - `charge_counts_by_offense`: A dataframe with counts of charges aggregated by both charge degree and offense category
    """
    # Extracts arrest data CSVs into dataframes
    pred_universe = pd.read_csv('https://www.dropbox.com/scl/fi/a2tpqpvkdc8n6advvkpt7/universe_lab9.csv?rlkey=839vsc25njgfftzakr34w2070&dl=1')
    arrest_events = pd.read_csv('https://www.dropbox.com/scl/fi/n47jt4va049gh2o4bysjm/arrest_events_lab9.csv?rlkey=u66usya2xjgf8gk2acq7afk7m&dl=1')

    # Creates two additional dataframes using groupbys
    charge_counts = arrest_events.groupby(['charge_degree']).size().reset_index(name='count')
    charge_counts_by_offense = arrest_events.groupby(['charge_degree', 'offense_category']).size().reset_index(name='count')
    
    return pred_universe, arrest_events, charge_counts, charge_counts_by_offense

def create_felony_update(pred_universe, arrest_events):
    """creates the dataframes for the level of arrest and joins with predictive dataset.

    Args:
        pred_universe(dataframe): dataset of prediction result
        arrest_events(dataframe): dataset of the arrest information for each event used for the prediction

    Returns:
        felony_charge(dataframe): the dataset for the felony charges
        updated_pred(dataframe): dataset for updated prediction with the joined data so it has the arrest level information.
    """

    #gets the felony level arrests
    felony_charge = arrest_events.groupby('arrest_id')['charge_degree'].apply(lambda x: 1 if (x == 'felony').sum() > 0 else 0).reset_index(name='has_felony_charge')
    #creates merged df 
    updated_pred = pred_universe.merge(felony_charge, on='arrest_id', how='inner')
    
    return felony_charge, updated_pred
