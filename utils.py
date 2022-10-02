'''
    These are function/class definitions that were created in the EDA notebook, then moved here so that
    the deployment file can have access to these definitions as well for unpickling purposes.
'''

import numpy as np
import pandas as pd

class Pipeline:
    '''
        This class holds a sequence of functions to transform data so a user can apply the same sequence
        to multiple batches of data easily.
    '''
    def __init__(self, *funcs):
        '''
            Desc:
                Takes in a list of functions & applies them to any pd.DataFramem passed
                in through the __call__ method.
            Args:
                *funcs: A list of functions
        '''
        self.funcs = list([func.__name__, func] for func in funcs)

    def __call__(self, dataframe):
        for funcname, func in self.funcs:
            print("Applying func", funcname)
            dataframe = func(dataframe)
        return dataframe

    def add(self, func):
        self.funcs.append( (func.__name__, func) )

    def __str__(self):
        return "Pipeline: " + ', '.join(funcname for funcname, _ in self.funcs)

class RegressionModel:
    '''
        This class is meant to provide a common interface between regression and classification
        models by converting regression models to classification models when the regression
        is over a certain threshold. This is so both models can be called with the model.predict
        interface & return binary values.
    '''
    def __init__(self, model, threshold):
        self.model = model
        self.threshold = threshold

    def predict(self, X):
        y = self.model.predict(X)
        y = y > self.threshold
        return y

def make_months_circular(df):
    months_map = dict(
        zip(
            ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            np.linspace(0,2*np.pi-2*np.pi/12,12)
        )
    )
    months_radian = df['Month'].apply(lambda month : months_map[month])
    months_x, months_y = np.cos(months_radian), np.sin(months_radian)
    df_updated = df.drop('Month', axis=1)
    df_updated['Month_x'] = months_x
    df_updated['Month_y'] = months_y
    return df_updated

def make_data_categorical(df):
    df[['OperatingSystems', 'Browser', 'Region', 'TrafficType', 'VisitorType']] = df[['OperatingSystems', 'Browser', 'Region', 'TrafficType', 'VisitorType']].astype('category')
    return df

def consolidate_session_data(df):
    updated_df = df.drop(['Administrative', 'Informational', 'ProductRelated','Administrative_Duration', 'Informational_Duration', 'ProductRelated_Duration'], axis=1)
    updated_df['total_time'] = df[['Administrative_Duration', 'Informational_Duration', 'ProductRelated_Duration']].sum(axis=1)
    return updated_df

def remove_computer_data(df):
    return df.drop(['OperatingSystems', 'Browser'], axis=1)
