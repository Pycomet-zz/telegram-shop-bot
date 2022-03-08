from config import *
import requests

class WalletApi(object):
    """
    This Model Handles All Requests to the Forging Block API for Bitcoin Wallet
    """

    def __init__(self):
        self.email = MAIL
        self.password = PASS
        self.token = FORGING_BLOCK_TOKEN
        self.mnemonic = ""

    def create_wallet(self):
        try:
            res1 = requests.post("https://wallet-api.forgingblock.io/v1/create-btc-mnemonic").json()
            self.mnemonic = res1['mnemonic']

            payload = {
                'mnemonic': self.mnemonic,
                'number': 0
            }
            res2 = requests.post("https://wallet-api.forgigblock.io/v1/retrieve-btc-wallet-address", data=payload).json()
            self.address = res2['address']
            return self.mnemonic, self.address

        except Exception as e:
            return None


    def get_balance(self, address):
        try:
            payload = {
                'address': address
            }
            resp = requests.post("https://wallet-api.forgingblock.io/v1/find-btc-address-balance", data=payload).json()
            balance = resp['balance']
            return balance

        except Exception as e:
            return "Failed"

    def get_balance_usd(self, address):
        try:
            payload = {
                'address': address
            }
            resp = requests.post("https://wallet-api.forgingblock.io/v1/find-btc-address-balance", data=payload).json()
            balance = resp['balanceUsd']
            return balance

        except Exception as e:
            return "Failed"

    def get_rate(self, address):
        try:
            payload = {
                'address': address
            }
            resp = requests.post("https://wallet-api.forgingblock.io/v1/find-btc-address-balance", data=payload).json()
            balance = resp['usdRate']
            return balance

        except Exception as e:
            return "Failed"

    def get_btc_fee(self):
        res = requests.post("https://wallet-api-demo.forgingblock.io/v1/find-btc-fee").json()
        return res['fastestFee'], res['halfHourFee'], res['hourFee']

    def send_money(self, user, amount, wallet):
        try:
            payload = {
                'mnemonic': user.mnemonic,
                'number': 0
            }
            # Get Wif
            resp1 = requests.post("https://wallet-api.forgingblock.io/v1/generate-btc-wif", data=payload).json()
            

            amount = '%.5f' % float(amount)

            # payload = {
            #     'orgAddress': user.address,
            #     'wif': resp1['wif'],
            #     'amountToSend': amount,
            #     'recipientAddress': wallet
            # }
            # response = requests.post("https://wallet-api.forgingblock.io/v1/send-btc-transaction", data=payload).json()
            # return response['txid']
            return "error"

        except Exception as e:
            return "Failed"
        