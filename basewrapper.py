
class WrapperException(Exception):
    pass


class BaseWrapper(object):
    
    def __init__(self, api_key, api_secret, currency_pair):
        self.base_uri = ''
        self.api_key = api_key
        self.api_secret = api_secret

    def get_hash(self, data):
        raise WrapperException('Implement logic in subclass')
        
    def api_request(self, method, data={}):
        raise WrapperException('Implement logic in subclass')
        
    def get_balances(self):
        raise WrapperException('Implement logic in subclass')
        
    def get_balance(self, currency):
        raise WrapperException('Implement logic in subclass')
        
    def place_order(self, order_type, amount, price, currency_pair):
        raise WrapperException('Implement logic in subclass')

    def get_orders(self):
        raise WrapperException('Implement logic in subclass')

    def get_order_book(self, currency_pair=None):
        raise WrapperException('Implement logic in subclass')