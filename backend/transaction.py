import jsonify
from web3 import Web3
from dataclasses import dataclass

@dataclass
class MyTransations:
    def __init__(self):
        self.ganache_url = 'http://127.0.0.1:7545'
        
    def transaction(self, acc2, quantity):
        
        web3 = Web3(Web3.HTTPProvider(self.ganache_url))

        acc1 = '0xBEbe3513B2A4287beB3CC506444B7A8059658A10'
        private_key = '0xa19a98d89a48bda9f2c26cc852209e2f09a3ac09531dcde74b9fc0b7ea56bf1b'

        nonce = web3.eth.get_transaction_count(acc1)

        tx = {
            'nonce':nonce,
            'to':acc2,
            'value':web3.to_wei(quantity, 'ether'),
            'gas':2000000,
            'gasPrice': web3.to_wei('50', 'gwei')
        }

        signed_tx = web3.eth.account.sign_transaction(tx, private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        hx_hash = web3.to_hex(tx_hash)
        order = {
            'Transaction Hash' : hx_hash,
            'Message' : 'Transaction Sucessful!'
        }
        return order
        