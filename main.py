# This program will cleanup any Netflix exported data
# import csv
from inspect import getfullargspec
from os.path import exists


class Modes:
    __thanks_message__ = 'Thank you for using this "library". Made by Martin.'

    def __init__(self):
        self.data = [x for x in dir(self) if not x.startswith('__') and not x.endswith('__')]

    def my_list___remove_profile(self, file_name):
        file = open(file_name, 'r')
        file_lines = file.readlines()

        print(file_lines)


        # active_profiles =

        self.finish()

    def my_list___only_one_profile(self, file_name):
        self.finish()

    def __finish__(self):
        print(self.__thanks_message__)


modes = Modes()

chosen_data_store = ''
while not [x for x in modes.data if x.startswith(chosen_data_store + '___')]:
    print("Choose a data type to edit from the following: ")
    print(', '.join(list(set([x.split('___')[0].replace('_', ' ').title() for x in modes.data]))))
    chosen_data_store = input().lower().replace(' ', '_')

chosen_operation = ''
while not [x for x in modes.data if x == chosen_data_store + '___' + chosen_operation]:
    print("Choose an operation from the following: ")
    print(', '.join(list(set([x.split('___')[1].replace('_', ' ').title() for x in modes.data if x.startswith(chosen_data_store + '___')]))))
    chosen_operation = input().lower().replace(' ', '_')

function = getattr(modes, chosen_data_store + '___' + chosen_operation)
argument_names = [x for x in getfullargspec(function).args if not x == 'self']
argument_values = []

for i in argument_names :
    print("What is the '" + i.replace('_', ' ') + '\'?')
    input_ = input()
    if i == 'file_name':
        while not exists(input_):
            print("That file doesn't exist.")
            input_ = input()
    argument_values.append(input_)

print(argument_values)