import datetime

class Task:
    
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date

    def __str__(self):
        return f'{self.description} and {self.due_date}'

task1 = Task("Buy Milk", datetime.date.today() )
task2 = Task("Buy Bread", datetime.date(2019, 5, 20))
taskk3 = Task("Buy something", datetime.date(2019, 7, 7))

print(task1, task2)

class TodoList:
    def __init__(self, name)
        self.name = name
        self.todo_list = []

    def add_task(self, task):
        self.todo_list.append(task)

my_requests = TodoList("my goals")

print(my_task.todo_lis.task1)
my_requests.add_task(task1)

print(my_task.todo_lis.task1)
my_requests.add_task(task1)

print(my_task.todo_lis.task2)
my_requests.add_task(task2)

print(my_task.todo_lis.task3)
my_requests.add_task(task3)
