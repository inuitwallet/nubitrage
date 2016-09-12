import json

from decimal import Decimal

from poloniex import PoloniexWrapper
from price_feed import PriceFeed


settings = json.load(open('settings.json'))

poloniex = PoloniexWrapper(
    api_key=settings['poloniex']['api_key'],
    api_secret=settings['poloniex']['api_secret'],
    currency_pair='btc/nbt'
)

price_feed = PriceFeed('BTC', 'USD')
price = Decimal(price_feed.coinmarketcap()['message'])

print(price)

top_orders = poloniex.get_top_orders(currency_pair='BTC_NBT')
top_bid = top_orders['bid']
print(top_bid)
print([Decimal(top_bid[0]) * Decimal(price), top_bid[1]])
top_ask = top_orders['ask']
print(top_ask)
print([Decimal(top_ask[0]) * Decimal(price), top_ask[1]])





