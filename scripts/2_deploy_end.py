from brownie import accounts, config, network, Storage


def deploy_storage():
    account = get_account()
    # Instantiate Storage contract
    storage = Storage.deploy({"from": account})
    # call addPerson function
    transaction = storage.addPerson('二两', 28, {"from": account})
    # wait transaction finish
    transaction.wait(1)
    # call people function to get data from people array
    result = storage.people(0)
    print('result: ', result)


def get_account():
    if network.show_active() == 'development':
        return accounts[0]
    if network.show_active() == 'dev':
        return accounts[0]
    else:
        # add new account to brownie accounts
        # account config data from brownie-config.yaml
        return accounts.add(config['wallets']['account_key'])


def main():
    deploy_storage()

