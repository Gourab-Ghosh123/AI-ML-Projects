
import pandas as pd

from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split

from sklearn.metrics import(
    mean_absolute_error ,
    mean_squared_error,
    r2_score
    )

data = {
    "size":[1000,1200,1500,1800,2000,2200,2500,2800],
    "price":[10,12,15,18,20,22,25,28]
}

df = pd.DataFrame(data)

X = df[["size"]]

y = df["price"]

X_train , X_test , y_train , y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train , y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(
    y_test,
    predictions
)

mse = mean_squared_error(
    y_test,
    predictions
)

r2 = r2_score(
    y_test,
    predictions
)

print("MAE :" , mae)
print("MSE : " , mse)
print("r2 Score : " , r2)