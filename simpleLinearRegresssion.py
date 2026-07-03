# IMPORT LIBRARIES
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# IMPORT THE DATASET
dataset = pd.read_csv(r"C:\Users\HP\Downloads\Salary_Data.csv")   # ← Update with actual filename

x = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]


from sklearn.model_selection import train_test_split

x_train , x_test, y_train, y_test = train_test_split(x,y,train_size = 0.8, test_size = 0.2,random_state=0)



from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)


plt.scatter(x_test, y_test, color='red')
plt.plot(x_train,regressor.predict(x_train), color= 'blue')
plt.title('salary vs exp')
plt.xlabel('years of exp')
plt.ylabel('Salary')
plt.show()



m_coef = regressor.coef_
print(m_coef)

c_inter = regressor.intercept_
print(c_inter)

y_12  =  m_coef * 12 + c_inter
print(y_12)

y_20 = m_coef *  20 + c_intercept_
print(y_20)









