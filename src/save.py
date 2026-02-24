def save_csv (df, path = 'bikeShare.csv'):
    df.to_csv(path, index = False)