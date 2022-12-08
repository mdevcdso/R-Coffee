import numpy as np
import pandas as pd
import qwiic bme280
from board import SCL,SDA
import busio
from adafruit seesaw.seesaw import Seesaw
import time

#declaring variables
i2c_bus = busio.I2C(SCL,SDA)
mysensor = qwiic_bme280.QwiicBme280()
ss = Seesaw(i2c_bus,addr = 0x36)

list1 = []
list2 = []
list3 = []
list4 = []

for i in np.arange(0,30): #For loop to perform scans every 30 seconds
    time.sleep(30) #scan every 30 seconds
    mysensor.begin()
    list1.append(i)
    list2.append(mysensor.humidity)
    list3.append(mysensor.temperature_celsius)
    list4.append(ss.get_temp())
    print("Humid air: ", mysensor.humidity)
    print("Temp_air: ",mysensor.temperature_celsius)
    print("Temp_eau: "+str(ss.get_temp()))

data = pd.DataFrame() #convert harvested values into retainable data
data["numero"] = list1
data["humidite_air"] = list2
data["temp_air"] = list3
data["temp_eau"] = list4

Data.to_csv("Projet_Raspberry.csv", index=None, sep=",") #save the collected data in a ".csv" file
