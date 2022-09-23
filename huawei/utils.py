import time
import re

timestamp = time.strftime("""%Y-%m-%dT%H:%M:%S%z""")


# patterns regex para identificar o tipo de output (huawei)
# verifica o primeiro elemto da linha do output
# TODO: melhorar a regex para identificar o tipo de output
# TODO: criar funções para cada tipo de output
class Match:
    MAC = '^([0-9A-Fa-f]{4}[:-])'
    UserId = '^\s([\d]{1,4})'
    Statistics = '^(0|[1-9][0-9]*)$'


# transforma o output de string para lista
def string_to_list(output, regx):
    output = output.split('\n')
    result = []

    for line in output:

        if re.search(regx, str(line)) is None:
            pass
        else:
            result.append(line + ' ' + timestamp + '\n')

    return result


# separa os campos da lista
def separate_fields(lista):
    result = []

    for line in lista:
        lista = str(lista)

        line = line.strip()

        line = line.split()

        result.append(line)

    return result


# gera uma lista mac se a primeira coluna do output
# (modelo tabela) for de endereços MAC.
def build_mac_list(lista):
    result = []

    for line in lista:
        result.append(line[0])

    return result


def build_statistics_list(lista):
    result = []
    x = '^(0|[1-9][0-9]*)$'
    for line in lista:
        if re.search(x, str(line)) is None:
            pass
        else:
            result.append(line)

    return result


def get_numbers_from_string(lista):
    result = []
    regex = r"(\d[0-9]*)$"
    matches = re.findall(regex, lista, re.MULTILINE)

    if matches is None:
        pass
    else:
        result.append(matches)

    return result[0]
