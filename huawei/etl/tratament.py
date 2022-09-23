from huawei.etl import extract
import pandas as pd

df_access_user = pd.DataFrame(extract.extract_display_access_user(),
                              columns=["UserID", "Username", "IPADDRESS", "MAC",
                                       "Status", "@timestamp-py"]
                              )

df_stations_all = pd.DataFrame(extract.extract_display_station_all(),
                               columns=['MAC', 'AP_ID', 'AP_NAME', 'RF/WLAN', 'BAND', 'Type',
                                        'RX/TX', 'RSSI', 'VLAN', 'IPADDRESS', 'SSID',
                                        "@timestamp-py"]
                               )


df_statistics = pd.DataFrame(extract.extract_statistics_list(),
                             columns=["MAC", "PCKT_SENT", "PCKT_RECEIVED", "BYTES_SENT",
                                      "BYTES_RECEIVED", "WID_RATE_SENT", "WID_RATE_RECEIVED",
                                      "TRIGGER_R_TOTAL", "TRIGGER_R_FAILED", "STA_POWER_SAVE"]
                             )

if __name__ == '__main__':
    print(df_access_user)
    print(df_stations_all)
    print(df_statistics)