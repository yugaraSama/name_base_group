import csv
import random
import json

final_list = {}
secu_dictionary = {}
dev_app_dictionary = {}

tutors_devapp = []
tutors_secu=[]

tutored_list_devapp = []
tutored_list_secu = []

seen = []

#Read the CSV file
with open('resources/tutorat_2024_2025.csv') as file:
    reader = csv.reader(file, delimiter=";")
    
    for row in reader:
        
        if "dev app" in row[0] or "ai" in row[0]:
            if "bloc 1" in row[4] and row[5] == "oui":
                tutored_list_devapp.append(row[3])
            elif "bloc 2 | bloc 3" in row[4] and row[6] == "oui":
                tutors_devapp.append(row[3])
                
        elif "cyber sécurité" in row[0]:
            if "bloc 1" in row[4] and row[5] == "oui":
                tutored_list_secu.append(row[3])
            elif "bloc 2 | bloc 3" in row[4] and row[6] == "oui":
                tutors_secu.append(row[3])

# Calculate the students per tutor for dev app
sbt_devapp = len(tutored_list_devapp) // len(tutors_devapp)
extra_students_devapp = len(tutored_list_devapp) % len(tutors_devapp)

# Calculate the students per tutor for secu
sbt_secu = len(tutored_list_secu) // len(tutors_secu)
extra_students_secu = len(tutored_list_secu) % len(tutors_secu)

print('---')

print(f'Total amount of students to tutor : {len(tutored_list_devapp) + len(tutored_list_secu)}')
print(f'Total amount of tutors : {len(tutors_devapp) + len(tutors_secu)}')

print('---')

print(f'Dev App - Number of tutored students per tutor: {sbt_devapp}')
print(f'Dev App - Number of extra students to distribute: {extra_students_devapp}')

print('---')

print(f'Secu - Number of tutored students per tutor: {sbt_secu}')
print(f'Secu - Number of extra students to distribute: {extra_students_secu}')

print('---')

# Initialize the dictionaries with tutor keys
for tutor in tutors_devapp:
    dev_app_dictionary[tutor] = []
    
for tutor in tutors_secu:
    secu_dictionary[tutor] = []

# Function to evenly distribute students
def distribute_students(tutored_list, tutors, tutor_dict, sbt):
    # First assign the minimum required students to each tutor
    for tutor in tutors:
        for _ in range(sbt):
            if tutored_list:
                student = random.choice(tutored_list)
                tutor_dict[tutor].append(student)
                tutored_list.remove(student)
    
    # Distribute any remaining students
    while tutored_list:
        for tutor in tutors:
            if tutored_list:
                student = random.choice(tutored_list)
                tutor_dict[tutor].append(student)
                tutored_list.remove(student)

# Distribute dev app students
distribute_students(tutored_list_devapp, tutors_devapp, dev_app_dictionary, sbt_devapp)

# Distribute secu students
distribute_students(tutored_list_secu, tutors_secu, secu_dictionary, sbt_secu)

# Combine both dictionaries into final_list
final_list['dev_app'] = dev_app_dictionary
final_list['secu'] = secu_dictionary

with open('resources/tutorat_2425.json', 'w', encoding='utf-8') as json_file:
    json.dump(final_list, json_file, ensure_ascii=False, indent=4)

#print(f'Tutor tab: {final_list}')