import poloniex

polo = poloniex.Poloniex()
cmd = 'init string'
while cmd != 'exit':
    try:
        cmd = input("Press enter to retrieve USDT_LTC price: ")
    except EOFError:
        pass
    print(polo('returnTicker')['USDT_LTC']['last'])
