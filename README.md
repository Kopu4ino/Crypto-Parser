# Yobit API Wrapper
This project is a simple Python wrapper for the Yobit cryptocurrency exchange's API. This script makes it easy to interact with the Yobit API to perform tasks such as retrieving market information, placing trades, and more.

# Installation
This project requires Python 3.7+ and the requests library. You can install requests with pip:

<code>pip install requests</code>

# Setup
The config.py file should contain your API credentials (API_KEY and API_SECRET) obtained from your Yobit account. It should look something like this:

<code>API_KEY = 'your-api-key'
API_SECRET = 'your-api-secret'</code>

# Usage
The script contains several functions that correspond to different actions that can be performed through the Yobit API. Here's a brief description of each function:

<code>get_info()</code>: Returns general info about the Yobit exchange.

<code>get_ticker(coin1, coin2)</code>: Returns the ticker info for a specified trading pair.

<code>get_last_order(coin1, coin2, limit=150)</code>: Returns the last 150 orders for a specified trading pair.

<code>get_trades(coin1, coin2, limit=150)</code>: Returns the last 150 trades for a specified trading pair.

<code>get_user_info()</code>: Returns info about the user's account.

<code>get_deposit_adress(coin_name)</code>: Returns the deposit address for a specified coin.

<code>buy_coin(coin1, coin2, rate=None, amount=0)</code>: Places a buy order for a specified trading pair at a given rate and amount.

<code>sell_coin(coin1, coin2, rate=None, amount=0)</code>: Places a sell order for a specified trading pair at a given rate and amount.

<code>cancel_order(order_id)</code>: Cancels an order with a given order ID.

To use any of these functions, simply import them into your Python script and call them. For example:
<code>
from yobit_api_wrapper import get_ticker
print(get_ticker("btc", "usd"))
</code>

# Disclaimer
This script is provided as is, without any guarantees or liability. Trading cryptocurrency involves risk and could result in the loss of capital. You should use this script with caution, and at your own risk.
