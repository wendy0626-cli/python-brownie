```
├───build                # 编译、部署等结果存放目录
│   ├───contracts
│   ├───deployments
│   └───interfaces
├───contracts            # 智能合约的目录
├───interfaces           # 接口的目录
├───reports              # JSON报告文件的目录（使用GUI的用户才会使用）
├───scripts              # 脚本的目录
└───tests                # 测试脚本目录

1.关于添加网络

https://eth-brownie.readthedocs.io/en/v1.12.3/api.html

brownie networks list
brownie networks --help

add <env> <id> [key=value, ...]  Add a new network
delete <id> 

brownie networks add Development dev cmd=ganache-cli host=http://127.0.0.1:8545
![image](https://user-images.githubusercontent.com/77438845/186085683-feaac235-1fcc-48ae-97b5-3947089a2ead.png)
brownie networks delete dev 
![image](https://user-images.githubusercontent.com/77438845/186086056-cf3874c1-7fde-4dee-8461-3b5fdd748531.png)
  
brownie run scripts/2_deploy_end.py --network dev
![image](https://user-images.githubusercontent.com/77438845/186086326-76d60e80-007a-4ccb-acb6-446dddf321c7.png)
  
2.关于ganache

Ganache现在有两个版本，
一个是带图形界面的版本，下载地址：
https://github.com/trufflesuite/ganache/releases
另一个这边使用的是命令行版本，github地址：
https://github.com/trufflesuite/ganache-cli

3.关于web3.py原生方法编译部署和测试
使用到了ganache客户端！！！

执行顺序：base.py---ini.py---deploy0822.py---test0822.py(脚本暂时无法传递data参数！)

其中：.env环境变量如下
export RINKEBY_RPC_URL='http://127.0.0.1:7545'
export ACCOUNT_ADDRESS='0x6Aad0eCb2eDA8a6282d86F1D5FA0f502f4807Cf9'
export PRIVATE_KEY='74a58a8d4e169d81d14942e141d3689eb6e0b449ff7161b3016aea908f246250'
export CHAIN_ID=1337

![image](https://user-images.githubusercontent.com/77438845/186117567-e2b171bc-42ba-43e6-a386-8a479370b39d.png)
略

```
