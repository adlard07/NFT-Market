import csv
import pandas as pd
from flask_cors import CORS
from address import Address
from transaction import MyTransations
from flask import Flask, request, jsonify

app = Flask(__name__)
cors = CORS(app)


@app.route('/orders', methods=['POST'])
def order():
    data = request.get_json()
    acc2 = data.get('dataId')
    quantity = data.get('enteredValue')
    
    transfer = MyTransations()
    order = transfer.transaction(acc2, quantity)
    order = jsonify({
            'Seller': acc2,
            'quantity': quantity,
            'Message': 'Transaction Sucessful!',
        })
    
    return order

@app.route('/addresses', methods=['GET'])
def account():
    all_accounts = Address()
    acc_bal = all_accounts.addresses()
    return acc_bal

    
if __name__ == '__main__':
    app.run(debug=True, port=7000)