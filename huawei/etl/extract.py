from huawei import utils, commands, configs

DEVICE = configs.AC6005


def extract_display_access_user():
    """Executa os comandos e retorna os outputs."""
    # executa o comando Display access-user e retorna o output
    output = commands.display_access_user(**DEVICE)
    output = utils.string_to_list(output, utils.Match.UserId)
    output = utils.separate_fields(output)
    return output


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


if __name__ == '__main__':
    # print(extract_display_access_user())
    # print(extract_display_station_all())
    print(get_mac_list())
    print(extract_statistics('5ccd-5bf3-c091'))

