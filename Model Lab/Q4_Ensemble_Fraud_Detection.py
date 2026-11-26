import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Sample data: replace this with the actual insurance CSV when available.
data = pd.DataFrame({
    "vehicle_age": [2,5,8,3,10,4,7,1,9,6,2,8,5,3,10,4,7,1,9,6],
    "claim_amount": [12000,45000,80000,18000,95000,25000,70000,10000,90000,55000,
                     15000,85000,40000,22000,98000,28000,75000,11000,92000,50000],
    "policy_tenure": [4,2,1,5,1,6,2,7,1,3,5,1,3,6,1,4,2,8,1,3],
    "past_claims": [0,2,4,1,5,0,3,0,4,2,1,5,2,0,5,1,3,0,4,2],
    "accident_type": ["Minor","Major","Major","Minor","Major","Minor","Major","Minor",
                      "Major","Minor","Minor","Major","Minor","Minor","Major","Minor",
                      "Major","Minor","Major","Minor"],
    "days_to_report": [1,5,10,2,15,1,8,1,12,4,2,14,3,1,16,2,7,1,13,4],
    "Fraud": [0,0,1,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,0]
})

X = pd.get_dummies(data.drop("Fraud", axis=1), columns=["accident_type"])
y = data["Fraud"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

models = {
    "Bagging": BaggingClassifier(estimator=DecisionTreeClassifier(),
                                 n_estimators=10, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=50, random_state=42),
    "AdaBoost": AdaBoostClassifier(n_estimators=20, random_state=42)
}

for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print(name, "Accuracy:", round(accuracy_score(y_test, pred) * 100, 2), "%")
