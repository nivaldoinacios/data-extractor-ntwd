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

df.to_csv(
    path_or_buf=os.getenv('dados'),
    sep=';',
    columns=['UserID', 'Username', 'IPADDRESS', 'MAC', 'Status', 'AP_ID',
             'AP_NAME', 'RF/WLAN', 'BAND', 'Type', 'RX/TX', 'RSSI', 'VLAN',
             'SSID', '@timestamp-py', "PCKT_SENT", "PCKT_RECEIVED", "BYTES_SENT",
             "BYTES_RECEIVED", "WID_RATE_SENT", "WID_RATE_RECEIVED",
             "TRIGGER_R_TOTAL", "TRIGGER_R_FAILED", "BYTES_SENT_CALC"],
    index_label='index',
    line_terminator='\n'
)

if __name__ == '__main__':
    print(df)
