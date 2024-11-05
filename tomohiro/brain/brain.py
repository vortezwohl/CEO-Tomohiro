import logging

from ceo import Agent, get_openai_model

from tomohiro.ability import *

logging.getLogger('ceo').setLevel(logging.DEBUG)

abilities = [calculator, get_current_datetime, search_internet]


model = get_openai_model()

agent = Agent(abilities, model)

agent.assign('啥是ceo-py,现在几点了，一加三等于几')

print(agent.just_do_it())
