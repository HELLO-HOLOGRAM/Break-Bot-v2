import os
import yaml


class Config:
    """
    用于读写yaml配置文件的类，实例化时读取配置文件中的值并存储到内存中。
    如果检测到没有对应的配置文件则自动根据模板生成一个配置文件并进行默认赋值。
    """
    # Bot默认值
    bot_name = 'break-bot'
    version = '1.0'

    # web-gui默认值
    gr_ip = '127.0.0.1'
    gr_port = 8051

    # quart-server默认值
    server_ip = '127.0.0.1'
    server_port = 8050

    # remote-client默认值
    client_address = 'http://127.0.0.1:8050'

    # MongoDB Server默认值
    db_ip = '127.0.0.1'
    db_port = 27017
    db_username = 'breakbot'
    db_passwd = ''

    def __init__(self):
        # 检测是否存在目录下对应的文件
        if not os.path.exists('config/bot_config.yml'):
            self._generate_config_file()
            print('未检测到配置文件，自动生成了 config/bot_config.yml ')
        else:
            self.get_config()
        pass

    def _generate_config_file(self):
        # 检测是否存在文件夹
        if not os.path.exists('config/'):
            os.mkdir('config')
        # 生成一个配置文件
        config = (f"# Auto Generate By BreakBotV2\n\n"
                  f"# 项目名称\n"
                  f"# 这个配置只会影响一部分地方显示的项目名称，改不改似乎都没什么区别\n"
                  f"bot-name: {self.bot_name}\n"
                  f"version: {self.version}\n"
                  f"\n"
                  f"# Remote Client设置\n"
                  f"# 配置模拟Client的连接地址\n"
                  f"# 本地运行一般无须修改，远程连接请修改成对应的url\n"
                  f"# 请不要在url的末尾添加'/'!\n"
                  f"client-address: {self.client_address}\n"
                  f"\n"
                  f"# MongoDB设置\n"
                  f"# 配置数据库的连接地址\n"
                  f"db-ip: {self.db_ip}\n"
                  f"db-port: {self.db_port}\n"
                  f"db-username: {self.db_username}\n"
                  f"db-passwd: {self.db_passwd}\n")
        # 写入配置文件
        with open('config/bot_config.yml', 'w', encoding='utf-8') as c:
            c.write(config)
            c.close()
        pass

    def get_config(self):
        """
        调用这个方法会使Config实例重新读取config.yaml。
        :return: None
        """
        # 读取配置文件
        with open('config/bot_config.yml', 'r', encoding='utf-8') as file:
            cfgs = yaml.load(file, Loader=yaml.FullLoader)
            file.close()
        # 赋值
        self.bot_name = cfgs['bot-name']
        self.version = cfgs['version']
        self.client_address = cfgs['client-address']
        self.db_ip = cfgs['db-ip']
        self.db_port = cfgs['db-port']
        self.db_username = cfgs['db-username']
        self.db_passwd = cfgs['db-passwd']
