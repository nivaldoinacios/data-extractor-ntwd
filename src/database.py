from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os

load_dotenv()

# váriaveis de ambiente
CLOUD_ID = os.getenv('ELK_CLOUD_ID')
PASSWORD = os.getenv('ELK_PASSWORD')
USER = os.getenv('ELK_USER')


# função para criar instâncias de conexões com o elasticsearch
def Engine():
    """
    Connect to Elasticsearch
    """
    es = Elasticsearch(cloud_id=CLOUD_ID,
                       basic_auth=(USER, PASSWORD))
    return es


if __name__ == '__main__':
    # instância de conexão com o banco de dados
    client = Engine()
    # verifica conexão com o banco
    try:
        print(client.info())
    except Exception as e:
        print(e)
