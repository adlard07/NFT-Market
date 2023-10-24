from transaction import MyTransations
from flask import Flask, request
from address import Address

app = Flask(__name__)

@app.route('/order', methods=['POST'])
def order():
    quantity = request.form['image1-number']
    acc2 = '0xDd95d7409dF2D9c922204F31A912a1a733fD0759'
    transfer = MyTransations()
    order = transfer.transaction(acc2, quantity)
    
    return order

@app.route('/addresses', methods=['GET'])
def account():
    all_accounts = Address()
    acc_bal = all_accounts.addresses()
    return acc_bal

if __name__ == '__main__':
    app.run(debug=True, port=7000)