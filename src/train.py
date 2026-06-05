# load packages
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# load the dataset
bank_data = pd.read_csv('/Users/macbookpro/Desktop/End-to-End Projects/bank_customer/data/BankCustomerData.csv')

# drop the target column
X = bank_data.drop('term_deposit', axis=1)
y = bank_data['term_deposit']

def encode_yes_no(bank_data, term_deposit):
    bank_data[term_deposit] = bank_data[term_deposit].map({
        'no': 0,
        'yes': 1
    })

    return bank_data

# separate numerical and categorical columns
numerical_cols = X.select_dtypes(include=["int64"]).columns
categorical_cols = X.select_dtypes(include=["object"]).columns

# Numerical Pipeline
num_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler())
])

# Categorical Pipeline
cat_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

# preprocessor
preprocessor = ColumnTransformer([
    ("num", num_pipeline, numerical_cols),
    ("cat", cat_pipeline, categorical_cols)
])

# final pipeline
model_pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", RandomForestClassifier(
        n_estimators=200,
        random_state=42
    ))
])

# train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# model training
model_pipeline.fit(X_train, y_train)

# model prediction
predictions = model_pipeline.predict(X_test)

# classification report
print("\nClassification Report: ")
print(classification_report(y_test, predictions))

# confusion matrix
cm = confusion_matrix(y_test, predictions)
print("\nConfusion Matrix: ")
print(cm)

# model accuracy
accuracy = accuracy_score(y_test, predictions)

# result
print(f"Accuracy Score: {accuracy:.4f}")

# rf model
model = model_pipeline.named_steps["model"]
# transform feature names
feature_names = model_pipeline.named_steps[
    "preprocessor"
].get_feature_names_out()

# get feature names
importances = model.feature_importances_

# create a dataframe for FI
importance_data = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importances
})

importance_data = importance_data.sort_values(
    by="Importance",
    ascending=False
)

print(importance_data.head(20))

# save the model
joblib.dump(model_pipeline, "/Users/macbookpro/Desktop/End-to-End Projects/bank_customer/model/bank_model.pkl")

print("Model saved successfully")