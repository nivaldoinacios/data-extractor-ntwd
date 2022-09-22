import time
import re

timestamp = time.strftime("""%Y-%m-%dT%H:%M:%S%z""")


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
