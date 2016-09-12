import hashlib
import hmac
import json
import urllib

import time

import requests

from basewrapper import BaseWrapper


class PoloniexWrapper(BaseWrapper):

    def __init__(self, api_key, api_secret, currency_pair):
        super(PoloniexWrapper, self).__init__(api_key, api_secret, currency_pair)
        self.base_uri = 'https://poloniex.com'

    def get_hash(self, data):
        post_data = urllib.urlencode(data)
        return hmac.new(str(self.api_secret), post_data, hashlib.sha512).hexdigest()

    def api_request(self, method, data={}):
        data['command'] = method
        data['nonce'] = int(time.time() * 1000)
        headers = {
            'Sign': self.get_hash(data),
            'Key': self.api_key
        }
        r = requests.post(
            url='{}/tradingApi'.format(self.base_uri),
            headers=headers,
            data=data
        )
        try:
            return r.json()
        except ValueError as e:
            return {'error': True, 'message': '{}: {}'.format(e.message, r.text)}

    def get_balances(self):
        balances = self.api_request('returnBalances')
        return balances

    def get_balance(self, currency):
        balances = self.get_balances()
        return balances[currency.upper()]

    def place_order(self, order_type, amount, price, currency_pair):
        data = {
            'currencyPair': currency_pair,
            'rate': price,
            'amount': amount,
            'immediateOrCancel': 1
        }
        if order_type == 'bid':
            return self.api_request('buy', data)
        else:
            return self.api_request('sell', data)

    def get_order_book(self, currency_pair=None):
        if currency_pair is None:
            currency_pair = 'all'
        r = requests.get(
            url='{}/public?command=returnOrderBook&currencyPair={}'.format(
                self.base_uri,
                currency_pair
            )
        )
        try:
            return r.json()
        except ValueError as e:
            return {'error': True, 'message': '{}: {}'.format(e.message, r.text)}

    def get_top_orders(self, currency_pair=None):
        order_book = self.get_order_book(currency_pair)
        return {'bid': order_book['bids'][0], 'ask': order_book['asks'][0]}