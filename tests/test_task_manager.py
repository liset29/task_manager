import json
import pytest
import tempfile
from models.task_manager import TaskManager


"""Фикстура для создания временного файла и инициализации TaskManager"""
@pytest.fixture
def task_manager():
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.close()

    with open(temp_file.name, 'w') as f:
        json.dump([], f)

    task_manager = TaskManager(temp_file.name)
    return task_manager


"""Фикстура для предоставления тестовых данных о задачах"""
@pytest.fixture
def sample_tasks():

    return [
        ("Task1", "надо покушать", "еда", "2024-12-12", "средний"),
        ("Task2", "работать", "работа", "2024-12-15", "высокий"),
    ]


"""Тест на добавление задачи"""
@pytest.mark.parametrize("title, description, category, due_date, priority", [
    ("Task1", "надо покушать", "еда", "2024-12-12", "средний")
])
def test_add_task(task_manager, title, description, category, due_date, priority):

    task_manager.add_task(title, description, category, due_date, priority)
    task = task_manager.tasks[0]

    assert len(task_manager.tasks) == 1
    assert task.title == title
    assert task.description == description
    assert task.category == category
    assert task.due_date == due_date
    assert task.priority == priority


"""Тест на удаление задачи"""
def test_delete_task(task_manager, sample_tasks):
    task_manager.add_task(*sample_tasks[0])
    task_manager.delete_task(1)

    assert len(task_manager.tasks) == 0


"""Тест на изменение статуса задачи на "Выполнена"""
def test_mark_task_as_done(task_manager, sample_tasks):
    task_manager.add_task(*sample_tasks[0])
    task = task_manager.tasks[0]
    task_manager.mark_task_as_completed(task.id)

    assert task.status == "Выполнена"


"""Параметризированный тест на поиск задач"""
@pytest.mark.parametrize(
    "task_data, search_keyword, expected_count, expected_title, expected_status",
    [
        # Тест 1: Поиск задач по категории "работа"
        (
                [
                    ("Task3", "работать", "работа", "2024-12-12", "высокий"),
                    ("Task4", "кушать", "работа", "2024-12-05", "средний")
                ],
                #ожидаемы результаты
                "работа",
                2,
                "Task3",
                None
        ),
        # Тест 2: Поиск задач по статусу "Выполнена"
        (
                [
                    ("Task3", "работать", "работа", "2024-12-12", "высокий"),
                    ("Task4", "кушать", "еда", "2024-12-05", "средний")
                ],
                #ожидаемы результаты
                "Выполнена",
                1,
                None,
                "Выполнена"
        )
    ]
)
def test_search_tasks(task_manager, task_data, search_keyword, expected_count, expected_title, expected_status):
    for title, description, category, due_date, priority in task_data:
        task_manager.add_task(title, description, category, due_date, priority)

    if search_keyword == "Выполнена":
        task_manager.mark_task_as_completed(1)

    found_tasks = task_manager.search_tasks(search_keyword)

    assert len(found_tasks) == expected_count

    if expected_title:
        assert found_tasks[0].title == expected_title

    if expected_status:
        assert found_tasks[0].status == expected_status


"""Тест на удаление несуществующей задачи"""
def test_delete_task_not_found(task_manager):
    initial_len = len(task_manager.tasks)
    task_manager.delete_task(999)
    assert len(task_manager.tasks) == initial_len
