import ccxt
exchange = ccxt.binance({
    'proxies': {
        'http': 'http://localhost:1080',
        'https': 'http://localhost:1080',
    },
})
markets = exchange.load_markets()
print(len(markets))