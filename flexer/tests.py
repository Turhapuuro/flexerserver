from django.test import TestCase
from flexer.models import Task
import datetime


class TaskTestCase(TestCase):
    def setUp(self):
        Task.objects.create(name="test task", start_date="2018-01-04T16:44:14.051000Z", end_date="2018-01-04T17:44:14.051000Z",
        break_time="00:30", total_hours="00:30")

    def test_task_is_created_correctly(self):
        task = Task.objects.get(name="test task")
        self.assertEqual(task.name, "test task")
        # fix datetime format equal comparison
        # self.assertEqual(task.start_date, datetime.datetime(2018, 1, 4, 16, 44, 14, 51000))
        # self.assertEqual(task.end_date, "2018-01-04T17:44:14.051000Z")
        self.assertEqual(task.break_time, datetime.time(0, 30))
        self.assertEqual(task.total_hours, datetime.time(0, 30))