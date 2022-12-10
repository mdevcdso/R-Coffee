# R-Coffee 
Are you tired of burning yourself every time you drink your coffee or tea ? Don't panic ! The R-Coffee will solve this problem for you !

There is nothing more annoying than getting burned by a tea that is too hot or a coffee that has been forgotten and therefore too cold to drink.
So, I made a little project on a Raspberry Pi 3B that will make your life easier.

To achieve this, I used :
- 1 captor Seesaw i2c Soil
- 1 captor Sensor BME 280
- 1 keyboard
- 1 mouse
- 1 screen
- 1 adaptator Qwiic pHat
- 1 mug
- Coffee, tea... or water why not ? 🙂

**"According to the WHO, the risk of burns is present from 50 ° C when drinking coffee."**

----------

Method :
1) Turn on the Raspberry by plugging in the power cable and Ethernet
2) Connect all sensors and other peripheral hardware (keyboard, mouse, ...)
3) Turn on the screen and open Python
4) Begin to write your code
5) Boil the water and pour into the mug when it comes to a boil (i.e. close to 100°C)
6) Put the captor Seesaw i2c Soil in the water without the line being completely submerged (this may damage the connectors of the sensor)
7) When everything is ready, launch the code
8) Observ the results

It is estimated that it would take about 7-8 minutes to reach the ideal temperature if we graph below :

![image](https://user-images.githubusercontent.com/100076215/206738311-bdd26200-7806-487e-96f7-0c78d3099849.png)

This graph shows three datas collected by our Raspberry but only the water temperature in green interests us here. This allows us to deduce the time it takes us roughly in minutes to avoid burning ourselves.

----------

So, this experiment was the first I did on Raspberry and it was presented and it was intended for scientific research in the first place.

Marion
