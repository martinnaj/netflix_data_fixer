# This program will cleanup any Netflix exported data
from inspect import getfullargspec
from os.path import exists
from re import split


class Modes:
    __thanks_message__ = 'Thank you for using this "library". Made by Martin.'

    def __init__(self):
        self.data = [x for x in dir(self) if not x.startswith('__') and not x.endswith('__')]

    def __remove_column__(self, file_name):
        file_lines = open(file_name, 'r', encoding="utf-8").read().split('\n')

        columns = split(r',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)', file_lines.pop(0))

        another_column = len(columns) > 1
        while another_column:
            print("Please select one of the following columns to remove:")
            print(', '.join(columns).title())

            chosen_column = input().lower()
            while not len([j for j in [p.lower() for p in columns] if j.startswith(chosen_column)]) == 1:
                print("Column not found or matches multiple")
                chosen_column = input().lower()

            chosen_column = columns[[p.lower() for p in columns].index(
                [j for j in [p.lower() for p in columns] if j.startswith(chosen_column)][0])]

            column_index = columns.index(chosen_column)

            columns.pop(column_index)

            file_lines = [','.join([split(r',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)', j)[k] for k in
                                    range(len(split(r',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)', j))) if
                                    not k == column_index]) for j in file_lines]

            print("Would you like to remove another column? (y/n)")

            file = open(file_name, 'w+', encoding="utf-8")
            file.write(','.join(columns) + '\n' + '\n'.join(file_lines))
            file.close()

            another_column = input().lower() == 'y' and len(columns)

    def __only_one_profile__(self, file_name, profile_column_name):
        file_lines = open(file_name, 'r', encoding="utf-8").read().split('\n')

        first_line = file_lines.pop(0)

        data = {j: [] for j in split(r',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)', first_line)}

        self.__finish__() if profile_column_name not in data.keys() else None

        profiles = list(
            {split(r',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)', j)[list(data.keys()).index(profile_column_name)]: 0 for j in
             file_lines if
             split(r',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)', j)[list(data.keys()).index(profile_column_name)]}.keys())

        print("Please select one of the following profiles to keep:")
        print(', '.join(profiles).title())

        chosen_profile = input().lower()
        while not len([j for j in [p.lower() for p in profiles] if j.startswith(chosen_profile)]) == 1:
            print("Profile not found or matches multiple")
            chosen_profile = input().lower()

        chosen_profile = profiles[[p.lower() for p in profiles].index(
            [j for j in [p.lower() for p in profiles] if j.startswith(chosen_profile)][0])]

        file_lines = [j for j in file_lines if
                      split(r',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)', j)[
                          list(data.keys()).index(profile_column_name)] == chosen_profile]

        file = open(file_name, 'w+', encoding="utf-8")
        file.write(first_line + '\n' + '\n'.join(file_lines))
        file.close()

    def __remove_profile__(self, file_name, profile_column_name):
        file_lines = open(file_name, 'r', encoding="utf-8").read().split('\n')

        first_line = file_lines.pop(0)

        data = {j: [] for j in split(r',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)', first_line)}

        self.__finish__() if profile_column_name not in data.keys() else None

        profiles = list(
            {split(r',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)', j)[list(data.keys()).index(profile_column_name)]: 0 for j in
             file_lines if
             split(r',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)', j)[list(data.keys()).index(profile_column_name)]}.keys())

        another_profile = len(profiles) > 1
        while another_profile:
            print("Please select one of the following profiles to remove:")
            print(', '.join(profiles).title())

            chosen_profile = input().lower()
            while not len([j for j in [p.lower() for p in profiles] if j.startswith(chosen_profile)]) == 1:
                print("Profile not found or matches multiple")
                chosen_profile = input().lower()

            chosen_profile = profiles[[p.lower() for p in profiles].index(
                [j for j in [p.lower() for p in profiles] if j.startswith(chosen_profile)][0])]

            profiles.pop(profiles.index(chosen_profile))

            file_lines = [j for j in file_lines if not split(r',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)', j)[
                                                           list(data.keys()).index(
                                                               profile_column_name)] == chosen_profile]

            print("Would you like to remove another profile? (y/n)")

            file = open(file_name, 'w+', encoding="utf-8")
            file.write(first_line + '\n' + '\n'.join(file_lines))
            file.close()

            another_profile = input().lower() == 'y' and len(profiles)

    def __remove_by_value__(self, file_name, col_name, value='', remove_all=False):
        file_lines = open(file_name, 'r', encoding="utf-8").read().split('\n')

        first_line = file_lines.pop(0)

        data = {j: [] for j in split(r',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)', first_line)}

        self.__finish__() if col_name not in data.keys() else None

        column_values = list(
            {split(r',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)', j)[list(data.keys()).index(col_name)]: 0 for j in file_lines if
             split(r',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)', j)[list(data.keys()).index(col_name)]}.keys())

        another_value = len(column_values) > 1
        while another_value:
            print("Please select one of the following values to remove:") if not value and not remove_all else None
            print(', '.join(column_values).title()) if not value and not remove_all else None

            chosen_value = input().lower() if not value and not remove_all else value
            while not remove_all and not len(
                    [j for j in [p.lower() for p in column_values] if j.startswith(chosen_value)]) == 1:
                print("Value not found or matches multiple")
                chosen_value = input().lower()

            chosen_value = column_values[[p.lower() for p in column_values].index(
                [j for j in [p.lower() for p in column_values] if j.startswith(chosen_value)][
                    0])] if not remove_all else column_values[0]

            column_values.pop(column_values.index(chosen_value))

            file_lines = [j for j in file_lines if not split(r',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)', j)[
                                                           list(data.keys()).index(col_name)] == chosen_value or (
                                      not split(r',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)', j)[
                                          list(data.keys()).index(col_name)] and remove_all)]

            print("Would you like to remove another value? (y/n)") if not value and not remove_all else None

            file = open(file_name, 'w+', encoding="utf-8")
            file.write(first_line + '\n' + '\n'.join(file_lines))
            file.close()

            another_value = len(column_values) and (remove_all or (input().lower() == 'y' and not value))

    def viewing_activity___remove_trailers_and_hooks(self, file_name):
        self.__remove_by_value__(file_name, 'Supplemental Video Type', '', True)
        self.__finish__()

    def viewing_activity___remove_not_latest_bookmark(self, file_name):
        self.__remove_by_value__(file_name, 'Latest Bookmark', 'not latest view')
        self.__finish__()

    def viewing_activity___remove_device(self, file_name):
        self.__remove_by_value__(file_name, 'Device Type')
        self.__finish__()

    def viewing_activity___remove_profile(self, file_name):
        self.__remove_profile__(file_name, 'Profile Name')
        self.__finish__()

    def viewing_activity___only_one_profile(self, file_name):
        self.__only_one_profile__(file_name, 'Profile Name')
        self.__finish__()

    def viewing_activity___remove_column(self, file_name):
        self.__remove_column__(file_name)
        self.__finish__()

    def search_history___remove_profile(self, file_name):
        self.__remove_profile__(file_name, 'Profile Name')
        self.__finish__()

    def search_history___only_one_profile(self, file_name):
        self.__only_one_profile__(file_name, 'Profile Name')
        self.__finish__()

    def search_history___remove_column(self, file_name):
        self.__remove_column__(file_name)
        self.__finish__()

    def my_list___remove_profile(self, file_name):
        self.__remove_profile__(file_name, 'Profile Name')
        self.__finish__()

    def my_list___only_one_profile(self, file_name):
        self.__only_one_profile__(file_name, 'Profile Name')
        self.__finish__()

    def my_list___remove_column(self, file_name):
        self.__remove_column__(file_name)
        self.__finish__()

    def __finish__(self):
        print(self.__thanks_message__)
        exit()


modes = Modes()

chosen_data_store = 'viewing_activity'
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
    input_ = 'ViewingActivity.csv'
    input_ = input()
    if i == 'file_name':
        while not exists(input_):
            print("That file doesn't exist.")
            input_ = input()
    argument_values.append(input_)

function(*argument_values)
