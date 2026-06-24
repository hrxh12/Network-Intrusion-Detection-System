"""
train.py
Models train karta hai: Random Forest, XGBoost, aur SMOTE-balanced version.
"""
from sklearn.ensemble import RandomForestClassifier    # Random Forest
from sklearn.model_selection import train_test_split   # data baatne ka tool
from xgboost import XGBClassifier                       # XGBoost model
from imblearn.over_sampling import SMOTE                # rare class balance
from . import config                                    # settings

def split_data(X,y):
     return train_test_split(
        X, y,
        test_size=config.TEST_SIZE,
        random_state=config.RANDOM_STATE,
        stratify=y,                  # har class ka ratio dono mein same
    )

def train_random_forest(X_train, y_train):
    """Random Forest model train karo."""
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=config.RANDOM_STATE,
        n_jobs=-1,
    )
    model.fit(X_train, y_train)
    return model

def train_xgboost(X_train, y_train):
    """XGBoost model train karo (Random Forest se compare ke liye)."""
    model = XGBClassifier(
        n_estimators=100,
        random_state=config.RANDOM_STATE,
        n_jobs=-1,
        eval_metric='logloss',
    )
    model.fit(X_train, y_train)
    return model

def train_with_smote(X_train, y_train):
    # 1) SMOTE: rare classes ke naqli (synthetic) examples banao
    #    DHYAN: sirf TRAIN data pe — test asli rakho
    smote = SMOTE(random_state=config.RANDOM_STATE)
    X_bal, y_bal = smote.fit_resample(X_train, y_train)

    # 2) balanced data pe Random Forest train karo
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=config.RANDOM_STATE,
        n_jobs=-1,
    )
    model.fit(X_bal, y_bal)
    return model