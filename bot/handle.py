from config import word, command_text
import os
import sys
import coloredlogs
import logging.handlers
from telethon import TelegramClient, sync, events
# lib完畢

from config import base
base = base.base()
api_id = base['api_id']
api_hash = base['api_hash']
logging_level = base['logging_level']
log_file_path = base['log_file_path']
log_format = base['log_format']
plugins_path = base['plugins_path']
Language = base['Language']
lg = Language
# 獲取基礎資訊完畢

cw = word.text()
ct = command_text.command()
# 獲取命令、文字完畢

logger = logging.getLogger(__name__)
handler1 = logging.StreamHandler(sys.stdout)
handler2 = logging.handlers.TimedRotatingFileHandler(
    filename=log_file_path,
    when='D',
    encoding='utf-8'
)
formatter = logging.Formatter(log_format)
handler1.setFormatter(formatter)
handler2.setFormatter(formatter)

logger.setLevel(logging_level)
handler1.setLevel(logging_level)
handler2.setLevel(logging_level)

logger.addHandler(handler1)
logger.addHandler(handler2)

coloredlogs.install(level=logging_level, logger=logger)
# logger設定完畢

client = TelegramClient('TMAR', api_id, api_hash)
client.start()
# client啟動完畢


class handle:
    def __init__(self):
        logger.info('=========>>>>>>>>>>start<<<<<<<<<<=========')
        logger.info('logging is ready')
        self.loadPlugins()

    def loadPlugins(self):
        for filename in os.listdir(plugins_path):
            if not filename.endswith(".py") or filename.startswith("_"):
                continue
            self.runPlugin(filename)

    def runPlugin(self, filename):
        pluginName = os.path.splitext(filename)[0]
        logger.debug(plugins_path)
        plugin = __import__(
            f"{plugins_path.replace('/','.')}.{pluginName}",
            fromlist=[pluginName]
        )
        plugin.run(client, logger, lg, ct, cw)
        logger.info(f'{pluginName} load_ed.')

    def run(self):
        logger.info('client is start!')
        client.run_until_disconnected()
