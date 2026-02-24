from src.load_data import load_data
from src.data_cleaning import clean
from src.save import save_csv
from src.visuals import graphs
from src.analysis import calc_metricas

def main():
    df_raw = load_data('.venv/data/*.csv')
    df_clean = clean(df_raw)

    metricas = calc_metricas(df_clean)
    for chave, valor in metricas.items():
        print(f"\n--- {chave.upper()} ---\n {valor}")

    graphs(df_clean)
    save_csv(df_clean)

if __name__ == '__main__':
    main()