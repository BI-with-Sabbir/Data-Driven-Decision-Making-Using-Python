import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
import warnings

warnings.filterwarnings("ignore")

# Load the dataset
df = pd.read_csv("pjm_hourly_energy.csv", parse_dates=["Datetime"], index_col="Datetime")

# Create time-based features
def create_features(df):
    df['hour'] = df.index.hour
    df['dayofweek'] = df.index.dayofweek
    df['quarter'] = df.index.quarter
    df['month'] = df.index.month
    df['year'] = df.index.year
    df['dayofyear'] = df.index.dayofyear
    df['dayofmonth'] = df.index.day
    df['weekofyear'] = df.index.isocalendar().week
    return df

df = create_features(df)

# Train-test split (data after 2015 used for testing)
train = df[df.index.year < 2015]
test = df[df.index.year >= 2015]

X_train, y_train = train.drop(columns=['AEP_MW']), train['AEP_MW']
X_test, y_test = test.drop(columns=['AEP_MW']), test['AEP_MW']

# Train the XGBoost model
model = xgb.XGBRegressor(objective="reg:squarederror", n_estimators=1000, learning_rate=0.05)
model.fit(X_train, y_train, eval_set=[(X_test, y_test)], early_stopping_rounds=50, verbose=False)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate performance
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)
mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100

print(f"RMSE: {rmse:.2f}")
print(f"MAE: {mae:.2f}")
print(f"MAPE: {mape:.2f}%")

# Save the model
model.save_model("xgboost_model.json")
