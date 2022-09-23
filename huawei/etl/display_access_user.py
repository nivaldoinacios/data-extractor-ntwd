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


def extract_display_access_user():
    """Executa os comandos e retorna os outputs."""
    # executa o comando Display access-user e retorna o output
    output = display_access_user(**AC6005)
    output = utils.string_to_list(output, utils.Match.UserId)
    output = utils.separate_fields(output)
    return output


df_access_user = pd.DataFrame(extract_display_access_user(),
                              columns=["UserID", "Username", "IPADDRESS", "MAC",
                                       "Status", "@timestamp-py"]
                              )

if __name__ == '__main__':
    print(df_access_user)
