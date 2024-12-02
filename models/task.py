from typing import Optional


class Task:
    def __init__(self, id: int, title: str, description: str, category: str, due_date: str, priority: str):
        """Конструктор для создания задачи."""
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.status = "Не выполнена"

    def mark_as_done(self):
        """Отмечает задачу как выполненную, изменяя ее статус на "Выполнена"."""
        self.status = "Выполнена"

    def update(self, title: Optional[str] = None, description: Optional[str] = None,
               category: Optional[str] = None, due_date: Optional[str] = None, priority: Optional[str] = None):
        """Обновляет атрибуты задачи. Если какой-то из параметров не передан,
        соответствующий атрибут не изменяется."""
        if title:
            self.title = title
        if description:
            self.description = description
        if category:
            self.category = category
        if due_date:
            self.due_date = due_date
        if priority:
            self.priority = priority

    def to_dict(self):
        """Преобразует объект задачи в словарь."""
        return self.__dict__

    @staticmethod
    def from_dict(data: dict):
        """Создает объект задачи из словаря."""
        task = Task(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            category=data["category"],
            due_date=data["due_date"],
            priority=data["priority"],
        )
        task.status = data["status"]
        return task
