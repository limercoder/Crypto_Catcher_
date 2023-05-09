import ccxt
import time
print("1 SIMPLE")
print("2 NORMAL")
program = input(": ")
last_coin = input("COIN: ")
kucoin = ccxt.kucoin()
while True:
    symbols = kucoin.load_markets()
    crypto_list = [symbol for symbol in symbols]
   # last_coin = cry
    # pto_list[-1]
    print(last_coin)
    price = kucoin.fetch_ticker(last_coin)['last']
    if price != None:
        price_ = str(price)
        print("Price: " + price_)
        result = (price / 100) * 2
        buy_price = (price + result)  # for buy without risk add procentage
        # $$$$$$$$$$
        amount = (100 / price) #$$$$$$$$
        print("Amount: " + str(amount))
        # sell price
        price25 = (price / 100) * 40 #25 profit
        _price = (price / 100) * 50   #50 profit
        _price_ = (price / 100) * 100  #100% profit
        sell_price = _price + buy_price
        sell_price100 = _price_ + buy_price
        sell_price25 = price25 + buy_price
        sell_amount = amount / 2
        stop_price = price - price25 #stop 25%
        file = open("coin.txt", "r")
        data = file.read()
        file.close()
        if data == last_coin:
            print("[-]Encore")
            time.sleep(1)
        else:

            api = "6451388e80512e00018c14aa"
            secret = "1baf22ead-15fd-4d1f-a8d6-a313546af8791"
            password = ""

            kucoin.apiKey = api
            kucoin.secret = secret
            kucoin.password = password
            params = {
                'stopPrice': stop_price
            }
            try:

                buy_order = kucoin.create_order(last_coin, 'limit', 'buy', amount, buy_price)

                print("[+] Order ID: ", buy_order['id'])
                print("[+] Bought at price " + str(buy_price))
                file = open("coin.txt", "w")
                file.write(last_coin)
                file.close()
                pr_txt = open("price.txt", "w")
                am = open("amount.txt", "w")
                am.write(str(amount))
                am.close()
                pr_txt.write(str(price))
                pr_txt.close()
                time.sleep(2)
                if program == "2":
                    sell_order = kucoin.create_order(last_coin, 'limit', 'sell', sell_amount, sell_price25)
                    print("[+] Created sell order at: " + str(sell_price25))
                    print("[+] Order ID: ", sell_order['id'])

                elif program == "1":
                    price10 = (price / 100) * 10  #10 profit
                    sell_price10 = price + price10
                    sell_order = kucoin.create_order(last_coin, 'limit', 'sell', sell_amount, sell_price10)
                    print("[+] Created sell order at: " + str(sell_price10))
                    print("[+] Order ID: ", sell_order['id'])


            except:
                print("[-]Error")
                time.sleep(1)
    else:
        print("[-] Price None")
        time.sleep(1)




