import pandas as pd
import glob

def load_data(path = '.venv/data/*.csv'):
    arquivos = glob.glob(path)
    if not arquivos:
        raise FileNotFoundError('Nenhum arquivo CSV encontrado no diretório.')

    lista_df = [pd.read_csv(arq) for arq in arquivos]
    return pd.concat(lista_df, ignore_index=True)