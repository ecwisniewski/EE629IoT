
## Plot
import os
import pandas as pd
#import numpy as np
from sqlalchemy import create_engine

# Get Database into a Dataframe
mysqli = create_engine("mysql+mysqldb://pi:password@localhost/database")
query = "SELECT * FROM testtable GROUP BY tdate, ttime"
df = pd.read_sql(query, mysqli)

# Combine Date and Time Columns
#df.apply(lambda r: pd.datetime.combine(r['tdate'],r['ttime']).time(),1)
df['Date Time']=pd.to_datetime(df.pop('tdate'))+pd.to_timedelta(df.pop('ttime'))

#print(df.head())

# Get Path to HTML
imgs_path = "/var/www/html/images"


# Plots
plot=df.plot.line(title="Moisture Change Over Time(Where >60=Dry)",x='Date Time',y='moisture')
fig = plot.get_figure()
fig.savefig(os.path.join(imgs_path,"moisture.png"))

plot = df.plot.line(title="Light Change Over Time (Where >11=Dark)",x='Date Time',y='light')
fig = plot.get_figure()
fig.savefig(os.path.join(imgs_path,"light.png"))

plot = df.plot.line(title="Temp Change Over Time (Indoors)",x='Date Time',y='temperature')
fig = plot.get_figure()
fig.savefig(os.path.join(imgs_path,"temperature.png"))

plot = df.plot.line(title="Hum Change Over Time(Indoors)",x='Date Time',y='humidity')
fig = plot.get_figure()
fig.savefig(os.path.join(imgs_path,"humidity.png"))
