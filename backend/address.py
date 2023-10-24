from web3 import Web3
import pandas as pd

class Address:
    def __init__(self):
        self.ganache_url = "http://127.0.0.1:7545" 
        
    def addresses(self):
        web3 = Web3(Web3.HTTPProvider(self.ganache_url))
        #accounts
        accounts = list(web3.eth.accounts)
        
        #balance
        balance = []
        for addr in accounts:
            bal = web3.eth.get_balance(addr)
            balance.append(bal)
            
        ax = {}
        for i in range(len(balance)):
            ax[accounts[i]]=balance[i]
            
        return (
            ax
            )
        
if __name__=='__main__':
    addr = Address()
    ax = addr.addresses()
    print(ax)