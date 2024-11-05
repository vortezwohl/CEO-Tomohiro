from ceo import Agent
from langchain_core.language_models import BaseChatModel

from tomohiro.ability import *

class Tomohiro(Agent):
    def __init__(self, brain: BaseChatModel):
        abilities = [calculator, get_current_datetime, search_internet]
        super().__init__(abilities=abilities, brain=brain)
