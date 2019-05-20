import random
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty


class Exercise:
    random_verb = ""
    answer_list = []
    tense_list = ['Präsens (er) ', 'Präteritum (ich) ', 'Perfekt (er) ']
    verb_list = {'Beginnen': ['beginnt', 'begann', 'hat begonnen'], 'Haben': ['hat', 'hatte', 'hat gehabt']}

    def __init__(self):
        self.random_verb = self.get_random_verb()

    def get_random_verb(self):
        return random.choice(list(self.verb_list.keys()))


exercise = Exercise()


class OpeningWindow(Screen):
    pass


class MainWindow(Screen):

    current_verb = exercise.random_verb.upper()

    def add_answers(self):
        self.answer_list.append(self.answer1.text)
        self.answer_list.append(self.answer2.text)
        self.answer_list.append(self.answer3.text)
    pass


class ResultWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class DeutscheVerben(App):

    def build(self):
        return screen_manager

    # def exercise(self):
    #     random_verb = random.choice(list(self.verb_list.keys()))
    #     answer_list = []
    #     mistake_counter = -1
    #
    # def random_verb(self):
    #     return random.choice(list(self.verb_list.keys()))
    #
    # def add_answer(self, answer):
    #     answer_list = []
    #     answer_list.append(answer)
    #
    #     while answer_list != self.verb_list[random_verb]:
    #         answer_list = []
    #         print('\n{}'.format(random_verb.upper()))
    #         for tense in self.tense_list:
    #             answer = input('{}: '.format(tense))
    #             answer_list.append(answer)
    #         mistake_counter += 1
    #
    #     print('FEHLER GEMACHT: {}'.format(mistake_counter))


kv_source = Builder.load_file('deutscheverben.kv')

screen_manager = WindowManager()

screens = [OpeningWindow(name="opening"), MainWindow(name="main"), ResultWindow(name="result")]
for screen in screens:
    screen_manager.add_widget(screen)

exercise = Exercise()

if __name__ == '__main__':
    DeutscheVerben().run()
