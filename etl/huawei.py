from src.huawei import utils, commands, devices, patterns, dataframes

DEVICE = devices.AC6005


def extract_access_user():
    """Executa os comandos e retorna os outputs."""
    # executa o comando Display access-user e retorna o output
    output = commands.display_access_user(**DEVICE)
    output = utils.string_to_list(output, patterns.Match.UserId)
    output = utils.separate_fields(output)
    return output


def tratament_access_user():
    """Trata o output do comando Display access-user."""
    output = extract_access_user()
    # cria um dataframe com o output do comando
    df = dataframes.df_access_user(output)
    return df


def extract_station_all():
    """Executa os comandos e retorna os outputs."""
    # executa o comando Display station all e retorna o output
    output = commands.display_station_all(**DEVICE)
    output = utils.string_to_list(output, patterns.Match.MAC)
    output = utils.separate_fields(output)
    return output


def tratament_station_all():
    """Trata o output do comando Display station all."""
    output = extract_station_all()
    # cria um dataframe com o output do comando
    df = dataframes.df_station_all(output)
    return df


def extract_statistics():
    """Executa os comandos e retorna os outputs."""
    # executa o comando Display station statistics sta-mac e retorna o output
    mac_list = get_mac_list()
    output = []
    for mac in mac_list:
        output.append(commands.display_station_statistics_sta_mac(mac, **DEVICE))

    connection.disconnect()
    return output


def get_mac_list():
    """Retorna uma lista de MACs."""
    output = extract_station_all()
    return utils.build_mac_list(output)


if __name__ == '__main__':
    # print(extract_access_user())
    # print(tratament_access_user())
    # print(extract_display_station_all())
    # print(tratament_station_all())
    # print(get_mac_list())
    print(extract_statistics())
