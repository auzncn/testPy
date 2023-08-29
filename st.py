import pandas as pd
import numpy as np
import ccxt

exchange = ccxt.binance({
    'proxies': {
        'http': 'http://localhost:1080',
        'https': 'http://localhost:1080',
    },
})

symbol = 'BTC/USDT'
timeframe = '4h' # 4小时
klines = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=1000)
df = pd.DataFrame(data=klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')


df['H-L'] = df['high'] - df['low']
df['H-PC'] = abs(df['high'] - df['close'].shift(1))
df['L-PC'] = abs(df['low'] - df['close'].shift(1))
df['TR'] = df[['H-L', 'H-PC', 'L-PC']].max(axis=1)
df['ATR'] = df['TR'].rolling(10).mean()

df['UB'] = df['high'] + 3 * df['ATR']
df['LB'] = df['low'] - 3 * df['ATR']

df['Trend'] = 0
for i in range(10, len(df)):
    if df['close'][i] > df['UB'][i-1]:
        df['Trend'][i] = 1
    elif df['close'][i] < df['LB'][i-1]:
        df['Trend'][i] = -1
    else:
        df['Trend'][i] = df['Trend'][i-1]

df['Supertrend'] = np.nan
for i in range(10, len(df)):
    if df['Trend'][i] == 1:
        df['Supertrend'][i] = df['LB'][i]
    elif df['Trend'][i] == -1:
        df['Supertrend'][i] = df['UB'][i]
    else:
        df['Supertrend'][i] = df['Supertrend'][i-1]
        if df['Supertrend'][i] > df['UB'][i]:
            df['Supertrend'][i] = df['UB'][i]
        elif df['Supertrend'][i] < df['LB'][i]:
            df['Supertrend'][i] = df['LB'][i]

print(df)



