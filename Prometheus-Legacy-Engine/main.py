import asyncio
from agents.archaeologist import ArchaeologistAgent
from agents.architect import ArchitectAgent
from agents.validator import ValidatorAgent
from utils.logger import log

async def main():
    log.info("🚀 启动 Prometheus 遗留系统重构引擎 v2.6...")
    
    # 初始化智能体
    archaeologist = ArchaeologistAgent()
    architect = ArchitectAgent()
    validator = ValidatorAgent()
    
    # 模拟遗留代码输入 (高 Token 消耗场景)
    legacy_code = "..." * 50000  # 模拟大量代码
    
    # 1. 分析阶段
    analysis = await archaeologist.think(legacy_code)
    doc_id = await archaeologist.act(analysis)
    
    # 2. 设计阶段
    design = await architect.think(doc_id)
    plan_id = await architect.act(design)
    
    # 3. 验证阶段 (高并发/多模态)
    test_cases = await validator.think(plan_id)
    result = await validator.act(test_cases)
    
    log.info("🎉 整个重构工作流执行完毕。")

if __name__ == "__main__":
    asyncio.run(main())