# -*- coding: utf-8 -*-
from modules.DialogueManagement.manager import DialogueManager
from modules.DialogueManagement.state import DialogueState
from modules.LanguageGeneration.generator import LanguageGenerator
from modules.LanguageUnderstanding.language_understanding import LanguageUnderstanding
from modules.BackEnd.APIs.hotpepper import HotPepperGourmetAPI

if __name__ == '__main__':
    generator = LanguageGenerator()
    language_understanding = LanguageUnderstanding()
    state = DialogueState()
    manager = DialogueManager()
    api = HotPepperGourmetAPI()

    print('S: 料理のジャンルや場所をおっしゃってください。')
    while True:
        # Input from User
        sent = input('U: ')
        if sent == 'ありがとう':
            print('S: どういたしまして')
            break

        # Language Understanding
        dialogue_act = language_understanding.execute(sent)

        # Update Dialogue state
        manager.update_dialogue_state(dialogue_act, state)
        sys_act_type = manager.select_action(dialogue_act, state, api)

        # Generate Sentence
        sent = generator.generate_sentence(sys_act_type)
        print(sent)