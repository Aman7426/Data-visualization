import csv
from datetime import datetime
import matplotlib.pyplot as plt


file_name =  'data/sitka_weather_2018_simple.csv'
with open (file_name) as f :
    reader = csv.reader(f)
    header_Row = next(reader)
    
    #for index,column_header in enumerate(header_Row):
       # print(index,column_header)

    #get high tempraure , dates from this file
    highs ,dates,lows = [],[],[]
    
    for row in reader:
        current_date = datetime.strptime(row[2] ,'%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        highs.append(high)
        lows.append(low)
        dates.append(current_date)

#plot the high temprature 
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates , highs, c='red',alpha = 0.5)
ax.plot(dates ,lows , c = 'Blue', alpha = 0.5)
plt.fill_between(dates,highs,lows, facecolor = 'Blue',alpha = 0.3)

# Format plot.
plt.title("Daily high and low temperatures,  2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
