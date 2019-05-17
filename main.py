import random


class DeutscheVerben:

    tense_list = ['Präsens (er) ', 'Präteritum (ich) ', 'Perfekt (er) ']
    verb_list = {'Beginnen': ['beginnt', 'begann', 'hat begonnen']}

    def __init__(self):
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
    DeutscheVerben()
