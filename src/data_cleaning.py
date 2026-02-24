import pandas as pd

def clean(df):
    # Conversão de datas
    df['ended_at'] = pd.to_datetime(df['ended_at'], errors="coerce")  # transformar em data/hora
    df['started_at'] = pd.to_datetime(df['started_at'], errors="coerce")

    # Remover dados com datas invalidas
    df = df.dropna(subset=['started_at', 'ended_at'])

    # Duração da viagem
    df['ride_length'] = df['ended_at'] - df['started_at']
    df = df[df['ride_length'].dt.total_seconds() > 0]

    # Remover valores inválidos
    filtro_teste = df['start_station_name'].str.contains('HQ|TEST', na=False)  # Remover valores de teste
    df = df[~filtro_teste].copy()

    # Ordenando os dias da semana
    mapa = {
        'Monday': 'segunda-feira',
        'Tuesday': 'terça-feira',
        'Wednesday': 'quarta-feira',
        'Thursday': 'quinta-feira',
        'Friday': 'sexta-feira',
        'Saturday': 'sábado',
        'Sunday': 'domingo'
    }
    df['day_of_week'] = df['started_at'].dt.day_name().map(mapa)
    ordem_dias = ['segunda-feira','terça-feira','quarta-feira','quinta-feira','sexta-feira','sábado','domingo']
    df['day_of_week'] = pd.Categorical(df['day_of_week'], categories=ordem_dias, ordered=True)
    # Duração em segundos
    df['ride_length_seconds'] = df['ride_length'].dt.total_seconds()

    # Hora do dia
    df['hour'] = df['started_at'].dt.hour
    return df
