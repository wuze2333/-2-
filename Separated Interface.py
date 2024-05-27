import tkinter as tk
from tkinter import messagebox, simpledialog
from abc import ABC, abstractmethod

# 定义状态接口
class TaskState(ABC):
    @abstractmethod
    def check(self, context):
        pass

    @abstractmethod
    def publish(self, context):
        pass

# 具体状态类实现接口
class Draft(TaskState):
    def check(self, context):
        messagebox.showinfo("Check", "Checking draft...")
        if self._is_valid():
            context.set_state(Review())
        else:
            context.set_state(NotPresented())

    def _is_valid(self):
        # 假设某些验证逻辑
        return True

    def publish(self, context):
        messagebox.showwarning("Publish", "Cannot publish. Draft not reviewed.")

class NotPresented(TaskState):
    def check(self, context):
        messagebox.showinfo("Check", "Draft not presented. Needs to be revised.")
        context.set_state(Draft())

    def publish(self, context):
        messagebox.showwarning("Publish", "Cannot publish. Draft not presented.")

class Review(TaskState):
    def check(self, context):
        messagebox.showinfo("Check", "Reviewing...")
        if self._is_valid():
            context.set_state(Poster())
        else:
            context.set_state(NotPresented())

    def _is_valid(self):
        # 假设某些验证逻辑
        return True

    def publish(self, context):
        messagebox.showwarning("Publish", "Cannot publish. Review in progress.")

class Poster(TaskState):
    def check(self, context):
        messagebox.showinfo("Check", "Poster already reviewed.")

    def publish(self, context):
        messagebox.showinfo("Publish", "Publishing poster...")
        context.set_state(Published())

class Published(TaskState):
    def check(self, context):
        messagebox.showwarning("Check", "Cannot check. Already published.")

    def publish(self, context):
        messagebox.showinfo("Publish", "Already published.")

# 上下文类
class Task:
    def __init__(self, name, label):
        self.name = name
        self.state = Draft()
        self.label = label
        self.update_state_label()

    def set_state(self, state):
        self.state = state
        self.update_state_label()

    def check(self):
        self.state.check(self)

    def publish(self):
        self.state.publish(self)

    def update_state_label(self):
        state_name = self.state.__class__.__name__
        self.label.config(text=f"Task: {self.name} | State: {state_name}")

# GUI部分
def add_task():
    task_name = simpledialog.askstring("Input", "Enter the task name:")
    if task_name:
        task_label = tk.Label(task_frame, text="", font=("Arial", 10))
        task_label.pack(pady=5)
        task = Task(task_name, task_label)
        tasks.append(task)
        task.update_state_label()

def start_task():
    task_name = simpledialog.askstring("Input", "Enter the task name to start:")
    for task in tasks:
        if task.name == task_name:
            task.check()
            return
    messagebox.showwarning("Warning", f"No task named '{task_name}' found.")

def complete_task():
    task_name = simpledialog.askstring("Input", "Enter the task name to complete:")
    for task in tasks:
        if task.name == task_name:
            task.publish()
            return
    messagebox.showwarning("Warning", f"No task named '{task_name}' found.")

# 创建GUI应用
app = tk.Tk()
app.title("Task Manager")
app.geometry("400x300")

tasks = []

task_frame = tk.Frame(app)
task_frame.pack(pady=20)

# 添加任务按钮
add_task_button = tk.Button(app, text="Add Task", command=add_task, width=20)
add_task_button.pack(pady=5)

# 开始任务按钮
start_task_button = tk.Button(app, text="Start Task", command=start_task, width=20)
start_task_button.pack(pady=5)

# 完成任务按钮
complete_task_button = tk.Button(app, text="Complete Task", command=complete_task, width=20)
complete_task_button.pack(pady=5)

app.mainloop()
