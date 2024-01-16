# Break-Bot-v2

基于NoneBot v2的Python文本交互Bot，对BreakBot v1进行了完全重构并开源。

Hitechnology, Fun and So Fxxking tasty.

同时将数据迁移到MongoDB上，方便日后的维护。

org.breaktheheli.*为项目库文件目录

## 项目结构

- org.breaktheheli.**common** ——  存储各类主要功能
- org.breaktheheli.**utils** ——  存储一些工具函数
- org.breaktheheli.**database** ——  存储操作数据库相关的函数
- org.breaktheheli.**net** ——  网络通讯相关的功能
- org.breaktheheli.config —— 配置文件相关的函数存放在这一类中
- org.breaktheheli.logger —— 配置后封装好的logging函数，可以直接通过调用它来生成日志。  

- plugins/ —— 存放nonebot的插件
- static/ —— 存放静态资源文件
- data/ —— 存放本地存储的数据文件
- config/ —— 存放配置文件
- logs/ —— 存放日志文件  

- break-onebot.py —— 兼容Onebot v11的QQ-Bot  

- README.md —— 仓库介绍文档

## 依赖

BreakBot的开发阶段使用了Python3.10，更高版本理论上只要引入的库都有对应的兼容版本就可以使用，但是并未经过测试。

BreakBot的数据存储使用了MongoDB，主要的数据交换格式为Json（但是配置文件使用yaml，因为好用）。

项目内包含了requirement.txt，你可以通过pip进行安装。

```shell
pip install -r requirement.txt
```

你也可以分别进行安装：

```shell
pip install pyyaml  # 读写yaml配置文件使用的库
pip install pycryptodome  # aes解密加密使用的库
pip install aiohttp  # 异步http(s)请求库
pip install urllib3  # 同步http(s)请求库
pip install requests  # 同步http(s)请求库
pip install fastapi  # 异步api框架，用于搭建服务端
pip install uvicorn[standard]  # 异步网络服务器，作为fastapi的服务端
```

## 使用

配置文件和部分资源文件都会在启动程序时自动生成/下载。  

启动QQ-Bot（使用模拟Client功能需要配置远程服务器！）：

```shell
python3 break-onebot.py
```

## 启动参数

### break-onebot.py

None
