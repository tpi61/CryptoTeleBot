import requests
import json

from config import keys

class APIException(Exception):
    pass

class CryptoConvertor:
    @staticmethod
    def get_price(quote: str,base: str,amount: str):

        if quote == base: raise APIException(f'The same quote and base')
        if not keys.get(quote): raise APIException(f'Currency {quote} isn\'t in keys')
        if not keys.get(base): raise APIException(f'Currency {base} isn\'t in keys')
        if not amount.isdigit(): raise APIException(f'{amount} is not digit')
        
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote}&tsyms={base}')
        per_price = json.loads(r.content)[base]
        return per_price*int(amount)