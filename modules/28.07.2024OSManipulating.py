

import os
import shutil
ROOT = r".\Python"
DATA_ROOT = ROOT
# Печать значений ROOT и DATA_ROOT


def show_data_list():
    for item in os.listdir(DATA_ROOT):
        print(item)

show_data_list()

print('---------------------------------------2----')

print(ROOT)
print(DATA_ROOT)

print('----------------------------------------3---')


#Функция create_data_directories будет принимать список
#  имен каталогов и создавать их в DATA_ROOT, если они не 
# существуют:

# Задание 3: Функция для создания каталогов
def create_data_directories(dirs):
    for directory in dirs:
        dir_path = os.path.join(DATA_ROOT, directory)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print(f"The directory {directory} has been created.")
        else:
            print(f"The directory {directory} already exists.")

dirs = ["personal", "work"]
create_data_directories(dirs)



print('---------------------------------------4----')

#Функция classify принимает словарь и перемещает 
# файлы в соответствующие каталоги:
# Задание 4: Функция для перемещения файлов в соответствующие каталоги
def classify(categories):
    for directory, files in categories.items():
        dir_path = os.path.join(DATA_ROOT, directory)
        for file in files:
            file_path = os.path.join(DATA_ROOT, file)
            if os.path.exists(file_path):
                shutil.move(file_path, dir_path)
                print(f"Moved {file} to {directory}.")

categories = {
    "personal": ["todos.txt", "bookmarks.txt"],
    "work": ["customers.csv", "jobs.csv"]
}

classify(categories)



print('--------------------------------------5-----')
#Создадим отчет pending_jobs.csv с использованием данных 

import csv
def generate_pending_jobs_report():
    reports_dir = os.path.join(DATA_ROOT)
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    customers_file = os.path.join(DATA_ROOT, 'customers.csv')
    jobs_file = os.path.join(DATA_ROOT,'jobs.csv')
    pending_jobs_file = os.path.join(reports_dir, 'pending_jobs.csv')

    customers = {}
    with open(customers_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            customers[row['id']] = row['name']

    with open(jobs_file, 'r', encoding='utf-8') as file, open(pending_jobs_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(file)
        writer = csv.writer(outfile)
        writer.writerow(['id', 'description', 'client'])
        
        for row in reader:
            if row['status'] != 'done':
                client_name = customers.get(row['customer_id'], 'Unknown')
                writer.writerow([row['id'], row['description'], client_name])
