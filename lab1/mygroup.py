# Список студентов: каждый студент — это словарь с полями:
# name (имя), surname (фамилия), exams (список экзаменов), marks (список оценок)
groupmates = [
    {
        "name": "Алексей",
        "surname": "Иванов",
        "exams": ["Математика", "Информатика", "Физика"],
        "marks": [5, 4, 5],
    },
    {
        "name": "Мария",
        "surname": "Петрова",
        "exams": ["История", "Экономика", "Право"],
        "marks": [3, 4, 4],
    },
    {
        "name": "Кирилл",
        "surname": "Сидоров",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5],
    },
    {
        "name": "Ирина",
        "surname": "Смирнова",
        "exams": ["Английский язык", "Математика", "Информатика"],
        "marks": [4, 4, 5],
    },
    {
        "name": "Дмитрий",
        "surname": "Кузнецов",
        "exams": ["Физика", "Химия", "Высшая математика"],
        "marks": [3, 3, 4],
    },
]


def print_students(students):
    """Печатает таблицу со студентами, переданными в список students."""
    # .ljust(N) — выравнивание строк по левому краю до длины N
    print("Имя".ljust(15), "Фамилия".ljust(12), "Экзамены".ljust(40), "Оценки".ljust(20))
    print("-" * 15, "-" * 12, "-" * 40, "-" * 20)
    for student in students:
        # str(...) нужен, чтобы список экзаменов/оценок превратить в строку
        print(
            student["name"].ljust(15),
            student["surname"].ljust(12),
            str(student["exams"]).ljust(40),
            str(student["marks"]).ljust(20),
        )


def filter_by_average(students, min_average):
    """Возвращает список студентов, у которых средний балл >= min_average."""
    result = []
    for student in students:
        marks = student["marks"]
        # Средний балл = сумма оценок / количество оценок
        average = sum(marks) / len(marks)
        if average >= min_average:
            result.append(student)
    return result


if __name__ == "__main__":
    # Основная точка входа в программу.
    # Сначала выводим всех студентов.
    print("Все студенты:")
    print_students(groupmates)

    # Просим пользователя ввести минимальный средний балл для фильтрации.
    # input всегда возвращает строку, поэтому приводим к float.
    print()  # пустая строка для визуального отступа
    user_input = input("Введите минимальный средний балл для фильтрации: ")

    try:
        min_avg = float(user_input)
    except ValueError:
        print("Ошибка: нужно ввести число. Программа завершена.")
        # exit(1) — завершение программы с кодом ошибки 1
        # но можно просто сделать return из main или ничего не делать.
    else:
        print(f"Студенты со средним баллом >= {min_avg}:")
        filtered = filter_by_average(groupmates, min_avg)
        if filtered:
            print_students(filtered)
        else:
            print("Нет студентов с таким средним баллом или выше.")
