from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event, GroupMessageEvent
from nonebot.adapters.onebot.v11 import Message

from org.breaktheheli.config import Config

# 初始化读取配置文件
cfg = Config()

ping = on_command(' ping', priority=10, block=True)


@ping.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    if event.group_id in cfg.group_whitelist:
        await ping.send(Message('Pong!'))
