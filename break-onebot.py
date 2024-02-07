import os
import sys

import nonebot
import cmd
import threading
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
SUPERUSERS={cfg.super_user}
'''
    f.write(env)
    f.close()


# 初始化交互式命令行线程
# noinspection PyMethodMayBeStatic,PyProtectedMember
class BotCmd(cmd.Cmd):
    intro = ''
    prompt = ''

    def do_help(self, arg):
        print('\n- version | 查看当前bot的版本号'
              '\n- superuser | 查看超级用户列表'
              '\n- whitelist | 查看群白名单'
              '\n- supergroup | 查看高级权限群名单'
              '\n- exit | 退出程序\n')

    def do_version(self, arg):
        # 返回当前的bot版本
        print(f"\nBreak Bot V2 {cfg.version}\n"
              "Developed By HELLO-HOLOGRAM\n"
              "2024.")

    def do_exit(self, arg):
        # 退出bot
        print("正在结束运行......")
        os._exit(0)

    def do_superuser(self, arg):
        print('\nBot当前有如下超级用户：')
        for user in cfg.super_user:
            print('- ' + str(user) + '\n')

    def do_whitelist(self, arg):
        print('\nBot当前有如下白名单群：')
        for group in cfg.group_whitelist:
            print('- ' + str(group) + '\n')

    def do_supergroup(self, arg):
        print('\nBot当前有如下高级权限群：')
        for group in cfg.group_superlist:
            print('- ' + str(group) + '\n')


def start_cmd():
    BotCmd().cmdloop()


# 初始化 NoneBot
nonebot.init()

# 注册适配器
driver = nonebot.get_driver()
driver.register_adapter(ConsoleAdapter)

# 在这里加载插件
nonebot.load_plugins("./plugins/common")
nonebot.load_plugins("./plugins/utils")

if __name__ == "__main__":
    # 在另一个线程中启动cmd循环
    cmd_thread = threading.Thread(target=start_cmd, daemon=True)
    cmd_thread.start()

    nonebot.run()
