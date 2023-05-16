import sys
import ccxt
import time
import os

while True:
    fiLe = open('coin.txt', 'r')
    symb = fiLe.read().strip()
    coin = symb.split("/")[0]
    file = open("price.txt", "r")
    price = file.read()
    _pr = float(price)
    _price = (_pr / 100) * 3
    final = _pr - _price
    print("[-]Stop price: " + str(price))
    file = open("coin.txt", "r")
    symbol = file.read()
    print("[-]"+symbol)
    kucoin = ccxt.kucoin()
    priceK = kucoin.fetch_ticker(symbol)['last']
    pricek = float(priceK)
    print("[-]Live price: " + str(priceK))
    time.sleep(10)
    pricLst = kucoin.fetch_ticker(symbol)['last']
    prlst = float(pricLst)

    if priceK < _pr:
        _sell = (priceK / 100) * 3
        sell_price = priceK - _sell
        api = "6451388e80512e00018c14aa"
        secret = ""
        password = ""
        kucoin.apiKey = api
        kucoin.secret = secret
        kucoin.password = password

        orders = kucoin.fetch_open_orders(symbol = symbol)
        for order in orders:
            kucoin.cancel_order(id=order['id'], symbol=symbol)
            print("[+]Order canseled")
        try:

            balance = kucoin.fetch_balance()
            amount = balance.get(coin)["total"]
            print("[+]Balance: " + str(amount))
            stop_order = kucoin.create_order(symbol, 'limit', 'sell', amount, sell_price)
            print("[+]Stopped")
            time.sleep(90)

        except:
            pass

    elif prlst < pricek:

        print("[+]Price going down fixing profit")
        api = "63d6d0d912de5c0001297013"
        secret = ""
        password = ""
        kucoin.apiKey = api
        kucoin.secret = secret
        kucoin.password = password
        orders = kucoin.fetch_open_orders(symbol=symbol)
        try:
            for order in orders:
                kucoin.cancel_order(id=order['id'], symbol=symbol)
                print("[+]Order canseled")
        except:
            print("[-]Balance zero")
        try:

            balance = kucoin.fetch_balance()
            _sell_ = (pricLst / 100) * 3
            sell_price1 = pricLst - _sell_
            amount = balance.get(coin)["total"]
            print("[+]Balance: " + str(amount))
            stop_order = kucoin.create_order(symbol, 'limit', 'sell', amount, sell_price1)
            print("[+]Profit fixed")
            time.sleep(90)
        except:
            pass
    else:
        print("[-]Passer")
        time.sleep(3)








