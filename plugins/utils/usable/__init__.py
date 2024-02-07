# 初始化读取配置文件
import time

from org.breaktheheli.config import Config

cfg = Config()

print('如果你看到了这条消息，那么所有的插件都已经正常加载了\n'
      f'完成websocket链接后可以在QQ中使用{cfg.command_start}{cfg.command_sep}ping来检查bot的可用性')