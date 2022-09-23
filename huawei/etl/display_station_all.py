from netmiko import ConnectHandler
from dotenv import load_dotenv
from huawei import utils
import pandas as pd
import os

load_dotenv()

AC6005 = {
    'device_type': 'huawei',
    'host': os.getenv('HOST'),
    'username': os.getenv('USUARIO'),
    'password': os.getenv('PASSWORD'),
    'global_delay_factor': 1.0,
}


def display_station_all(**dev):
    connection = ConnectHandler(**dev, conn_timeout=60)
    connection.enable()
    command = 'display station all'
    output = connection.send_command(command)
    connection.disconnect()
    return output


def extract_display_station_all():
    """Executa os comandos e retorna os outputs."""
    # executa o comando Display station all e retorna o output
    output = display_station_all(**AC6005)
    output = utils.string_to_list(output, utils.Match.MAC)
    output = utils.separate_fields(output)
    return output


df_station_all = pd.DataFrame(extract_display_station_all(),
                              columns=['MAC', 'AP_ID', 'AP_NAME', 'RF/WLAN', 'BAND', 'Type',
                                       'RX/TX', 'RSSI', 'VLAN', 'IPADDRESS', 'SSID',
                                       "@timestamp-py"]
                              )

if __name__ == '__main__':
    print(df_stations_all.keys())
