import ccxt
import pprint

f = open("./binance.key")
lines = f.readlines()
api_key = lines[0].strip()
secret = lines[1].strip()
f.close()

exchange = ccxt.binance(config={
    'apiKey': api_key,
    'secret': secret,
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future'
    }
})

markets = exchange.load_markets()
btc_usdt_limits = markets['BTC/USDT']['limits']
xrp_usdt_limits = markets['XRP/USDT']['limits']

pprint.pprint(btc_usdt_limits)
pprint.pprint(xrp_usdt_limits)