import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("Book2.csv")

data

model = LinearRegression()
model.fit(data[['videos','days','subscribers',]],data.views)

model.predict([[45,180,3100]])

model.coef_

model.intercept_

views_result_check = (model.coef_[0]*45 + model.coef_[1]*180 + model.coef_[2]*3100) + model.intercept_
views_result_check
