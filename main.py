from helper.models import *
from helper.processing import *
import pandas as pd
import numpy as np
import os



def read_data(path):
    """
    
    """

    data_df = pd.read_csv(path)
    return data_df




if __name__ == "__main__":

    #read the data
    DATA_PATH = os.path.abspath('./Data') + '/train_demo_subset.csv'

    data = read_data(DATA_PATH)
    print(data)

