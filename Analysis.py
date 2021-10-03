import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

data = pd.read_csv("Datasets/day.csv")
seasonArray = data.loc[:]['season']
mnthArray = data.loc[:]['mnth']
weekdayArray = data.loc[:]['weekday']
weathersitArray = data.loc[:]['weathersit']
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




