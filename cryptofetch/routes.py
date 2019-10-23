from flask import render_template, request, url_for, flash, redirect, request
from cryptofetch import app, db
from flask_sqlalchemy import SQLAlchemy
from cryptofetch.models import CryptoCurrency
from cryptofetch.coinmarket import push_data_to_db


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    push_data_to_db()
    cryptos = CryptoCurrency.query.all()
    if request.is_xhr:
        template_name = 'ajax.html'
        flash('Api data loaded successfuly', 'success')
    else:
        template_name = 'home.html'
    return render_template(template_name, title="CryptoFetch", cryptos=cryptos)
