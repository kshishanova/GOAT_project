from typing import List, Dict

class TargetLLM:
    """
    Целевая LLM, которую мы пытаемся взломать.
    """ 

    def __init__(self, model_provider):
        self.model = model_provider

    def generate_response(self, conversation_history: List[Dict[str, str]]) -> str:
        """
        Генерирует ответ на промпт атакующего  """
        
        # Добавляем промпт атакующего в историю
        #self.C_T.append({"role": "user", "content": attacker_prompt})

        # Генерируем ответ через модель
        response = self.model.generate(conversation_history)

        # Добавляем ответ модели в историю
        #self.C_T.append({"role": "assistant", "content": response})

        return response
    
    """def clear(self):
        pass"""
    
 

    