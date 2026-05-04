from abc import ABC, abstractmethod
from config import Config
from utils.logger import log

class BaseAgent(ABC):
    def __init__(self, name):
        self.name = name
        self.config = Config()
        log.info(f"Agent [{self.name}] 初始化完成。")

    @abstractmethod
    async def think(self, context):
        pass

    @abstractmethod
    async def act(self, context):
        pass