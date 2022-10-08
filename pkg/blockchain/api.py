import requests


public_key ='0x9ad39Af9b0fCEFFA20504A9316d85A0c645d592c'
private_key = 'e563a6a212c9e6df8c656e90690e438b70ea42ec6837e574b28ca66cd156b011'
base_url = 'https://hackathon.lsp.team/hk'


def get_balance(public_key: str):
    r = requests.get('{}/v1/wallets/{}/balance'.format(base_url, public_key))
    return r.json()

def transfer_rubles():
    pass

def create_nft():
    pass



print(get_balance())