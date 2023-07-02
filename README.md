# Yobit API Wrapper
This project is a simple Python wrapper for the Yobit cryptocurrency exchange's API. This script makes it easy to interact with the Yobit API to perform tasks such as retrieving market information, placing trades, and more.

# Installation
This project requires Python 3.7+ and the requests library. You can install requests with pip:

pip install requests

# Setup
The config.py file should contain your API credentials (API_KEY and API_SECRET) obtained from your Yobit account. It should look something like this:

API_KEY = 'your-api-key'
API_SECRET = 'your-api-secret'

# Usage
The script contains several functions that correspond to different actions that can be performed through the Yobit API. Here's a brief description of each function:

<code>get_info()</code>: Returns general info about the Yobit exchange.

get_ticker(coin1="btc", coin2="usd"): Returns the ticker info for a specified trading pair.

get_last_order(coin1="btc", coin2="usd", limit=150): Returns the last 150 orders for a specified trading pair.

get_trades(coin1="btc", coin2="usd", limit=150): Returns the last 150 trades for a specified trading pair.

get_user_info(): Returns info about the user's account.

get_deposit_adress(coin_name="btc"): Returns the deposit address for a specified coin.

buy_coin(coin1="btc", coin2="usdtbep20", rate=None, amount=0): Places a buy order for a specified trading pair at a given rate and amount.

sell_coin(coin1="usdt", coin2="rur", rate=None, amount=0): Places a sell order for a specified trading pair at a given rate and amount.

cancel_order(order_id): Cancels an order with a given order ID.

To use any of these functions, simply import them into your Python script and call them. For example:
<code>
from yobit_api_wrapper import get_ticker
print(get_ticker("btc", "usd"))
</code>

# Contribution
Please feel free to fork this repository and submit pull requests. All contributions are welcome.

# License
This project is licensed under the MIT License.

# Disclaimer
This script is provided as is, without any guarantees or liability. Trading cryptocurrency involves risk and could result in the loss of capital. You should use this script with caution, and at your own risk.
