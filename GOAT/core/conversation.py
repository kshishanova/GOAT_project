from typing import List, Optional
from models.reasoning import ConversationTurn
from core.attacker import AttackerLLM
from core.target import TargetLLM


class ConversationManager:
    """Цикл атаки """

    def __init__(self, attacker: AttackerLLM, target: TargetLLM, max_turns: int = 5):
        self.attacker = attacker
        self.target = target
        self.max_turns = max_turns
        self.turns: List[ConversationTurn] = []

    def run_conversation(self, goal: str) -> List[ConversationTurn]:
        self.turns = []

        # Генерация начальной атаки
        reasoning = self.attacker.generate_initial_attack()
        self.turns.append(ConversationTurn(
            attacker_prompt=reasoning.response,
            target_response="",
            reasoning=reasoning
        ))

        for i in range(self.max_turns):
            print(f"\n--- Turn {i+1} ---")

            target_response = self.target.generate_response(self.attacker.C_T)
            # target_response = self.target.generate_response(self.attacker.C_T[-1]["content"])
            # получает полную историю диалога
            self.attacker.C_T.append({"role": "assistant", "content": target_response})
            self.turns[-1].target_response = target_response

            if i == self.max_turns - 1:
                break
            # Генерация следующей атаки    
            reasoning = self.attacker.generate_next_attack(target_response)
            self.turns.append(ConversationTurn(
                attacker_prompt=reasoning.response,
                target_response="",
                reasoning=reasoning
            ))

        return self.turns
