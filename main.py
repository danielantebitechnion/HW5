# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json


def names_of_registered_students(input_json_path, course_name):
    output = []
    with open(input_json_path, 'r') as json_file:
        data = json.load(json_file)
    for v in data.values():
        if course_name in v['registered_courses']:
            output.append(v['student_name'])
    return output

def enrollment_numbers(input_json_path, output_file_path):
    courses_dict = {}
    with open(input_json_path, 'r') as json_file:
        data = json.load(json_file)
    for v in data.values():
        for courses in v['registered_courses']:
            if courses in courses_dict:
                courses_dict[courses] = courses_dict.get(courses)+1
            else:
                courses_dict[courses] = 1
    iterator = 1
    with open(output_file_path, 'w') as f:
        for key,value in sorted(courses_dict.items()):
            str = '"' + key + '"' + ' ' + "{}".format(value)
            f.write(str)
            if iterator < len(courses_dict):
                f.write('\n')
            iterator +=1

def main():
    enrollment_numbers('C:\\Users\\user\\Desktop\\test.json', 'C:\\Users\\user\\Desktop\\out.json')

if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
