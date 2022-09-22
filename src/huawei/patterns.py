import re


# patterns regex para identificar o tipo de output (huawei)
# verifica o primeiro elemto da linha do output
class Pattern:
    MAC = '^([0-9A-Fa-f]{4}[:-])'
    UserId = '^\s([\d]{1,4})'

    # # trata os dados do output
    # output = string_to_list(output, '^\s([\d]{1,4})')
    # #
    # output = separate_fields(lista)
    #
    # keys = ['UserID', 'Username', 'IP_Address', 'MAC', 'Status']
    #
    # my_dict = []
    #
    # for key in keys:
    #     for line in output:
    #         x = dict.fromkeys(key, line)
    #         my_dict.append(x)
