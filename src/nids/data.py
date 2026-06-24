"""
data.py
Saari CSV files ko load karke ek bade table mein concatinate krta hai.
"""
import pandas as pd
from . import config

def load_data():
    #saari csv file load krke ek combine table banao
    parts=[]

    for name,path in config.DATA_FILES.items():
        temp=pd.read_csv(path,nrows=config.SAMPLE_ROWS)
        parts.append(temp)
    df=pd.concat(parts, ignore_index=True)
    print(f"Table Shape:{df.shape}")
    return df
