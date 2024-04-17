import csv
import os
filename = "university_database/"
def finding_files_in_directory():
    for filename in os.listdir("university_database/"):
        print(filename) 
finding_files_in_directory()
filename += input("Виберіть файл з списку вище: ")
def find_names_by_grades(grade: int, filename=filename):
    names, grades = read()
    return names[grades.index(str(grade))]
def read(filename = filename):
    fd = open(filename, "r")

    reader = csv.reader(fd, delimiter="\t")
    names = []
    grades = []
    for row in reader:
        row = row[0].split(" ")
        names.append(row[0:2])
        grades.append(row[-1])
    return names, grades

def sorting(filename=filename):
    names, grades = read()
    grades_int = []
    names_and_surnames = []
    for name_and_surname in names:
        names_and_surnames.append(name_and_surname[0]+" "+name_and_surname[1])
    for grade in grades:
        grades_int.append(int(grade))
    dict_ = dict.fromkeys(names_and_surnames, grades_int)
    for i in range(len(names_and_surnames)):
        dict_[names_and_surnames[i]] = grades_int[i]
    sorte = sorted(dict_.items(), key=lambda x:x[1], reverse=True)
    converted_dict = dict(sorte)   
    print(converted_dict)

    first = list(converted_dict.keys())[0]
    for key, grades in zip(converted_dict.keys(), converted_dict.values()):
        if key == first:
            write(key, str(grades))
            continue
        else:
            write_after(key, str(grades))
    read()
def write(name, grade,filename=filename,):
    fd = open(filename, "w")
    fd.write(name + " " + grade)

def write_after(name, grade, filename=filename):
    with open(filename, 'a') as file:
        file.write('\n' + name + " " + grade)


while True:
    what_todo = int(input("Що робити(1 - прочитати, 2 - записати з початку, 3 - дозапис, 4 - пошук за балом, 5 - сортування за середнім балом), 6 - вийти:( "))

    if what_todo == 1:
        print(read())
    elif what_todo == 2:
        name = input("Ім'я студента")
        grade = input("Середнії бал студента")
        write(name, grade)
    elif what_todo == 3:
        name = input("Ім'я студента")
        grade = input("Середнії бал студента")
        write_after(name, grade)

    elif what_todo == 4:
        grade = input("Середнії бал шуканого студента")
        print(find_names_by_grades(int(grade)))


    elif what_todo == 5:
        sorting()
    elif what_todo == 6:
        break