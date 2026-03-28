from pymongo import MongoClient
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["irisDB"]
collection = db["iris"]

data = list(collection.find())

if len(data) == 0:
    print("No data found in MongoDB!")
    exit()

# Convert nested MongoDB structure into flat format
cleaned_data = []

for doc in data:
    cleaned_data.append({
        "sepal_length": float(doc["sepal.length"]),
        "sepal_width": float(doc["sepal.width"]),
        "petal_length": float(doc["petal.length"]),
        "petal_width": float(doc["petal.width"]),
        "species": doc["variety"]
    })

df = pd.DataFrame(cleaned_data)

print("Dataset Preview:")
print(df.head())

# Features & target
X = df[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
y = df["species"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "iris_model.pkl")

print(" Model trained successfully!")