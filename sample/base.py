import os
import json
from web3 import Web3

# 编译 solidity
# https://github.com/iamdefinitelyahuman/py-solc-x
from solcx import compile_standard, install_solc

with open('/Users/xxx/python-brownie/contracts/Storage.sol', 'r',
          encoding='utf-8') as f:
    storage_file = f.read()

# 下载0.6.0版本的Solidity编译器
install_solc('0.6.0')

# 编译Solidity
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        # Solidity文件
        "sources": {"Storage.sol": {"content": storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    # 编译后产生的内容
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    # 版本，与编写智能合约时Solidity使用的版本对应
    solc_version="0.6.0",
)

# 编译后的结果写入文件
with open('../build/contracts/compiled_code.json', 'w') as f:
    json.dump(compiled_sol, f)
