import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "size" : [1000 , 1500 , 1800 , 2400 , 3000],
    "bedrooms" : [2 , 3 , 3 , 4 , 4],
    "age" : [20 , 15 , 10 , 5 , 2],
    "price" : [50 , 75 , 90 , 120 , 150]
}

df = pd.DataFrame(data)

X = df[["size" , "bedrooms" , "age"]]

y = df["price"]

model = LinearRegression()

model.fit(X , y)

prediction = model.predict([[2000 , 3 , 8]])

print(f"Predicted Price: {prediction}")

print(f"Coefficients : {model.coef_}")

print(f"Intercept : {model.intercept_}")