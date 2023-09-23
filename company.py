"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.

Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела

Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.

Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.

13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]

# Ваши задачи такие:

print("\n1. Вывести названия всех отделов")
print(*[department['title'] for department in departments], sep=', ')

print("\n2. Вывести имена всех сотрудников компании")
name_list = []
for i, employers in enumerate([department['employers'] for department in departments]):
    name_list.extend([employer['first_name'] for employer in employers])
print(*name_list, sep=', ')
"""
# Вариант 2 для варианта 2
name_list = []
for department in departments:
    for employer in department['employers']:
        name_list.append(employer['first_name'])
        #print(name_list)
print(*name_list, sep=', ')
"""

print("\n3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают")
for department in departments:
    for employer in department['employers']:
        print(f"Department: {department['title']}; Employee: {employer['first_name']}")

print("\n4. Вывести имена всех сотрудников компании, которые получают больше 100к")
for department in departments:
    for employer in department['employers']:
        if employer['salary_rub'] > 100000:
            print(f"Employee {employer['first_name']} earns more than 100,000")

print("\n5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями)")
for department in departments:
    for employer in department['employers']:
        if employer['salary_rub'] < 100000:
            print(f"In department {department['title']}, employees earn less than 80,000")
            
print("\n6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела")
for department in departments:
    department_salary = 0
    for employer in department['employers']:
        department_salary += employer['salary_rub']
    print(f"In department {department['title']}, employees earn a total of {department_salary}")

# Второй уровень:
print("\n7. Вывести названия отделов с указанием минимальной зарплаты в нём")
for department in departments:
    department_salary = []
    for employer in department['employers']:
        department_salary.append(employer['salary_rub'])
    print(f"The minimum salary in department {department['title']} is {min(department_salary)}")

print("\n8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём")
for department in departments:
    department_salary = []
    for employer in department['employers']:
        department_salary.append(employer['salary_rub'])
    print(f"The minimum salary in department {department['title']} is {min(department_salary)}, average salary is {int(sum(department_salary) / len(department_salary))} and maximum is {max(department_salary)}")

print("\n9. Вывести среднюю зарплату по всей компании")
for department in departments:
    for employer in department['employers']:
        department_salary.append(employer['salary_rub'])
print(f"The average salary in company {int(sum(department_salary) / len(department_salary))}")

print("\n10. Вывести названия должностей, которые получают больше 90к без повторений")
positions = set()
for department in departments:
    for employer in department['employers']:
        if employer['salary_rub'] > 90000:
            positions.add(employer['position'])
print(f"{', '.join(positions)} earns more than 90,000")
        
print("\n11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин)")
female_salary = []
for department in departments:
    for employer in department['employers']:
        if employer["first_name"] in ['Michelle', 'Nicole', 'Christina', 'Caitlin']:
            female_salary.append(employer['salary_rub'])
    print(f"In the {department['title']} department the average salary for girls is {sum(female_salary)/ len(female_salary)}")

print("\n12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву")
last_names = set()
for department in departments:
    for employer in department['employers']:
        print(employer["last_name"][-1])
        if employer["last_name"][-1] in 'aeijoquy':
            last_names.add(employer['first_name'])
print(f"{', '.join(last_names)}")

print("\n13. Вывести список отделов со средним налогом на сотрудников этого отдела")

# 14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
# 15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
# 16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
# 17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.