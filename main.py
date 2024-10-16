# Ініціалізація словника з даними про студентів
# Ключ словника - повне ім'я студента
# Значення - вкладений словник з інформацією про студента
students_group = {
    "Тихонов Богдан Валерійович": {
        'group_number': 'КН-37-4',  # Назва групи студента
        'course': 2,  # Курс навчання
        'subjects_grades': {  # Словник предметів та оцінок
            'ММДО': 85,
            'Чисельні Методи': 95,
            'Алгоритмізація': 95
        }
    },
    "Срібна Ольга Юріївна": {
        'group_number': 'КН-37-4',
        'course': 2,
        'subjects_grades': {
            'ММДО': 70,
            'Чисельні Методи': 95,
            'Алгоритмізація': 85
        }
    },
    "Лободюк Євгеній Сергійович": {
        'group_number': 'КН-37-4',
        'course': 2,
        'subjects_grades': {
            'ММДО': 95,
            'Чисельні Методи': 95,
            'Алгоритмізація': 95
        }
    },
    "Ткаченко Ілля Олександрович": {
        'group_number': 'КН-37-4',
        'course': 2,
        'subjects_grades': {
            'ММДО': 95,
            'Чисельні Методи': 95,
            'Алгоритмізація': 85
        }
    },
    "Росієнко Олексій Олександрович": {
        'group_number': 'КН-37-4',
        'course': 2,
        'subjects_grades': {
            'ММДО': 70,
            'Чисельні Методи': 85,
            'Алгоритмізація': 85
        }
    }
}


def add_student(students_dict):
    """
    Тихонов Богдан
    Функція для додавання нового студента в словник.
    Вона взаємодіє з користувачем через введення з клавіатури.

    Аргументи:
    students_dict -- словник студентів, до якого буде додано новий запис
    """
    try:
        # Введення повного імені студента
        full_name = input("Введіть повне ім'я студента (Прізвище Ім'я По батькові): ")

        # Перевірка наявності студента в словнику
        if full_name in students_dict:
            print(f"Студент {full_name} вже існує.")
            return

        # Введення назви групи
        group_number = input(f"Введіть назву групи для студента {full_name}: ")

        # Введення курсу та перевірка на числове значення
        course = input(f"Введіть курс для студента {full_name}: ")
        if not course.isdigit():
            print("Помилка: курс має бути числом.")
            return
        course = int(course)

        # Ініціалізація порожнього словника для предметів та оцінок
        subjects_grades = {}

        # Введення предметів та оцінок
        while True:
            # Введення назви предмета
            subject = input("Введіть назву предмета (або натисніть Enter для завершення): ")
            if subject == "":
                break  # Вихід з циклу, якщо користувач натиснув Enter без введення

            # Введення оцінки за предмет та перевірка на числове значення
            grade = input(f"Введіть оцінку за предмет {subject}: ")
            if not grade.isdigit():
                print("Помилка: оцінка має бути числом.")
                continue  # Повернення на початок циклу для повторного введення оцінки

            # Додавання предмета та оцінки до словника subjects_grades
            subjects_grades[subject] = int(grade)

        # Додавання нового студента до основного словника students_dict
        students_dict[full_name] = {
            'group_number': group_number,
            'course': course,
            'subjects_grades': subjects_grades
        }
        print(f"Студента {full_name} додано.")

    except ValueError as e:
        # Обробка винятків, якщо виникають помилки при введенні даних
        print(f"Помилка: {e}")


def display_students(students_dict):
    """
    Тихонов Богдан
    Функція для виведення на екран всіх студентів та їх даних.


    Аргументи:
    students_dict -- словник студентів, інформацію про яких потрібно вивести
    """
    if not students_dict:
        print("Словник порожній.")
    else:
        # Прохід по всіх записах словника students_dict
        for student, details in students_dict.items():
            print(f"\nСтудент: {student}")
            print(f"Група: {details['group_number']}, Курс: {details['course']}")
            print("Оцінки:")
            # Виведення всіх предметів та оцінок студента
            for subject, grade in details['subjects_grades'].items():
                print(f"  {subject}: {grade}")


def calculate_average_grade(students_dict):
    """
    Лободюк Євгеній
    Функція для обчислення та виведення середньої оцінки кожного студента.

    Аргументи:
    students_dict -- словник студентів, для яких потрібно обчислити середню оцінку
    """
    if not students_dict:
        print("Словник порожній.")
    else:
        for student, details in students_dict.items():
            grades = details['subjects_grades'].values()
            if grades:
                average_grade = sum(grades) / len(grades)
                print(f"Студент: {student}, Середня оцінка: {average_grade:.2f}")
            else:
                print(f"У студента {student} немає оцінок.")


def students_below_threshold(students_dict):
    """
    Ткаченко Ілля
    Функція для виведення студентів, які мають оцінку нижче заданого порогу за певний предмет.

    Аргументи:
    students_dict -- словник студентів, яких потрібно перевірити
    """
    if not students_dict:
        print("Словник порожній.")
    else:
        # Введення назви предмета
        subject = input("Введіть назву предмета: ")

        # Введення порогової оцінки
        try:
            threshold = int(input("Введіть порогову оцінку: "))
        except ValueError:
            print("Помилка: оцінка повинна бути числом.")
            return

        # Перевірка студентів
        students_below = []
        for student, details in students_dict.items():
            # Перевіряємо, чи є предмет у словнику предметів студента
            if subject in details['subjects_grades']:
                grade = details['subjects_grades'][subject]
                if grade < threshold:
                    students_below.append((student, grade))

        # Виведення студентів з оцінками нижче порога
        if students_below:
            print(f"\nСтуденти, які мають оцінку нижче {threshold} з предмету {subject}:")
            for student, grade in students_below:
                print(f"{student}: {grade}")
        else:
            print(f"Немає студентів з оцінкою нижче {threshold} за предмет {subject}.")


def exit_program():
    """
    Функція для завершення роботи програми.
    """
    print("Вихід з програми.")
    exit()


def main():
    """
    Головна функція програми, що надає меню для взаємодії з користувачем.
    Тут можна додавати нові пункти меню та відповідні функції.
    """
    # Словник, що відповідає за вибір користувача та виклик відповідних функцій
    menu_actions = {
        "1": display_students,  # Виведення всіх студентів
        "2": add_student,  # Додавання нового студента
        "3": calculate_average_grade,  # Обчислення середньої оцінки кожного студента
        "4": students_below_threshold,  # функція для виведення студентів, які мають оцінку за певним предметом нижче заданого порогу
        # Додати новий пункт меню можна тут, призначивши йому індекс та ф-цію
        "5": exit_program  # Вихід з програми
    }

    while True:
        # Виведення меню на екран
        print("\n--- Меню ---")
        print("1. Вивести всіх студентів та їх дані")
        print("2. Додати нового студента")
        print("3. Обчислити середню оцінку кожного студента")
        print("4. Функція для виведення студентів, які мають оцінку за певним предметом нижче заданого порогу")
        print("5. Вийти")

        # Запит вибору дії у користувача
        choice = input("Оберіть дію (1-5): ")


        # Отримання функції з словника menu_actions за ключем choice
        action = menu_actions.get(choice)
        if action:
            # Виклик відповідної функції та передача словника студентів як аргументу
            action(students_group)
            # Пауза перед поверненням до меню
            input("\nНатисніть Enter, щоб повернутися до меню.")
        else:
            # Повідомлення про невірний вибір
            print("Невірний вибір, спробуйте ще раз.")


# Запуск програми
main()
