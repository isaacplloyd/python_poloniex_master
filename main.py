import poloniex

polo = poloniex.Poloniex()

print(polo('returnTicker')['USDT_LTC']['last'])
