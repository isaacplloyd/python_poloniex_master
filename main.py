import poloniex

polo = poloniex.Poloniex()
cmd = 'init string'
while cmd != 'exit':
    cmd = input("Press enter to retrieve USDT_LTC price: ")
    print(polo('returnTicker')['USDT_LTC']['last'])
