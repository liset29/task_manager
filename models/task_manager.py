import json
from typing import List, Optional

from models.task import Task



class TaskManager:
    def __init__(self, file_path: str):
        """Конструктор для создания менеджера задач."""
        self.file_path = file_path
        self.tasks: List[Task] = []
        self.load_tasks()

    def load_tasks(self):
        """Загружает задачи из файла.
        Если файл не существует, создается пустой список задач."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.tasks = [Task.from_dict(task) for task in data]
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        """Сохраняет все задачи в файл."""
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump([task.to_dict() for task in self.tasks], file, ensure_ascii=False, indent=4)

    def add_task(self, title: str, description: str, category: str, due_date: str, priority: str):
        """Добавляет новую задачу в список и сохраняет её в файл."""
        task_id = max([task.id for task in self.tasks], default=0) + 1
        new_task = Task(task_id, title, description, category, due_date, priority)
        self.tasks.append(new_task)
        self.save_tasks()

    def list_tasks(self, category: Optional[str] = None, status: Optional[str] = None):
        """Возвращает список задач, отфильтрованных по категории и/или статусу."""
        filtered_tasks = self.tasks
        if category:
            filtered_tasks = [task for task in filtered_tasks if task.category == category]
        if status:
            filtered_tasks = [task for task in filtered_tasks if task.status == status]
        return filtered_tasks

    def delete_task(self, task_id: int):
        """Удаляет задачу по её идентификатору и сохраняет изменения в файл."""
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save_tasks()

    def search_tasks(self, keyword: str):
        """Ищет задачи по ключевому слову в заголовке, описании или категории."""
        return [task for task in self.tasks if
                keyword.lower() in task.title.lower()
                or keyword.lower() in task.description.lower()
                or keyword.lower() in task.category.lower()]
