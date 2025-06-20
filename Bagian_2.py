import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("survey.csv")

selected_columns = ['Age', 'Gender', 'self_employed', 'family_history',
                    'work_interfere', 'no_employees', 'remote_work',
                    'tech_company', 'benefits', 'care_options',
                    'wellness_program', 'seek_help', 'anonymity',
                    'leave', 'mental_health_consequence', 'phys_health_consequence',
                    'coworkers', 'supervisor', 'mental_health_interview',
                    'phys_health_interview', 'mental_vs_physical', 'obs_consequence',
                    'treatment']

df = df[selected_columns]

df.dropna(inplace=True)

label_encoders = {}
for column in df.columns:
    if df[column].dtype == object:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders[column] = le

X = df.drop("treatment", axis=1)
y = df["treatment"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
