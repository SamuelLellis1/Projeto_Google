import seaborn as sns
import matplotlib.pyplot as plt

def graphs (df):
    #  Viagens por dia da semana
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='day_of_week', hue='member_casual')
    plt.title('Viagens por dia da semana: Casuais vs Membros')
    plt.xlabel('Dia da semana')
    plt.ylabel('Total de viagens')
    plt.legend(title='Tipo de usuário')
    plt.tight_layout()
    plt.show()

    # Duração das viagens durante a semana
    df_duracao = df.groupby(['member_casual', 'day_of_week'], observed=True)[
        'ride_length_seconds'].mean().reset_index()
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df_duracao, x='day_of_week', y='ride_length_seconds', hue='member_casual', marker='o')
    plt.title('Duração media de viagens durante a semana')
    plt.xlabel('Dia da semana')
    plt.ylabel('duração media(segundos)')
    plt.tight_layout()
    plt.show()

    # Horários de pico
    df_picos = df.groupby(['hour', 'member_casual']).size().reset_index(name='quantidade_viagens')
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df_picos, x='hour', y='quantidade_viagens', hue='member_casual', marker='o')
    plt.title('Horários de pico durante a semana')
    plt.xlabel('Horário(0-23h)')
    plt.ylabel('Quantidade de viagens')
    plt.xticks(range(0, 24))
    plt.grid(True, linestyle='--', alpha=.6)
    plt.tight_layout()
    plt.show()

