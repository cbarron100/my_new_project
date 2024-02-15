# -*- coding: utf-8 -*-


## First AI project: check based on characteristics of wines what the quality should be
## I think the best way to do it will be with nearest neightbour 
## tested the raw data with k = 3, going to scale the characteristics score was like 0.4
## test with scalar and the score became like 0.58
## test with raw data and fine tuning K was poor,
## but when I tried it with the scaled values k = 1 was the best with a score of 0.65
#%%
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
#%%

data = np.loadtxt("WineQualityRed.csv", delimiter= ";", skiprows = 1)

x_data = data[ : , :-1]
y_data = data[ : , -1]
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size= 0.2, random_state=6)
scalar = StandardScaler()
x_train_standard_scalar = scalar.fit_transform(x_train)
x_test_standard_scalar = scalar.fit_transform(x_test)

#%%


#k = 3

score = 0 
best = 0

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(x_train_standard_scalar, y_train)
y_predict = knn.predict(x_test_standard_scalar)

print(classification_report(y_test, y_predict))
print(confusion_matrix(y_test,y_predict))
#%%





