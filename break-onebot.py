import nonebot
from nonebot.adapters.onebot.v11 import Adapter as ConsoleAdapter  # 避免重复命名

from org.breaktheheli.config import Config

# 初始化读取配置文件
cfg = Config()

# 生成env文件
with open('.env', 'w', encoding='utf-8') as f:
    env = f'''
DRIVER=~quart+~httpx+~websockets
HOST={cfg.ws_host}
PORT={cfg.ws_port}
COMMAND_START=["{cfg.command_start}"]
COMMAND_SEP=["{cfg.command_sep}"]
ONEBOT_ACCESS_TOKEN={cfg.onebot_token}
'''
    f.write(env)
    f.close()

# 初始化 NoneBot
nonebot.init()

# 注册适配器
driver = nonebot.get_driver()
driver.register_adapter(ConsoleAdapter)

# 在这里加载插件
# nonebot.load_builtin_plugins("echo")  # 内置插件
# nonebot.load_plugin("thirdparty_plugin")  # 第三方插件
nonebot.load_plugins("./plugins")  # 本地插件

if __name__ == "__main__":
    nonebot.run()