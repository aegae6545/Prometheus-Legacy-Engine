import os

class Config:
    # Mimo API 配置
    MIMO_API_KEY = os.getenv("MIMO_API_KEY", "sk-xxxxxxxxxxxxxxxx")
    MIMO_BASE_URL = "https://api.mimo.com/v1"
    
    # 模型选择
    REASONING_MODEL = "mimo-max-2026"  # 用于复杂推理
    VISION_MODEL = "mimo-vision-pro"   # 用于生成架构图
    CODING_MODEL = "mimo-coder-v2"     # 用于代码生成
    
    # 项目路径
    LEGACY_CODE_PATH = "./data/legacy_source"
    OUTPUT_PATH = "./data/refactored_code"
    LOG_PATH = "./logs/prometheus.log"
    
    # 阈值配置
    MAX_CONTEXT_WINDOW = 1048576  # 1M Tokens
    RECURSION_LIMIT = 50