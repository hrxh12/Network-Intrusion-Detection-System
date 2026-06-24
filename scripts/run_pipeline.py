import sys
from pathlib import Path

# src folder ko import-path mein daalo (taaki 'nids' package import ho)
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

# apne banaye functions import karo
from nids.data import load_data
from nids.features import clean_data, split_X_y
from nids.train import split_data, train_random_forest, train_with_smote
from nids.evaluate import evaluate_model, compare_smote
def main():
    print("NIDS Pipeline\n")

    # 1) data load karo (saari files jodo)
    df = load_data()

    # 2) clean karo + multi-class target (attack_code) banao
    df, le = clean_data(df)

    # 3) features (X) aur target (y) alag — multi-class
    X, y = split_X_y(df, target='attack_code')

    # 4) train/test mein baato
    X_train, X_test, y_train, y_test = split_data(X, y)

    # attack ke naam (number -> naam), report mein dikhane ke liye
    names = list(le.classes_)

    # 5) NORMAL model (bina SMOTE) train karo
    print("\n--- Random Forest (without SMOTE) ---")
    model_rf = train_random_forest(X_train, y_train)
    evaluate_model(model_rf, X_test, y_test, target_names=names)

    # 6) SMOTE model train karo
    print("\n--- Random Forest + SMOTE ---")
    model_smote = train_with_smote(X_train, y_train)
    evaluate_model(model_smote, X_test, y_test, target_names=names)

    # 7) DONO ka comparison — YAHI PROJECT KA MAIN POINT hai
    print()
    compare_smote(model_rf, model_smote, X_test, y_test, target_names=names)

    print("\n=== Pipeline complete! ===")


# file ko seedha chalाne pe hi main() chale (import pe na chale)
if __name__ == "__main__":
    main()