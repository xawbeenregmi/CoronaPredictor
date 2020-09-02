import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

##### Load Data
data = pd.read_csv('coronaCases.csv',sep =',')
data = data[['id','cases']]
print('-'*30);print('HEAD');print('-'*30)
print(data.head())

###### Prepare Data
print('-'*30);print('Prepare Data');print('-'*30)
x = np.array(data['id']).reshape(-1,1)
y = np.array(data['cases']).reshape(-1,1)
plt.plot(y, '-m')
#plt.show()
polyFeat = PolynomialFeatures(degree=4)
x = polyFeat.fit_transform(x)
#print(x)

###### Training Data
print('-'*30);print('Traning Data');print('-'*30)
model = linear_model.LinearRegression()
model.fit(x,y)
accuracy = model.score(x,y)
print(f'Accuracy:, {round(accuracy*100,3)} %')

y0 = model.predict(x)


#### Prediction
days = 17
print('-'*30);print('Prediction Data');print('-'*30)
print(f'Prediction - Cases after {days} days:', end='')
print(round(int(model.predict(polyFeat.fit_transform([[234+days]])))/1000000,2), 'Millions')

x1 = np.array(list(range(1,234+days))).reshape(-1,1)
y1 = model.predict(polyFeat.fit_transform(x1))
plt.plot(y1, '--r')
plt.plot(y0, '--b')
plt.show()
