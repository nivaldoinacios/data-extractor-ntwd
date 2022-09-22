import pandas as pd
import numpy as np


def df_access_user(lista):
    df = pd.DataFrame(lista,
                      columns=["UserID", "Username", "IPADDRESS", "MAC",
                               "Status", "@timestamp-py"]
                      )

    return df


def df_station_all(lista):
    df = pd.DataFrame(lista,
                      columns=['MAC', 'AP_ID', 'AP_NAME', 'RF/WLAN', 'BAND', 'Type',
                               'RX/TX', 'RSSI', 'VLAN', 'IPADDRESS', 'SSID',
                               "@timestamp-py"]
                      )

    return df
