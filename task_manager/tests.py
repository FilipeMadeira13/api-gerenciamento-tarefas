from django.test import TestCase

from task_manager.models import Task

class TaskTestCase(TestCase):
    def setUp(self) -> None:
        Task.objects.create(title='test')

    def test_task_created_successfully(self):
        task = Task.objects.get(title='test')
        self.assertEqual(task.title, 'test')
        self.assertEqual(task.completed, False)