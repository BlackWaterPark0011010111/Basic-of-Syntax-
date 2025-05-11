"""
Task: Write a function school_grades that accepts student names via *args and their subject grades via **kwargs in the format subject=grade, 
and returns a dictionary in the format {'name': {'subject': grade}}. If a student has no grades, indicate 'no grades'. Handle cases where 
the argument is not a string (name) or the grade is not a number between 1 and 5. Example call: school_grades('Vasya', 'Petya', math=4, physics=5, 
Petya_chemistry=3) should return {'Vasya': {'math': 4, 'physics': 5}, 'Petya': {'chemistry': 3}}.
Задача: напишите функцию school_grades, которая принимает через *args имена учеников, а через **kwargs их оценки по предметам в формате 
предмет=оценка, и возвращает словарь вида {'имя': {'предмет': оценка}}. Если у ученика нет оценок, укажите 'нет оценок'. Обработайте случай,
когда переданный аргумент не является строкой (имя) или оценка не число от 1 до 5. Пример вызова: school_grades('Вася', 'Петя', математика=4, 
физика=5, Петя_химия=3) 
должно вернуть {'Вася': {'математика': 4, 'физика': 5}, 'Петя': {'химия': 3}}.

"""
def school_grades(*args, **kwargs):
    grades_dict = {}
    for name in args:
        if not isinstance(name, str):
            print(f"Error: '{name}' - invalid name")
            continue
        grades_dict[name] = {}
    for subject_grade, grade in kwargs.items():
        subject_parts = subject_grade.split('_')
        if len(subject_parts) > 1:
            name = subject_parts[0]
            subject = '_'.join(subject_parts[1:])
        else:
            name = None
            subject = subject_grade
        if not isinstance(grade, int) or grade < 1 or grade > 5:
            print(f"Error: grade '{grade}' for '{subject_grade}' is invalid")
            continue
        if name and name in grades_dict:
            grades_dict[name][subject] = grade
        elif not name:
            for name in grades_dict:
                grades_dict[name][subject] = grade
    for name in grades_dict:
        if not grades_dict[name]:
            grades_dict[name] = 'no grades'
    return grades_dict
print(school_grades('Vasya', 'Petya', math=4, physics=5, Petya_chemistry=3))