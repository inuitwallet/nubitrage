
class WrapperBase(object):
    
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
    
    def get_hash(self):
        pass
        
    def api_request(self, method, data):
        pass
        
    def get_balances(self):
        pass
        
    def get_balance(self, currency):
        pass
        
    def place_order(