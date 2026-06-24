from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    recall_score,
)


def evaluate_model(model, X_test, y_test, target_names=None):
    # model se prediction karwao (jo data train mein nahi dekha)
    y_pred = model.predict(X_test)

    # 1) overall accuracy — kitne % sahi
    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {acc * 100:.2f}%\n")

    # 2) per-class report
    print("Per-class report:")
    print(classification_report(y_test, y_pred, target_names=target_names))

    return y_pred


def get_per_class_recall(model, X_test, y_test, target_names=None):
    #Sirf har class ka recall nikaalo (SMOTE before/after compare ke liye
    y_pred = model.predict(X_test)

    # average=None -> har class ka alag recall (ek number nahi, list)
    recalls = recall_score(y_test, y_pred, average=None)

    # naam ke saath dikhao (taaki samajh aaye konsa class)
    print("Per-class Recall:")
    names = target_names if target_names else range(len(recalls))
    for name, r in zip(names, recalls):
        print(f"  {name}: {r:.2f}")

    return recalls


def compare_smote(model_normal, model_smote, X_test, y_test, target_names=None):
    #SMOTE se PEHLE aur BAAD ka recall side-by-side dikhao.
    print("=" * 45)
    print("SMOTE EFFECT (per-class recall)")
    print("=" * 45)

    # dono models ke predictions
    pred_before = model_normal.predict(X_test)
    pred_after = model_smote.predict(X_test)

    # dono ka per-class recall
    recall_before = recall_score(y_test, pred_before, average=None)
    recall_after = recall_score(y_test, pred_after, average=None)

    # side-by-side table
    names = target_names if target_names else range(len(recall_before))
    print(f"\n{'Class':<25} {'Before':>8} {'After':>8} {'Change':>8}")
    print("-" * 42)
    for name, b, a in zip(names, recall_before, recall_after):
        change = a - b   # kitna badha/ghata
        arrow = "↑" if change > 0 else ("↓" if change < 0 else "=")
        print(f"{str(name):<25} {b:>8.2f} {a:>8.2f} {change:>+7.2f}{arrow}")