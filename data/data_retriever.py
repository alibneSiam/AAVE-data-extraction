import pandas as pd

data_src = [
    {
        'crypto': 'BTC',
        'aave': "../data/aave_data/Core Market/Wrapped BTC.csv",
        'polyio': "../data/polyio_data/adjusted/BTC.csv"
    },
    {
        'crypto': 'ETH',
        'aave': "../data/aave_data/Core Market/Wrapped ETH.csv",
        'polyio': "../data/polyio_data/adjusted/ETH.csv"
    },
    {
        'crypto': 'USDC',
        'aave': "../data/aave_data/Core Market/USD Coin.csv",
        'polyio': "../data/polyio_data/adjusted/USDC.csv"
    },
    {
        'crypto': 'USDT',
        'aave': "../data/aave_data/Core Market/Tether.csv",
        'polyio': "../data/polyio_data/adjusted/USDT.csv"
    }
]

def combine_on_datetime(csv_path1, csv_path2):
    df1 = pd.read_csv(csv_path1)
    df2 = pd.read_csv(csv_path2)
    df1['date-time'] = pd.to_datetime(df1['date-time'], utc=False).dt.tz_localize(None)
    df2['date-time'] = pd.to_datetime(df2['date-time'], utc=False).dt.tz_localize(None)
    merged_df = pd.merge(df1, df2, on='date-time', how='inner')
    return merged_df

def get_data(crypto: str) -> pd.DataFrame:
    for data in data_src:
        if crypto in data['crypto']:
            return combine_on_datetime(data['aave'], data['polyio'])
    raise Exception("Crypto not found!")