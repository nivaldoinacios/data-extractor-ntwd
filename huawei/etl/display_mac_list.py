from huawei import utils, commands, configs
from display_station_all import extract_display_station_all

DEVICE = configs.AC6005


def get_mac_list():
    """Retorna uma lista de MACs."""
    output = extract_display_station_all()
    return utils.build_mac_list(output)


if __name__ == '__main__':
    print(get_mac_list())
