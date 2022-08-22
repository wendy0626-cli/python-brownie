# python-brownie

# 简介
## Brownie框架是基于Python编写的智能合约开发框架，主要是基于Web3.py这个库开发而来。
## Brownie可以部署.sol、.py格式的智能合约，通过pytest进行智能合约测试。
## 它可以帮我们快速完成编译、部署、测试等智能合约开发的全流程。

# 环境
```
1.1 安装nodejs、python3
1.2 安装brownie------pip3 install eth-brownie
1.3 安装ganache-cli------npm install -g ganache-cli
1.4 检查brownie------brownie --help/brownie --version
```

# 工程python-brownie
```
2.1 创建文件与文件夹
    打开控制台终端，依次输入如下命令：
    mkdir python-brownie
    cd python-brownie
    brownie init
    touch brownie-config.yaml
    touch .env
    备注：a)brownie的配置文件:brownie-config.yaml（已是修改后版本），另有备份配置文件0816.yaml
         b)brownie的环境变量文件:.env，每个key通过官方获得即https://etherscan.io/、https://infura.io/
         c)brownie的工程的目录结构:目前只用到了contracts、scripts、tests
2.2 编写智能合约、编写测试脚本、编写部署脚本
    在contracts目录，创建一个智能合约文件: HelloERC20.sol
    在tests目录，创建一个测试脚本文件: 1_func_test.py
    在scripts目录，创建一个部署脚本文件: 1_deploy_token.py
2.3 进行部署和测试
    1）部署合约到Rinkeby
    ## 使能.env环境
    source .env
    ## 部署到Rinkeby
    brownie run scripts/1_deploy_token --network rinkeby
    效果如下：
    得到HelloERC20.sol的合约地址为: 
    2）测试HelloERC20合约
    ## 先启动ganache-cli
    ganache-cli
    ## 运行测试脚本
    ## 方法一：禁用print
    brownie test tests/1_func_test.py
    ## 方法二：启用print
    brownie test tests/1_func_test.py -s
    效果如下：
    备注：a）测试脚本的默认网络要配成development，配成其他没有作用（暂时不知道是什么原因）
         b）屏蔽测试脚本部分代码，日志不出现提示
         c）ganache客户端连不上，还需要再连接试试

    ------HelloERC20 deployed at: 0x2295E13eaac293Cff6EF9895a09cACe0692a6E23
    ------https://rinkeby.etherscan.io/address/0x2295e13eaac293cff6ef9895a09cace0692a6e23#code
    ------chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#
    ------验证和发布合约源代码———	验证成功！
    ------读合约和写合约，
    ------通过测试网浏览器和小狐狸钱包插件，查看操作记录。

2.4 编写其他智能合约和部署脚本
    编辑智能合约文件- vim contracts/BrownieDemo.sol
    编译智能合约文件- brownie compile
    查看编译通过后结果- ls build/contracts
    编辑部署合约文件- vim scripts/deploy.py
    运行部署脚本命令是：brownie run scripts/deploy.py --network rinkeby

    ------重新修改deploy.py文件，部署合约成功
    ------FooBar deployed at: 0x8C78d5e81F58DCb3AF7B09106680421F1F35e758
    ------https://rinkeby.etherscan.io/address/0x8C78d5e81F58DCb3AF7B09106680421F1F35e758#code
    ------会在部署同时，直接验证成功!
    ------写合约
    ------通过测试网浏览器和小狐狸钱包插件，查看操作记录。

2.5 远程调用合约方法
    通过Brownie控制台，远程调用合约方法
    brownie console --network rinkeby
    和浏览器写合约操作一样！    
2.6 其他其他
    PyCharm CE安装支持.sol语言插件

    Ropsten：一个POW的区块链，非常类似于目前以太坊主网
    Kovan：一个POA的区块链
    Rinkeby：一个POA的区块链
    Goerli：一个POS的区块链，对标ETH2.0

2.7 参考网站
    https://blog.csdn.net/weixin_30230009/article/details/121173553
    https://blog.csdn.net/sanqima/article/details/121229613
    https://bbs.csdn.net/topics/605988722
    https://blog.csdn.net/changyixue/article/details/124859635
```