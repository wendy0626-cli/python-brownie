import os
from brownie import accounts, HelloERC20

initial_supply = 1000000  # 1000000
token_name = "AppleToken"
token_symbol = "APT"


def get_account():
    accAddr = accounts.add(os.getenv('PRIVATE_KEY'))
    return accAddr


def main():
    account = get_account()
    print('account=', account)
    erc20 = HelloERC20.deploy(
        initial_supply, token_name, token_symbol, {"from": account}
    )
