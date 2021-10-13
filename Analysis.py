import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

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
                              'holiday': holidayArray, 'weekday': normalizedweekdayArray, 'workingday': workingdayArray,
                              'weathersit': normalizedweathersitArray, 'temp': tempArray, 'atemp': atempArray,
                              'windspeed': windspeedArray, 'hum': humArray, 'casual': normalizedcasualArray,
                              'registered': normalizedregisteredArray, 'cnt': normalizedcntArray})
# Calculate Correlation
# for x in np.arange(0, 14):
#     for y in np.arange(0, 14):
#         print("Correlation between {} and {} : \n {}".format(normalizedata.columns[x], normalizedata.columns[y],
#                                                              np.corrcoef(normalizedata.iloc[:, x].to_numpy(),
#                                                                          normalizedata.iloc[:, y].to_numpy())))

# Pair plots
# sb.set_style('darkgrid')
# sb.pairplot(normalizedata.iloc[:,11:14])
# plt.show()


# Reg plots
#
# plotreg1 = plt.figure(1)
# sb.regplot(x=normalizedseasonArray, y=normalizedcntArray)
# plt.xlabel('Season')
# plt.ylabel('Count of Total Rental')
#
# plotreg2 = plt.figure(2)
# sb.regplot(x=yrArray, y=normalizedcntArray)
# plt.xlabel('Year')
# plt.ylabel('Count of Total Rental')
#
# plotreg3 = plt.figure(3)
# sb.regplot(x=normalizedmnthArray, y=normalizedcntArray)
# plt.xlabel('Month')
# plt.ylabel('Count of Total Rental')
#
# plotreg4 = plt.figure(4)
# sb.regplot(x=holidayArray, y=normalizedcntArray)
# plt.xlabel('Holiday')
# plt.ylabel('Count of Total Rental')
#
# plotreg5 = plt.figure(5)
# sb.regplot(x=normalizedweekdayArray, y=normalizedcntArray)
# plt.xlabel('WeekDay')
# plt.ylabel('Count of Total Rental')
#
# plotreg6 = plt.figure(6)
# sb.regplot(x=workingdayArray, y=normalizedcntArray)
# plt.xlabel('WorkingDay')
# plt.ylabel('Count of Total Rental')
#
# plotreg7 = plt.figure(7)
# sb.regplot(x=normalizedweathersitArray, y=normalizedcntArray)
# plt.xlabel('Weathersit')
# plt.ylabel('Count of Total Rental')
#
# plotreg8 = plt.figure(8)
# sb.regplot(x=tempArray, y=normalizedcntArray, color='red')
# plt.xlabel('Temperature')
# plt.ylabel('Count of Total Rental')
#
# plotreg9 = plt.figure(9)
# sb.regplot(x=atempArray, y=normalizedcntArray, color='green')
# plt.xlabel('Emotional Temperature')
# plt.ylabel('Count of Total Rental')
#
# plotreg10 = plt.figure(10)
# sb.regplot(x=humArray, y=normalizedcntArray, color='black')
# plt.xlabel('humidity')
# plt.ylabel('Count of Total Rental')
#
# plotreg11 = plt.figure(11)
# sb.regplot(x=windspeedArray, y=normalizedcntArray, color='orange')
# plt.xlabel('WindSpeed')
# plt.ylabel('Count of Total Rental')
#
# plotreg12 = plt.figure(12)
# sb.regplot(x=normalizedcasualArray, y=normalizedcntArray, color='blue')
# plt.xlabel('Number of Casual')
# plt.ylabel('Count of Total Rental')
#
# plotreg13 = plt.figure(13)
# sb.regplot(x=normalizedregisteredArray, y=normalizedcntArray,  scatter_kws={"color": "black"}, line_kws={"color": "red"})
# plt.xlabel('Number of Registered')
# plt.ylabel('Count of Total Rental')
# plt.show()


# Histogram plots
#
# plot1 = plt.figure(1)
# plt.hist(seasonArray)
# plt.ylabel('Season')
#
# plot2 = plt.figure(2)
# plt.hist(mnthArray)
# plt.ylabel('Month')
#
# plot3 = plt.figure(3)
# plt.hist(yrArray)
# plt.ylabel('Year')
#
# plot4 = plt.figure(4)
# plt.hist(weekdayArray)
# plt.ylabel('WeekDay')
#
# plot5 = plt.figure(5)
# plt.hist(workingdayArray)
# plt.ylabel('WorkingDay')
#
# plot6 = plt.figure(6)
# plt.hist(weathersitArray)
# plt.ylabel('WeatherSit')
#
# plot7 = plt.figure(7)
# plt.hist(humArray)
# plt.ylabel('Humidity')
#
# plot8 = plt.figure(8)
# plt.hist(windspeedArray)
# plt.ylabel('WindSpeed')
#
# plot9 = plt.figure(9)
# plt.hist(casualArray)
# plt.ylabel('Casual')
#
# plot10 = plt.figure(10)
# plt.hist(registeredArray)
# plt.ylabel('Registered')
#
# plot11 = plt.figure(11)
# plt.hist(holidayArray)
# plt.ylabel('Holiday')
#
# plot12 = plt.figure(12)
# plt.hist(tempArray)
# plt.ylabel('Temperature')
#
# plot13 = plt.figure(13)
# plt.hist(atempArray)
# plt.ylabel('ATemperature')
#
