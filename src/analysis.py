
def calc_metricas(df):
    metricas = {}

    metricas ['media_usuario_seg'] =  df.groupby('member_casual')['ride_length_seconds'].mean()
    metricas ['media_semanal_seg'] = df.groupby(['member_casual', 'day_of_week'], observed= True)['ride_length_seconds'].mean()
    metricas ['viagens_usuario'] = df.groupby(['member_casual', 'day_of_week'], observed= True).size()
    metricas ['media_usuario_min'] = df.groupby('member_casual')['ride_length_seconds'].mean() / 60

    return metricas