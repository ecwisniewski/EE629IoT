
## Plot
import pandas as pd
#import numpy as np
from sqlalchemy import create_engine

# Get Database into a Dataframe
mysqli = create_engine("mysql+mysqldb://pi:password@localhost/database")
query = "SELECT * FROM testtable GROUP BY tdate, ttime"
df = pd.read_sql(query, mysqli)

# Combine Date and Time Columns
#df.apply(lambda r: pd.datetime.combine(r['tdate'],r['ttime']).time(),1)
df['DateTime']=pd.to_datetime(df.pop('tdate'))+pd.to_timedelta(df.pop('ttime'))

print(df.head())


# Plots
plot=df.plot.line(title="Moisture Change Over Time",x='DateTime',y='moisture')
fig = plot.get_figure()
fig.savefig("moisture.png")

plot = df.plot.line(title="Light Change Over Time",x='DateTime',y='light')
fig = plot.get_figure()
fig.savefig("light.png")

plot = df.plot.line(title="Temp Change Over Time",x='DateTime',y='temperature')
fig = plot.get_figure()
fig.savefig("temperature.png")

plot = df.plot.line(title="Hum Change Over Time",x='DateTime',y='humidity')
fig = plot.get_figure()
fig.savefig("humidity.png")
