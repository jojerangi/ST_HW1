import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import random


def simple_equation(x, y):
    x = np.insert(np.ones((731, 1)), 1, x, axis=1)
    theta = np.linalg.inv(np.transpose(x) @ x) @ np.transpose(x) @ y
    return theta


def gradient_descent(x, y, m):
    x = np.insert(np.ones((731, 1)), 1, x, axis=1)
    theta = np.zeros(x.shape[1])
    iter = 36000
    alpha = 0.000001
    lastError = 1000000
    errors = []
    for it in np.arange(iter):
        theta = theta - alpha * (0.5 * m) * np.dot(np.dot(x, theta) - y, x)
        J = (0.5 * m) * np.sum(np.power(np.dot(x, theta) - y, 2))
        if np.abs(J - lastError) < 0.0000001:
            break
        errors.append(J)
        lastError = J
        print("iter: {} ,error: {} ".format(it, J))
    plt.plot(np.arange(len(errors)), errors)
    plt.show()
    return theta


def main():
    data = pd.read_csv("Datasets/day.csv")

    seasonArray = data.loc[:]['season']
    yrArray = data.loc[:]['yr']
    mnthArray = data.loc[:]['mnth']
    holidayArray = data.loc[:]['holiday']
    weekdayArray = data.loc[:]['weekday']
    workingdayArray = data.loc[:]['workingday']
    weathersitArray = data.loc[:]['weathersit']
    tempArray = data.loc[:]['temp']
    atempArray = data.loc[:]['atemp']
    humArray = data.loc[:]['hum']
    windspeedArray = data.loc[:]['windspeed']
    casualArray = data.loc[:]['casual']
    registeredArray = data.loc[:]['registered']
    cntArray = data.loc[:]['cnt']

    normalizedseasonArray = np.divide(seasonArray, max(seasonArray))
    normalizedmnthArray = np.divide(mnthArray, max(mnthArray))
    normalizedweekdayArray = np.divide(weekdayArray, max(weekdayArray))
    normalizedweathersitArray = np.divide(weathersitArray, max(weathersitArray))
    normalizedcasualArray = np.divide(casualArray, max(casualArray))
    normalizedregisteredArray = np.divide(registeredArray, max(registeredArray))
    normalizedcntArray = np.divide(cntArray, max(cntArray))

    normalizedata = pd.DataFrame({'season': normalizedseasonArray, 'yr': yrArray, 'mnth': normalizedmnthArray,
                                  'holiday': holidayArray, 'weekday': normalizedweekdayArray,
                                  'workingday': workingdayArray,
                                  'weathersit': normalizedweathersitArray, 'temp': tempArray, 'atemp': atempArray,
                                  'windspeed': windspeedArray, 'hum': humArray, 'casual': normalizedcasualArray,
                                  'registered': normalizedregisteredArray, 'cnt': normalizedcntArray})
    normalizedata_v2 = np.concatenate((normalizedata.iloc[:, 11:13].to_numpy(),
                                       np.power(normalizedata.iloc[:, 11:13].to_numpy(), 2)), axis=1)

    thetaE = simple_equation(np.transpose(normalizedata_v2),
                             np.transpose(normalizedata.iloc[:, 13].to_numpy()))
    thetaG = gradient_descent(np.transpose(normalizedata_v2),
                              np.transpose(normalizedata.iloc[:, 13].to_numpy()), len(data))
    print(thetaE)
    print(thetaG)


if __name__ == '__main__':
    main()
