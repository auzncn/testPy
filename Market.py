class Market:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume
    def __str__(self):
        return ("name：%s\tvolume：%d" % (self.name, self.volume))
x = Market("BTC/USDT", 23155)
print(x.__str__())