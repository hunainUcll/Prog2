import pytest
from datetime import date, timedelta
from tasks import Task, TaskList
from calenders import CalendarStub


# Fixtures

@pytest.fixture
def today():
    return date(2000, 1, 1)

@pytest.fixture
def tomorrow(today):
    return today + timedelta(days=1)

@pytest.fixture
def yesterday(today):
    return today - timedelta(days=1)

@pytest.fixture
def calendar(today):
    return CalendarStub(today)

@pytest.fixture
def sut(calendar):
    return TaskList(calendar)


# Tests

def test_creation(sut):
    assert len(sut) == 0
    assert sut.due_tasks == []
    assert sut.overdue_tasks == []
    assert sut.finished_tasks == []


def test_adding_task_with_due_day_in_future(sut, tomorrow):
    task = Task("future task", tomorrow)

    sut.add_task(task)

    assert len(sut) == 1
    assert sut.due_tasks == [task]
    assert sut.overdue_tasks == []
    assert sut.finished_tasks == []


def test_adding_task_with_due_day_in_past(sut, yesterday):
    task = Task("past task", yesterday)

    with pytest.raises(RuntimeError):
        sut.add_task(task)


def test_task_becomes_finished(sut, tomorrow):
    task = Task("to finish", tomorrow)
    sut.add_task(task)

    task.finished = True

    assert task in sut.finished_tasks
    assert task not in sut.due_tasks
    assert task not in sut.overdue_tasks


def test_task_becomes_overdue(sut, calendar, tomorrow, today):
    task = Task("overdue one", tomorrow)
    sut.add_task(task)

    calendar.today = today + timedelta(days=7)

    assert sut.overdue_tasks == [task]
