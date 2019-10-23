from cryptofetch import db


class CryptoCurrency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    crypto_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.Text, nullable=False)
    market_cap = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    symbol = db.Column(db.Text, nullable=False)
    volume_24h = db.Column(db.Integer, nullable=False)
    circulating_supply = db.Column(db.Integer, nullable=False)
    percent_change_24h = db.Column(db.Integer, nullable=False)
    percent_change_7d = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"CryptoCurrency('{self.crypto_id}', '{self.name}', '{self.market_cap}', '{self.price}', '{self.symbol}', '{self.volume_24h}', \
        '{self.circulating_supply}', '{self.percent_change_24h}', '{self.percent_change_7d}')"