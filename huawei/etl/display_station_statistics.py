from display_mac_list import get_mac_list

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


def display_station_statistics_sta_mac(mac, **dev):
    connection = ConnectHandler(**dev, conn_timeout=60)
    connection.enable()
    command = 'display station statistics sta-mac ' + mac
    output = connection.send_command(command)
    connection.disconnect()
    return output


def extract_statistics(mac):
    """Executa os comandos e retorna os outputs."""
    # executa o comando Display station statistics sta-mac e retorna o output
    output = display_station_statistics_sta_mac(mac, **AC6005)
    output = utils.get_numbers_from_string(output)
    output.append(mac)
    return output


def extract_statistics_list():
    """Executa os comandos e retorna os outputs."""
    # executa o comando Display station statistics sta-mac e retorna o output
    mac_list = get_mac_list()
    output = []
    for mac in mac_list:
        output.append(extract_statistics(mac))
    return output


df_statistics = pd.DataFrame(extract_statistics_list(),
                             columns=["PCKT_SENT", "PCKT_RECEIVED", "BYTES_SENT",
                                      "BYTES_RECEIVED", "WID_RATE_SENT", "WID_RATE_RECEIVED",
                                      "TRIGGER_R_TOTAL", "TRIGGER_R_FAILED", "MAC"]
                             )


if __name__ == '__main__':
    # print(extract_statistics('00d7-6d3b-dc6f'))
    # print(extract_statistics_list())
    print(df_statistics)

