import requests


class PriceFeed(object):

    def __init__(self, base, relative):
        self.base = base
        self.rel = relative

    def bitfinex(self):
        r = requests.get(
            url='https://api.bitfinex.com/v1/pubticker/{}'.format(
                '{}{}'.format(self.base.lower(), self.rel.lower())
            )
        )
        try:
            data = r.json()
        except ValueError as e:
            return {'error': True, 'message': '{}: {}'.format(e.message, r.text)}
        return {'error': False, 'message': data['last_price']}

    def coinmarketcap(self):
        """
        only gives price in usd
        """
        r = requests.get(
            url='https://api.coinmarketcap.com/v1/ticker/?limit=1'
        )
        try:
            data = r.json()
        except ValueError as e:
            return {'error': True, 'message': '{}: {}'.format(e.message, r.text)}
        for currency in data:
            if currency['symbol'] == self.base.upper():
                return {'error': False, 'message': currency['price_usd']}

