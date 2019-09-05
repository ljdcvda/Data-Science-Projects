import pandas as pd
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
data = pd.read_csv('sphist.csv')
data['Date'] = pd.to_datetime(data['Date'])
data = data.sort_values(by='Date')
data['5_day_avg'] = data['Close'].rolling(5).mean().shift(1)
data['365_day_avg'] = data['Close'].rolling(365).mean().shift(1)
data['5_to_365_mean'] = data['5_day_avg'] / data['365_day_avg']
data['5_day_std'] = data['Close'].rolling(5).std().shift(1)
data['365_day_std'] = data['Close'].rolling(365).std().shift(1)
data['5_to_365_std'] = data['5_day_std'] / data['365_day_std']

data = data[data["Date"] > datetime(year=1951, month=1, day=2)]
data = data.dropna(axis=0)
train = data[data["Date"] < datetime(year=2013, month=1, day=1)]
test = data[data["Date"] >= datetime(year=2013, month=1, day=1)]

features = ['5_day_avg', '365_day_avg', '5_to_365_mean', '5_day_std', '365_day_std', '5_to_365_std']
target = 'Close'
model = LinearRegression()
model.fit(train[features], train[target])
predictions = model.predict(test[features])

mae = mean_absolute_error(predictions, test[target])
print(mae)