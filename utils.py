from datetime import datetime


def show_tasks(tasks: list):
    """Выводит список задач"""
    if len(tasks) == 0:
        print("Задачи не найдены")
    else:
        for task in tasks:
            task = task.to_dict()
            print(f"ID: {task['id']}, "
                  f"Название: {task['title']}, "
                  f"описание: {task['description']}, "
                  f"категория: {task['category']}, "
                  f"cрок выполнения: {task['due_date']}, "
                  f"приоритет: {task['priority']}, "
                  f"статус: {task['status']}")


def is_valid_date(date: str) -> bool:
    """Проверяет, что дата в формате YYYY-MM-DD."""
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def is_valid_priority(priority: str) -> bool:
    """Проверяет, что приоритет введен правильно (Низкий, Средний, Высокий)."""
    valid_priorities = ["низкий", "средний", "высокий"]
    return priority.lower() in valid_priorities


def get_valid_date_input():
    """Запрашивает у пользователя дату в формате YYYY-MM-DD,
    пока не будет введена корректная дата.
    """
    due_date = input("Срок выполнения (YYYY-MM-DD): ")
    while not is_valid_date(due_date):
        print("Ошибка: дата должна быть в формате YYYY-MM-DD.")
        due_date = input("Срок выполнения (YYYY-MM-DD): ")
    return due_date


def get_valid_priority_input():
    """Запрашивает у пользователя приоритет задачи (Низкий/Средний/Высокий),
    пока не будет введен корректный приоритет."""
    priority = input("Приоритет (Низкий/Средний/Высокий): ")
    while not is_valid_priority(priority):
        print("Ошибка: приоритет должен быть 'Низкий', 'Средний' или 'Высокий'.")
        priority = input("Приоритет (Низкий/Средний/Высокий): ")
    return priority
