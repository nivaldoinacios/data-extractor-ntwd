# funções para o tratamento e processamento dos outputs dos comandos

from netmiko import ConnectHandler
from dotenv import load_dotenv
import os

load_dotenv()

AC6005 = {
    'device_type': 'huawei',
    'host': os.getenv('HOST'),
    'username': os.getenv('USUARIO'),
    'password': os.getenv('PASSWORD'),
    'global_delay_factor': 1.0,
}


def display_access_user(**dev):
    # conecta no dispositivo
    connection = ConnectHandler(**dev, conn_timeout=60)
    connection.enable()
    # envia os comandos ao dispositivo
    command = 'display access-user'
    # capturando output do comando
    output = connection.send_command(command)
    # encerra a sessão aberta no dispositivo
    connection.disconnect()
    return output


def display_station_all(**dev):
    connection = ConnectHandler(**dev, conn_timeout=60)
    connection.enable()
    command = 'display station all'
    output = connection.send_command(command)
    connection.disconnect()
    return output


def display_station_statistics_sta_mac(mac, **dev):
    connection = ConnectHandler(**dev, conn_timeout=60)
    connection.enable()
    command = 'display station statistics sta-mac ' + mac
    output = connection.send_command(command)
    connection.disconnect()
    return output


if __name__ == '__main__':
    # x = display_station_all(**AC6005)
    # y = string_to_list(x, '^([0-9A-Fa-f]{4}[:-])')
    # z = separate_fields(y)
    # print(x, y, z, sep='\n')
    # x = display_station_statistics_sta_mac('00d7-6d3b-dc6f', **AC6005)
    x = display_station_statistics_sta_mac('5ccd-5bf3-c091', **AC6005)
    print(x)

