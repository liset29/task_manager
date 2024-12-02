from models.task_manager import TaskManager
from utils import show_tasks, get_valid_date_input, get_valid_priority_input


def main():
    manager = TaskManager("tasks.json")

    while True:
        print("\n1. Просмотреть задачи")
        print("2. Просмотреть задачи по категории")
        print("3. Добавить задачу")
        print("4. Изменить задачу")
        print("5. Удалить задачу")
        print("6. Отметить задачу выполненной")
        print("7. Поиск задач")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            tasks = manager.list_tasks()
            show_tasks(tasks)

        elif choice == "2":
            category = input("Введите категорию для просмотра: ")
            tasks_by_category = [task for task in manager.tasks if task.category.lower() == category.lower()]
            if tasks_by_category:
                show_tasks(tasks_by_category)
            else:
                print(f"Задачи в категории '{category}' не найдены.")

        elif choice == "3":
            title = input("Название: ")
            description = input("Описание: ")
            category = input("Категория: ")
            due_date = get_valid_date_input()
            priority = get_valid_priority_input()

            manager.add_task(title, description, category, due_date, priority)
            print('Задача была добавлена')

        elif choice == "4":
            try:
                task_id = int(input("Введите ID задачи для изменения: "))
                task = next((task for task in manager.tasks if task.id == task_id), None)
                if task:
                    title = input(f"Новое название (текущее: {task.title}): ")
                    description = input(f"Новое описание (текущее: {task.description}): ")
                    category = input(f"Новая категория (текущая: {task.category}): ")
                    due_date = get_valid_date_input()
                    priority = get_valid_priority_input()
                    manager.update_task(task, title=title, description=description, category=category,
                                        due_date=due_date, priority=priority)

                    print("Задача обновлена.")
                else:
                    print("Задача с таким ID не найдена.")
            except ValueError:
                print("Ошибка: введённый ID не является числом. Попробуйте снова.")

        elif choice == "5":
            try:
                task_id = int(input("Введите ID задачи для удаления: "))
                manager.delete_task(task_id)
                print("Задача удалена.")
            except ValueError:
                print("Ошибка: введённый ID не является числом. Попробуйте снова.")

        elif choice == "6":
            try:
                task_id = int(input("Введите ID задачи, чтобы отметить как выполненную: "))
                if manager.mark_task_as_completed(task_id):
                    print("Задача отмечена как выполненная.")
                else:
                    print("Задача с таким ID не найдена.")

            except ValueError:
                print("Ошибка: введённый ID не является числом. Попробуйте снова.")

        elif choice == "7":
            keyword = input("Введите ключевое слово для поиска (название, категория или статус выполнения): ")
            found_tasks = manager.search_tasks(keyword)
            show_tasks(found_tasks)

        elif choice == "0":
            break

        else:
            print("Некорректный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
