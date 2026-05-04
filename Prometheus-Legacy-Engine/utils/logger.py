from loguru import logger

def setup_logger():
    logger.add(
        "./logs/prometheus_{time}.log",
        rotation="500 MB",
        level="INFO",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
    )
    return logger

log = setup_logger()