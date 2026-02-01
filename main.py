# Tech AI for Engineers – Energy Consumption Prediction
# This script is intentionally simple and readable.
# Students are expected to generate this with GitHub Copilot, step by step.

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error


# =========================
# Step 1: Load & explore
# =========================
df = pd.read_csv("house_consumption.csv")

print("\n--- Data Preview ---")
print(df.head())

print("\n--- Data Info ---")
df.info()

print("\n--- Statistical Summary ---")
print(df.describe())


# =========================
# Step 2: Data cleaning
# =========================
print("\n--- Missing Values (Before) ---")
print(df.isnull().sum())

df = df.drop_duplicates()
df = df.fillna(df.median(numeric_only=True))

print("\n--- Missing Values (After) ---")
print(df.isnull().sum())


# =========================
# Step 3: Visualization
# =========================
# Correlation heatmap
corr = df.corr(numeric_only=True)

plt.figure()
plt.imshow(corr.values)
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45, ha="right")
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Correlation Heatmap")
plt.colorbar()
plt.tight_layout()
plt.show()

# Scatter plot (House_Area vs Consumption)
plt.figure()
plt.scatter(df["House_Area"], df["Consumption"])
plt.xlabel("House_Area")
plt.ylabel("Consumption")
plt.title("House Area vs Energy Consumption")
plt.tight_layout()
plt.show()


# =========================
# Step 4: Train model
# =========================
X = df.drop(columns=["Consumption"])
y = df["Consumption"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)


# =========================
# Step 5: Evaluate model
# =========================
y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print("\n--- Model Evaluation ---")
print(f"R² Score: {r2:.4f}")
print(f"Mean Squared Error: {mse:.4f}")

plt.figure()
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Consumption")
plt.ylabel("Predicted Consumption")
plt.title("Actual vs Predicted Consumption")
plt.tight_layout()
plt.show()

