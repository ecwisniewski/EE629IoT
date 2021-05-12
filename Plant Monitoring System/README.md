# Plant Monitoring System
## Final Project EE629IoT
Repositiory for final project Plant Monitoring System, code and data.

## Description

Designing a Plant Monitoring System to keep track of a plant. By connecting sensors to the Raspberry Pi, one can collect data and use this data to determine the overall state of the plant. The plan is to include sensors to detect soil moisture, light level, temperature, and humidity, and display this information in a meaningful way using LAMP on a local network.

![Plant Image](<https://github.com/errski/EE629IoT/blob/main/Plant%20Monitoring%20System/system.jpg>)

The first step is to get connect the sensors listed and collect meaningful sensor data through the Raspberry Pi. By using Python scripts and the Adafruit libraries for sensors, one is able to access their hardware in an easy way. It took testing to find the best option, but the decision was made to use analog input from the soil moisture and photosensor (to detect light level) and the MCP3008 ADC chip to read the analog values using SPI with the Raspberry Pi, and the DHT11 to detect temperature and humidity for reporting. Next step is to test the input analog values and determine a threshold to determine when the sensor is reading that there is enough moisture or light respectively. 

After setting up the sensors, one can create a database to collect the sensor information using MySQL. By creating a new database and tables to hold information, the information is easily accessible for use. This could be done by using information from class as well as some online resources. By testing MySQL database creation as well as LAMP (Linux Apache MySQL PHP) with the Raspberry Pi, once can create a simple .php file to access the MySQL database and table on the Raspberry Pi. After determining how to complete this task, all that is left is to design the webpage and design it with PHP and access it through LAMP. 

Using PHP, the icons change based on the level of brightness or moisture which is determined by a threshold. By doing these calculations in the .php file, it is easier to make changes on the fly and display data where the data input is not regularly changing. The PHP for this is not too complicated and it adds more character to the light and moisture detection of the system. Some CSS was added to include different fonts and give a cute design and display for the webpage. 

After this was done and the web server and page were shown as expected, the decision was made to try to print graphs to the webpage of the data from MySQL over time. This can be accomplished with a Python script that will take the MySQL database and plot the data. Since the sensors were reading fundamentally different values, it seemed like the best idea was to create a separate plot for each column. 

The script to plot the MySQL database was written using sqlalchemy to access the database and transforming this data into a DataFrame object using Pandas. With the proper permissions, the user on Raspberry Pi can save the plot figures to the /var/www/html folder where the webpage is being run from. So with these images available, one can use HTML to print them to the page.

![Monitor Image](<https://github.com/errski/EE629IoT/blob/main/Plant%20Monitoring%20System/index_php_main.jpg>)
![Data Image](<https://github.com/errski/EE629IoT/blob/main/Plant%20Monitoring%20System/index_php_graphs.jpg>)
[See Full Here](https://github.com/errski/EE629IoT/blob/main/Plant%20Monitoring%20System/index_php_webpage.jpg)

Displayed is the full main webpage called index.php. To view all the data, a PHP file was made called fulltable.php which displays all of the values collected in the MySQL database.

The final part of this project involves data collection and how to make sure the database is being updated, and scheduling tasks to run on the Raspberry Pi. To achieve this one can use Cron to schedule the tasks on the Raspberry Pi. The script is scheduled to run 4x a day at specific times to get a range of what the sunlight during the day might be like and collect the moisture reading at least once per day.

![Using Cron Image](<https://github.com/errski/EE629IoT/blob/main/Plant%20Monitoring%20System/cron_scheduler.jpg>)

For this project, it's possible that 4x a day is not enough data for light, but this can be managed through Cron easily. Another upgrade would be running the plotting.py script more than once a day or after the sched_sensors.py script runs. 

### Useful Elements For This Project

[Cron](https://bc-robotics.com/tutorials/setting-cron-job-raspberry-pi/)
