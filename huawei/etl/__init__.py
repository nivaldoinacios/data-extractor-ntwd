from display_station_all import df_station_all
from display_access_user import df_access_user
from display_station_statistics import df_statistics
import pandas as pd

df = pd.merge(df_access_user, df_station_all, how='outer', on=['MAC'])

df = df.drop(columns=['IPADDRESS_y', '@timestamp-py_x'])
df = df.rename(columns={'@timestamp-py_y': '@timestamp-py'})
df = df.rename(columns={'IPADDRESS_x': 'IPADDRESS'})

df = pd.merge(df, df_statistics, how='outer', on=['MAC'])
df = df.fillna(0)

if __name__ == '__main__':
    print(df)