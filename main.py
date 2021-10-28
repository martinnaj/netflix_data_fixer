# This program will cleanup any Netflix exported data
# import csv
from inspect import getfullargspec
from os.path import exists


class Modes:
    __thanks_message__ = 'Thank you for using this "library". Made by Martin.'

    def __init__(self):
        self.data = [x for x in dir(self) if not x.startswith('__') and not x.endswith('__')]
    

    def my_list___remove_profile(self, file_name):
        file_lines = open(file_name, 'r').read().split('\n')

        first_line = file_lines.pop(0)

        data = {j: [] for j in first_line.split(',')}

        self.__finish__() if 'Profile Name' not in data.keys() else None

        profiles = list({j.split(',')[list(data.keys()).index('Profile Name')]: 0 for j in file_lines if
                         j.split(',')[list(data.keys()).index('Profile Name')]}.keys())

        another_profile = len(profiles) > 1
        while another_profile:
            print("Please select one of the following profiles to remove:")
            print(', '.join(profiles).title())

            chosen_profile = input()
            while not len([j for j in [p.lower() for p in profiles] if j.startswith(chosen_profile)]) == 1:
                print("Profile not found")
                chosen_profile = input().lower()

            chosen_profile = profiles[[p.lower() for p in profiles].index(
                [j for j in [p.lower() for p in profiles] if j.startswith(chosen_profile)][0])]

            profiles.pop(profiles.index(chosen_profile))

            file_lines = [j for j in file_lines if not j.split(',')[0] == chosen_profile]

            print("Would you like to remove another profile? (y/n)")

            file = open(file_name, 'w+')
            file.write(first_line + '\n' + '\n'.join(file_lines))
            file.close()

            another_profile = input().lower() == 'y' and len(profiles)

        self.__finish__()

    def my_list___remove_column(self, file_name):
        file_lines = open(file_name, 'r').read().split('\n')

        columns = file_lines.pop(0).split(',')

        another_column = len(columns) > 1
        while another_column:
            print("Please select one of the following columns to remove:")
            print(', '.join(columns).title())

            chosen_column = input()
            while not len([j for j in [p.lower() for p in columns] if j.startswith(chosen_column)]) == 1:
                print("Column not found")
                chosen_column = input().lower()

            chosen_column = columns[[p.lower() for p in columns].index(
                [j for j in [p.lower() for p in columns] if j.startswith(chosen_column)][0])]

            column_index = columns.index(chosen_column)

            columns.pop(columns.index(chosen_column))

            file_lines = [','.join([k for k in j.split(',') if not j.split(',').index(k) == column_index]) for j in
                          file_lines]

            print("Would you like to remove another column? (y/n)")

            file = open(file_name, 'w+')
            file.write(','.join(columns) + '\n' + '\n'.join(file_lines))
            file.close()

            another_column = input().lower() == 'y' and len(columns)

        self.__finish__()

    def my_list___only_one_profile(self, file_name):
        self.__finish__()

    def __finish__(self):
        print(self.__thanks_message__)
        exit()


modes = Modes()

chosen_data_store = 'my_list'
chosen_data_store = ''
while not [x for x in modes.data if x.startswith(chosen_data_store + '___')]:
    print("Choose a data type to edit from the following: ")
    print(', '.join(list(set([x.split('___')[0].replace('_', ' ').title() for x in modes.data]))))
    chosen_data_store = input().lower().replace(' ', '_')

chosen_operation = 'remove_column'
chosen_operation = ''
while not [x for x in modes.data if x == chosen_data_store + '___' + chosen_operation]:
    print("Choose an operation from the following: ")
    print(', '.join(list(set([x.split('___')[1].replace('_', ' ').title() for x in modes.data if
                              x.startswith(chosen_data_store + '___')]))))
    chosen_operation = input().lower().replace(' ', '_')

function = getattr(modes, chosen_data_store + '___' + chosen_operation)
argument_names = [x for x in getfullargspec(function).args if not x == 'self']
argument_values = []

for i in argument_names:
    print("What is the '" + i.replace('_', ' ') + '\'?')
    input_ = 'MyList.csv'
    input_ = input()
    if i == 'file_name':
        while not exists(input_):
            print("That file doesn't exist.")
            input_ = input()
    argument_values.append(input_)

function(*argument_values)
