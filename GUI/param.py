import pandas as pd
import math
import ccxt

def cal_lp_up(exchange, symbol, window=11):
    ohlcv = exchange.fetch_ohlcv(symbol=symbol, timeframe='1d')
    df = pd.DataFrame(ohlcv, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
    pd_ts = pd.to_datetime(df['datetime'], utc=True, unit='ms')
    pd_ts = pd_ts.dt.tz_convert("Asia/Seoul")
    pd_ts = pd_ts.dt.tz_localize(None)
    df.set_index(pd_ts, inplace=True)
    df = df[['open', 'high', 'low', 'close', 'volume']]

    # bollinger bands
    std = df['close'].rolling(window=window).std()
    df['MA'] = df['close'].rolling(window=window).mean()
    df['UB'] = df['MA'] + 2 * std       # Upper Band
    df['LB'] = df['MA'] - 2 * std       # Lower Band

    lower_price = df['LB'].iloc[-1]
    upper_price = df['UB'].iloc[-1]
    return (lower_price, upper_price)

def cal_atr(exchange, symbol, window=14):
    ohlcv = exchange.fetch_ohlcv(symbol=symbol, timeframe='15m')
    df = pd.DataFrame(ohlcv, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
    pd_ts = pd.to_datetime(df['datetime'], utc=True, unit='ms')
    pd_ts = pd_ts.dt.tz_convert("Asia/Seoul")
    pd_ts = pd_ts.dt.tz_localize(None)
    df.set_index(pd_ts, inplace=True)
    df = df[['open', 'high', 'low', 'close', 'volume']]

    # ATR
    tr1 = abs(df['high'] - df['low'])
    tr2 = abs(df['close'].shift(1) - df['high'])
    tr3 = abs(df['close'].shift(1) - df['low'])
    trs = pd.concat([tr1, tr2, tr3], axis=1)

    df['TR'] = trs.max(axis=1)
    df['ATR'] = df['TR'].rolling(window=window).mean()
    return df['ATR'].iloc[-1]

def cal_grid_number(upper_price, lower_price, ATR):
    diff = upper_price - lower_price
    grid_number = math.ceil(diff / ATR)
    return grid_number



if __name__ == "__main__":
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

    #symbol = "BTC/BUSD"
    symbol = "XRP/USDT"
    lower_price, upper_price = cal_lp_up(exchange, symbol)
    atr = cal_atr(exchange, symbol)
    grid_number = cal_grid_number(upper_price, lower_price, atr)
    print(lower_price, upper_price, grid_number)