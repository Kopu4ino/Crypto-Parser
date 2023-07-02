import requests
import time
from urllib.parse import urlencode
import hmac
from config import API_SECRET, API_KEY
import hashlib


#  PUBLIC API METHODS
def get_info():
    response = requests.get(url="https://yobit.net/api/3/info")

    # with open("info.txt", "w") as file:
    #     file.write(response.text)
    return response.text


# получаем информацию о торговой паре
def get_ticker(coin1="btc", coin2="usd"):
    response = requests.get(url=f"https://yobit.net/api/3/ticker/{coin1}_{coin2}?ignore_invalid=1")

    return response.json()


# получаем 150 последних ордеров на покупку и продажу
def get_last_order(coin1="btc", coin2="usd", limit=150):
    response = requests.get(url=f"https://yobit.net/api/3/depth/{coin1}_{coin2}?limit={limit}&ignore_invalid=1")

    with open("depth.txt", "w") as file:
        file.write(response.text)

    # сумма всех выставленных на закуп ордеров
    bids = response.json()[f"{coin1}_usd"]["bids"]
    total_bids_amount = 0
    for item in bids:
        price = item[0]
        coin_amount = item[1]

        total_bids_amount += price * coin_amount

    return f"Total bids : {total_bids_amount}"


# получаем 150 последних совершенных сделок
def get_trades(coin1="btc", coin2="usd", limit=150):
    response = requests.get(url=f"https://yobit.net/api/3/trades/{coin1}_{coin2}?limit={limit}&ignore_invalid=1")

    with open("trades.txt", "w") as file:
        file.write(response.text)

    total_trade_ask = 0
    total_trade_bid = 0

    for iteam in response.json()[f"{coin1}_{coin2}"]:
        if iteam["type"] == "ask":
            total_trade_ask += iteam["price"] * iteam["amount"]
        else:
            total_trade_bid += iteam["price"] * iteam["amount"]

    info = f"[-] TOTAL {coin1} SELL: {total_trade_ask:.2f} $\n[+] TOTAL {coin1} BUY: {total_trade_bid:.2f} $"
    return info


# TRADE API METHODS

def get_user_info():
    values = dict()
    values["method"] = "getInfo"
    values["nonce"] = str(int(time.time()))
    # print(values)

    body = urlencode(values).encode("utf-8")
    # print(body) --> methods=getInfo&nonce=1651496290

    # Создаем подпись для запроса
    sign = hmac.new(API_SECRET.encode("utf-8"), body, hashlib.sha512).hexdigest()
    # print(sign)

    headers = {
        "key": API_KEY,
        "sign": sign
    }

    response = requests.post(url="https://yobit.net/tapi/", headers=headers, data=values)
    return response.json()


def get_deposit_adress(coin_name="btc"):
    values = dict()
    values["method"] = "GetDepositAddress"
    values["coinName"] = coin_name
    values["need_new"] = 0
    values["nonce"] = str(int(time.time()))

    body = urlencode(values).encode("utf-8")
    sign = hmac.new(API_SECRET.encode("utf-8"), body, hashlib.sha512).hexdigest()

    headers = {
        "key": API_KEY,
        "sign": sign
    }

    response = requests.post(url="https://yobit.net/tapi/", headers=headers, data=values)
    return response.json()


def buy_coin(coin1="btc", coin2="usdtbep20", rate=None, amount=0):
    ticker = get_ticker(coin1, coin2)
    sell_price = ticker[f"{coin1}_{coin2}"]["sell"] if rate is None else rate
    # print(ticker)

    values = dict()
    values["method"] = "Trade"
    values["nonce"] = str(int(time.time()))
    values["pair"] = f"{coin1}_{coin2}"
    values["type"] = "buy"
    values["rate"] = sell_price
    values["amount"] = amount / sell_price

    # return values

    body = urlencode(values).encode("utf-8")
    sign = hmac.new(API_SECRET.encode("utf-8"), body, hashlib.sha512).hexdigest()
    # print(body)

    headers = {
        "key": API_KEY,
        "sign": sign
    }

    response = requests.post(url="https://yobit.net/tapi/", headers=headers, data=values)
    return response.json()


def sell_coin(coin1="usdt", coin2="rur", rate=None, amount=0):
    ticker = get_ticker(coin1, coin2)
    buy_price = ticker[f"{coin1}_{coin2}"]["buy"] if rate is None else rate
    # print(ticker)

    values = dict()
    values["method"] = "Trade"
    values["nonce"] = str(int(time.time()))
    values["pair"] = f"{coin1}_{coin2}"
    values["type"] = "sell"
    values["rate"] = buy_price
    values["amount"] = amount

    # return values

    body = urlencode(values).encode("utf-8")
    sign = hmac.new(API_SECRET.encode("utf-8"), body, hashlib.sha512).hexdigest()
    # print(body)

    headers = {
        "key": API_KEY,
        "sign": sign
    }

    response = requests.post(url="https://yobit.net/tapi/", headers=headers, data=values)
    return response.json()


def cancel_order(order_id):
    values = dict()
    values["method"] = "CancelOrder"
    values["nonce"] = str(int(time.time()))
    values["order_id"] = order_id

    body = urlencode(values).encode("utf-8")
    sign = hmac.new(API_SECRET.encode("utf-8"), body, hashlib.sha512).hexdigest()
    # print(body)

    headers = {
        "key": API_KEY,
        "sign": sign
    }

    response = requests.post(url="https://yobit.net/tapi/", headers=headers, data=values)
    return response.json()


def main():
    # print(get_info())
    # print(get_ticker(coin1="btc", coin2='usdtbep20'))
    # print(get_last_order(coin1="btc"))
    # print(get_last_order(coin1="eth"))
    # print(get_trades(coin1="eth"))
    # TRADE API METHODS
    print(get_user_info())
    # coin_name = input("Enter a coin name ")
    # print(get_deposit_adress(coin_name=coin_name))
    # print(get_ticker(coin1="eth", coin2="usdt"))
    # print(buy_coin(rate=1000))
    # print(buy_coin(coin1="btc", coin2="usdtbep20", rate=1, amount=1))
    # print(cancel_order(1104373728168474))
    # print(sell_coin(coin1="btc", coin2="usdt", rate=35296, amount=0.0001))
    # print(get_ticker(coin1="btc", coin2="usdt"))


if __name__ == '__main__':
    main()
