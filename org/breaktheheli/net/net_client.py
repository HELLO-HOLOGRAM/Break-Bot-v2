import aiohttp

from org.breaktheheli.config import Config
from org.breaktheheli.logger import Logger

logger = Logger('net.txt')


class AllConnector:
    def __init__(self):
        self.payload = {}
        self.status_code = None
        self.user_id = None
        self.response = None
        # 读取配置
        cfg = Config()
        self.uri = cfg.client_address

    async def get_uid(self, text):
        async with aiohttp.ClientSession() as session:
            async with session.get(url=self.uri + '/chime/auth', params={
                'text': text
            }) as res:
                if res.status != 504:
                    payload = eval(await res.text())
                    self.user_id = payload["userId"]
                    self.status_code = res.status
                    self.payload = payload
        return payload
