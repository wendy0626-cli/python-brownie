import json
import os

from dotenv import load_dotenv
from web3 import Web3

load_dotenv()

w3 = Web3(Web3.HTTPProvider(os.getenv("RINKEBY_RPC_URL")))
# chain_id = 1337

my_address = os.getenv("ACCOUNT_ADDRESS")
private_key = os.getenv("PRIVATE_KEY")
chain_id = int(os.getenv("CHAIN_ID"))

with open("/Users/xxx/python-brownie/build/contracts/compiled_code.json", 'r',
          encoding='utf8') as fp:

    json_data = json.load(fp)
    print('这是文件中的json数据：', json_data)
    print('这是读取到文件数据的数据类型：', type(json_data))

    # 智能合约编译后的字节码（上链的数据）
    bytecode = json_data["contracts"]["Storage.sol"]["Storage"]["evm"]["bytecode"]["object"]
    print('这是文件数据中的bytecode', bytecode)
    # ABI (Application Binary Interface)，用于与智能合约中的方法进行交互的接口
    abi = json.loads(json_data["contracts"]["Storage.sol"]["Storage"]["metadata"])["output"]["abi"]
    print('这是文件数据中的abi', abi)
