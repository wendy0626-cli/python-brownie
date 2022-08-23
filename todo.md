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
```
