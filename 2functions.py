

import json
from datetime import datetime
import random

class TaskManager:

    def __init__(self):
        self.tasks =[]

    def add_task(self, title, description):
        task_id = random.randint(1000, 9999)
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        task = task (task_id, title, description, created_at)
        self.tasks.append(task)
        print("Task added successfully!\n")

    def view_tasks(self):
        for t in self.tasks:
            print(f"ID:{t.id}, Title:{t.title}, Date: {t.created_at}")

    def update_task(self, id, new_title, new_description):
        for t in self.tasks:
            if t.id == id:
                t.title = new_title
                t.description = new_description
                print("Task updated!\n")

    def delete_task(self,id):
        for t in self.tasks:
            if t.id == id:
                self.tasks.remove(t)
                print("Task deleted!\n")

    def search_task(self, id):
        for t in self.tasks:
            if t.id == id:
                print(f"Found ->{t.title}: {t.description}")