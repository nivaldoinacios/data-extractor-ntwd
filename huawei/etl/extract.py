from huawei import utils, commands, configs

DEVICE = configs.AC6005


def extract_display_station_all():
    """Executa os comandos e retorna os outputs."""
    # executa o comando Display station all e retorna o output
    output = commands.display_station_all(**DEVICE)
    output = utils.string_to_list(output, utils.Match.MAC)
    output = utils.separate_fields(output)
    return output


def get_mac_list():
    """Retorna uma lista de MACs."""
    output = extract_display_station_all()
    return utils.build_mac_list(output)


def extract_statistics(mac):
    """Executa os comandos e retorna os outputs."""
    # executa o comando Display station statistics sta-mac e retorna o output
    output = commands.display_station_statistics_sta_mac(mac, **DEVICE)
    output = utils.get_numbers_from_string(output)
    return output


def extract_statistics_list():
    """Executa os comandos e retorna os outputs."""
    # executa o comando Display station statistics sta-mac e retorna o output
    mac_list = get_mac_list()
    output = []
    for mac in mac_list:
        output.append(mac + ',' + extract_statistics(mac))
    return output


if __name__ == '__main__':
    # print(extract_display_access_user())
    # print(extract_display_station_all())
    # print(get_mac_list())
    print(extract_statistics('50eb-71c2-1a9b'))
    print(extract_statistics_list())

