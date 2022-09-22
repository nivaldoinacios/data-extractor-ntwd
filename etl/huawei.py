from src.huawei import utils, commands, devices, patterns

DEVICE = devices.AC6005


def pipeline_01():
    """Executa os comandos e retorna os outputs."""
    # executa o comando Display access-user e retorna o output
    output = commands.display_access_user(**DEVICE)
    output = utils.string_to_list(output, patterns.Match.UserId)
    output = utils.separate_fields(output)
    return output


def pipeline_02():
    """Executa os comandos e retorna os outputs."""
    # executa o comando Display station all e retorna o output
    output = commands.display_station_all(**DEVICE)
    output = utils.string_to_list(output, patterns.Match.MAC)
    output = utils.separate_fields(output)
    return output


def get_mac_list():
    """Retorna uma lista de MACs."""
    output = pipeline_02()
    return utils.build_mac_list(output)
# pipeline_2 = utils.string_to_list(pipeline_1, '^([0-9A-Fa-f]{4}[:-])')


if __name__ == '__main__':
    # print(pipeline_01())
    # print(pipeline_02())
    print(get_mac_list())
