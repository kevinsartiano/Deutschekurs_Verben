import random
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen


class OpeningWindow(Screen):
    pass


class MainWindow(Screen):
    pass


class ResultWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class DeutscheVerben(App):
    tense_list = ['Präsens (er) ', 'Präteritum (ich) ', 'Perfekt (er) ']
    verb_list = {'Beginnen': ['beginnt', 'begann', 'hat begonnen']}

    def build(self):
        return Builder.load_file('deutscheverben.kv')

    def exercise(self):
        random_verb = random.choice(list(self.verb_list.keys()))
        answer_list = []
        mistake_counter = -1

        while answer_list != self.verb_list[random_verb]:
            answer_list = []
            print('\n{}'.format(random_verb.upper()))
            for tense in self.tense_list:
                answer = input('{}: '.format(tense))
                answer_list.append(answer)
            mistake_counter += 1

        print('FEHLER GEMACHT: {}'.format(mistake_counter))


if __name__ == '__main__':
    DeutscheVerben().run()
