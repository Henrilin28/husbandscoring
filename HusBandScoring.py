from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError


style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})


class HusBandScoring():
    
    def __init__(self, 
                 name, 
                 height, 
                 weight, 
                 talents, 
                 habits,
                 attitude
                 ):
        self.name = name
        self.height = height
        self.weight = weight
        self.talents = talents
        self.habits = habits
        self.attitude = attitude
        self.score = 0


    def basic_score(self, looks=True):

        if looks==True:
            self.score += 100
        if self.weight < 120:
            self.score += round((self.weight - 120)/10.0)*100
        if self.weight >= 150:
            self.score += round((150 - self.weight)/10.0)*100
        self.score += (self.height - 175)*100
        print(f"{self.score}")

    def talent_score(self):
        """This function will calculate talent score based on a dictionary
        """
        self.score += sum(self.talents.values())* 100 

    def habit_attitude_score(self):
        base_habit = len(self.habits.keys()) * -100.0
        base_attitude = len(self.attitude.keys())  * -100.0
        
        self.score += base_habit + base_attitude + (sum(self.habits.values()) * 200) + (sum(self.attitude.values()) * 200)

    def cheated(self):
        self.score = 0

    def print_summary(self):

        summary = f"""{self.name} has totlal score {self.score}

        
                   """
        print (summary)

class NumberValidator(Validator):
    def validate(self, document):
        try:
            float(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))  # Move cursor to end



print('Hi, welcome to 2020 Husband scoring system')

talents = ['sing', 'dance', 'draw painting', 'play instruments', 'do housework', 'cook']

talent_questions = [     {
        'type': 'confirm',
        'name': f'talent_{t}',
        'message': f'Can he {t}?',
        'default': True
    } for t in talents ]

habits = ['smoke', 'work out regularly', 'rather hanging out with kids then playing video games', 'make sure he looks neat everyday']

habits_questions = [     {
        'type': 'confirm',
        'name': f'habits_{h}',
        'message': f'Does he {h}?',
        'default': True
    } for h in habits ]

attitude = ['rarely fight with you', 'rarely judge on your apperance', 
            'rarely ignore you after a fight',
            'rarely admit his fault when you have a fight',
            'rarely think it is your fault when you have a fight', 
            'enjoy spending time with you without any excuse',
            'can always make you laugh',
            'always being responsible to you and the family',
            'is a romantic person',
            'has only one muse which is you <:3',
            'said his money is yours'
            ]

attitude_questions = [     {
        'type': 'confirm',
        'name': f'hattitude_{h}',
        'message': f'He {j}?',
        'default': True
    } for h, j in enumerate(attitude) ]

basic_questions = [
    {
        'type': 'input',
        'name': 'husband_name',
        'message': 'What\'s his name?',
        'default': 'Henry'
    },
    {
        'type': 'input',
        'name': 'height',
        'message': 'What\'s his height? (cm)',
        'validate': NumberValidator,
        'filter': lambda val: round(float(val))
    },
    {
        'type': 'input',
        'name': 'weight',
        'message': 'What\'s his weight (half a kilo)?',
        'validate': NumberValidator,
        'filter': lambda val: round(float(val))
    },
    {
        'type': 'confirm',
        'name': 'cheated',
        'message': 'Has he cheated you before?',
        'default': False
    }
]

final_questions = basic_questions + talent_questions + habits_questions + attitude_questions

answers = prompt(final_questions, style=style)
print('Order receipt:')
pprint(answers)
