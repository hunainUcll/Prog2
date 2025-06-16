from datetime import date, timedelta
from tasks import Task, TaskList
from calendars import CalendarStub
import pytest

# Shared globals for each test
today = None
tomorrow = None
yesterday = None
calendar = None
sut = None


def setup_function():
    global today, tomorrow, yesterday, calendar, sut
    today = date(2000, 1, 1)
    tomorrow = today + timedelta(days=1)
    yesterday = today - timedelta(days=1)
    calendar = CalendarStub(today)
    sut = TaskList(calendar)


def test_creation():
    # Assert
    assert len(sut) == 0
    assert sut.due_tasks == []
    assert sut.overdue_tasks == []
    assert sut.finished_tasks == []


def test_adding_task_with_due_day_in_future():
    # Arrange
    task = Task("future task", tomorrow)

    # Act
    sut.add_task(task)

    # Assert
    assert len(sut) == 1
    assert sut.due_tasks == [task]
    assert sut.overdue_tasks == []
    assert sut.finished_tasks == []


def test_adding_task_with_due_day_in_past():
    # Arrange
    task = Task("past task", yesterday)

    # Act & Assert
    with pytest.raises(RuntimeError):
        sut.add_task(task)


def test_task_becomes_finished():
    # Arrange
    task = Task("to finish", tomorrow)
    sut.add_task(task)

    # Act
    task.finished = True

    # Assert
    assert task in sut.finished_tasks
    assert task not in sut.due_tasks
    assert task not in sut.overdue_tasks


def test_task_becomes_overdue():
    # Arrange
    task = Task("overdue one", tomorrow)
    sut.add_task(task)

    # Act
    calendar.today = today + timedelta(days=7)

    # Assert
    assert sut.overdue_tasks == [task]
