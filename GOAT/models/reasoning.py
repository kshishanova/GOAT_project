from pydantic import BaseModel
from typing import List, Optional

class ReasoningStep(BaseModel):
    observation: str  # Наблюдение за ответом модели
    thought: str      # Размышление для продвижении к цели  
    strategy: str     # Выбранная стратегия атаки
    response: str     # Финальный ответ для целевой модели

class ConversationTurn(BaseModel):
    attacker_prompt: str
    target_response: str 
    reasoning: Optional[ReasoningStep] = None

class ConversationResult(BaseModel):
    goal: str
    attack_used: str
    turns: List[ConversationTurn]
    success: bool = False
    final_response: Optional[str] = None