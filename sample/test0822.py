from vyper.utils import keccak256

from ini import my_address, private_key, chain_id, bytecode, abi, w3
from ini import accounts
from Crypto.Hash import keccak

# 调用deploy.py会获得contract_address
# from web3.auto import w3

# abi = []

contract_address = '0xa25d0CfF56d304462cC6f5e9bD486C0489352226'

nonce = w3.eth.get_transaction_count(my_address)
# account = accounts[0]
# print(account)
# 实例化合约对象
storage = w3.eth.contract(address=contract_address, abi=abi)
# 调用addPerson方法
# transaction = storage.functions.addPerson('二两', 28).buildTransaction({
#     "chainId": chain_id,
#     "from": my_address,
#     "nonce": nonce
# })
# 签名

# keccak_hash = keccak.new(digest_bits = 256)
# keccak_hash.update(b'0')#044852b2a670ade5407e78fb2863c51de9fcb96542a07186fe3aeda6bb8a116d
# keccak_hash.update(b'a') 3ac225168df54212a25c1c01fd35bebfea408fdac2e31ddd6f80a4bbf9a5f1cb
# b'' 这个是字符转byte 的方法 因为hex 0 为不可见字符 所以我们没有办法通过字符转换
# a_bytes = bytes.fromhex('')
# # bytes.fromhex('61')等于 b'a'
# print('aaa:', a_bytes)
# # 打印为 b'a'

# data = keccak256("addPerson(string,uint256)")[:4]
# data += bytes32("二两")
# data += bytes32(28)


signed_transaction = w3.eth.account.sign_transaction(
    dict(
        nonce = w3.eth.get_transaction_count(my_address),
        gas = 21000,
        gasPrice = 10000,
        to = contract_address,
        value = 1,
        # data = data,
    ),
    private_key=private_key)
# 发送交易

print(my_address)
bal = w3.eth.get_balance(my_address)
print("balance: ", bal)

tx_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
print('add new Person to contract...')
# 等待交易完成
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
# 获得people数组中存储的值
# result = storage.functions.people(0).call()
# print(f'get person info: {result}')
