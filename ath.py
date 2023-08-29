import ccxt

class Market:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume
    def __str__(self):
        return ("name:%s\tvolume:%d" % (self.name, self.volume))

# 初始化币安交易所
exchange = ccxt.binance({
    'proxies': {
        'http': 'http://localhost:1080',
        'https': 'http://localhost:1080',
    },
})
exchange.load_markets()
print(exchange.market('ETH/USDT'))