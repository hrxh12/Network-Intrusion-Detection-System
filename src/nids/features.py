"""
features.py
Data ko clean karke model ke layak banata hai
(bekaar columns hatana, target banana, X/y alag karna).
"""

from sklearn.preprocessing import LabelEncoder # text ko number mein badalne ka tool
from . import config 

def clean_data(df):
    #removing useless columns\
    df=df.drop(columns=config.DROP_COLUMNS,errors='ignore')
    le=LabelEncoder()
    df['attack_code']=le.fit_transform(df['Attack Name'])
    return df,le 

def split_X_y(df,target='Label'):
    # X = features: target aur text columns hata ke baaki sab number columns
    X=df.drop(columns=['Label','attack_code','Attack Name'])
    #y=Target
    y = df[target]

    return X,y

    