from __future__ import absolute_import
import requests
from sqlalchemy.orm import Session
from internal.repository.user_actions import get_user_by_private_key


ROOT_public_key ='0x9ad39Af9b0fCEFFA20504A9316d85A0c645d592c'
ROOT_private_key = 'e563a6a212c9e6df8c656e90690e438b70ea42ec6837e574b28ca66cd156b011'
base_url = 'https://hackathon.lsp.team/hk'


def get_balance(public_key: str):
    r = requests.get('{}/v1/wallets/{}/balance'.format(base_url, public_key))
    return r.json()


def transfer_rubles(db: Session, from_private_key: str, to_public_key: str, amount: float):
    if amount > get_balance(get_user_by_private_key(db, from_private_key)):
        return 
    r = requests.post('{}/v1/transfers/ruble'.format(base_url), data={
        "fromPrivateKey": from_private_key,
        "toPublicKey": to_public_key,
        "amount": amount
    })
    return r.json()

def create_nft(id: int, to_public_key: str):
    r = requests.post('{}/v1/transfers/ruble'.format(base_url), data={
        "toPublicKey": to_public_key,
        "uri": str(id),
        "nftCount": 1
    })
    return r.json()

def get_nft_tockens_by_hash(transaction_hash: str):
    r = requests.post('{}/v1/nft/generate/{transactionHash}'.format(base_url, transaction_hash))
    return r.json()["tokens"][0]


def nft_change(from_private_key: str, to_public_key: str, token_id: int):
    r = requests.post('{}/v1/transfers/nft'.format(base_url), data={
        "fromPrivateKey": from_private_key,
        "toPublicKey": to_public_key,
        "tokenId": token_id
    })
    return r.json()