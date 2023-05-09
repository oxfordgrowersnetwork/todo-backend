from enum import Enum

import humps


class Recurrence(Enum):
    NEVER = 0,
    WEEKLY = 1,
    MONTHLY = 2,
    YEARLY = 3


class Task:
    '''
    Python class representing the task object
    '''

    def __init__(self, task_name, enabledMonths: set[int], recurrence: Recurrence):
        self.task_name = task_name
        self.enabled_months = enabledMonths
        self.recurrence = recurrence.name
        self.last_completed = None

    def to_json(self):
        return humps.camelize(self.__dict__)
