import requests

class WalletApi(object):
    """
    This Model Handles All Requests to the Forging Block API for Bitcoin Wallet
    """

    def __init__(self):
        self.email = MAIL
        self.password = PASS
        self.token = FORGING_BLOCK_TOKEN
        self.xpub = ""
        self.mnemonic = ""
        self.trade = ""
        self.token = ""
        self.store = ""


    def create_wallet(self):
        try:
            res1 = requests.post("https://wallet-api.forgingblock.io/v1/create-btc-mnemonic").json()
            self.mnemonic = res1['mnemonic']

            payload = {
                'mnemonic': self.mnemonic,
                'number': 0
            }
            res2 = requests.post("https://wallet-api.forgingblock.io/v1/retrieve-btc-wallet-address", data=payload).json()
            self.address = res2['address']
            return self.mnemonic, self.address

        except Exception as e:
            return None

    def get_xpub(self):
        payload = {
            'mnemonic': self.mnemonic,
        }
        res = requests.post("https://wallet-api.forgingblock.io/v1/generate-btc-xpub", data=payload).json()
        self.xpub = res['xpub']

        return self.xpub


    def create_store(self, name):
        payload = {
            'email': self.email,
            'password': self.password,
            'xpub': self.xpub,
            'name': name
        }
        result = requests.post("https://api.forgingblock.io/create-store", data=payload).json()
        
        print(result)
        self.trade = result['trade']
        self.token = result['token']
        self.store = result['store']
        return self.trade, self.token, self.store

    
    def connect_store(self):
        try:
            payload = {
                'email': self.email,
                'password': self.password,
                'address': self.address,
                'store': self.store
            }
            result = requests.post("https://api.forgingblock.io/connect-wallet-btc-single", data=payload).json()
            return result['success']

        except Exception as e:
            return "Failed"


    
    def create_invoice(self, trade):
        try:
            payload = {
                'trade': trade.trade,
                'token': trade.token,
                'amount': trade.price,
                'currency': trade.currency,
            }
            result = requests.post('https://api.forgingblock.io/create-invoice', data=payload).json()
            
            invoice = result['id']
            return invoice

        except Exception as e:
            return "Failed"

    def get_payment_url(self, invoice):
        try:
            payload = {
                'trade': self.trade,
                'token': self.token,
                'invoice': invoice
            }
            result = requests.post('https://api.forgingblock.io/check-invoice', data=payload).json()
            return result['url']

        except Exception as e:
            return "Failed"

    def check_status(self, trade):
        try:
            payload = {
                'trade': trade.trade,
                'token': trade.token,
                'invoice': trade.invoice
            }
            result = requests.post('https://api.forgingblock.io/check-invoice-status', data=payload).json()
            return result['status']

        except Exception as e:
            return "Failed"


    def send_money(self, trade, wallet):
        try:
            payload = {
                'mnemonic': trade.mnemonic,
                'number': 0
            }
            # Get Wif
            resp1 = requests.post("https://wallet-api.forgingblock.io/v1/generate-btc-wif", data=payload).json()
            
            # Get rate
            resp2 = requests.post("https://wallet-api.forgingblock.io/v1/find-btc-rates").json()

            amountToSend = float(trade.price) / float(resp2['usdRate'])
            amount = '%.5f' % amountToSend

            payload = {
                'orgAddress': trade.address,
                'wif': resp1['wif'],
                'amountToSend': amount,
                'recipientAddress': wallet
            }
            response = requests.post("https://wallet-api.forgingblock.io/v1/send-btc-transaction", data=payload).json()
            return response['txid']

        except Exception as e:
            return "Failed"
        