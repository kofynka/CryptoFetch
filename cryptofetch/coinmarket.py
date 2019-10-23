from coinmarketcap import Market
from cryptofetch.models import CryptoCurrency
from flask_sqlalchemy import SQLAlchemy
from cryptofetch import db
import json

results = 10

def get_data_from_market():
    coinmarketcap = Market()
    res = coinmarketcap.ticker(limit=results)   #get crypto data from coinmarketcap
    data = list(iter(res['data'].items()))  #iterates through data and creates easy readable list

    return data


def push_data_to_db():
    db.session.query(CryptoCurrency).delete()   #deletes all rows from db
    db.session.commit() #commits changes to db
    data = get_data_from_market()

    for x in range(results):
        crypto_id = data[x][1]['id']
        name = data[x][1]['name']
        mc = data[x][1]['quotes']['USD']['market_cap']
        market_cap = f'{mc:,.0f}'
        pr = data[x][1]['quotes']['USD']['price']
        if pr >= 1:
            price = f'{pr:,.2f}'
        else:
            price = f'{pr:.6f}'
        symbol = data[x][1]['symbol']
        vol = data[x][1]['quotes']['USD']['volume_24h']
        volume_24h = f'{vol:,.2f}'
        cs = data[x][1]['circulating_supply']
        circulating_supply = f'{cs:,.0f}'
        percent_change_24h = data[x][1]['quotes']['USD']['percent_change_24h']
        percent_change_7d = data[x][1]['quotes']['USD']['percent_change_7d']
        crypto = CryptoCurrency(crypto_id=crypto_id, name=name, market_cap=market_cap, price=price, symbol=symbol, volume_24h=volume_24h, \
        circulating_supply=circulating_supply, percent_change_24h=percent_change_24h, percent_change_7d=percent_change_7d)
        db.session.add(crypto)
        db.session.commit()
