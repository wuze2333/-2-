import tkinter as tk
from tkinter import messagebox

class State:
    def check(self, context):
        pass

    def publish(self, context):
        pass

class Draft(State):
    def check(self, context):
        messagebox.showinfo("Check", "Checking draft...")
        if self._is_valid():
            context.set_state(Review())
        else:
            context.set_state(NotPresented())

    def _is_valid(self):
        # 假设某些验证逻辑
        return True

class NotPresented(State):
    def check(self, context):
        messagebox.showinfo("Check", "Draft not presented. Needs to be revised.")
        context.set_state(Draft())

    def publish(self, context):
        messagebox.showwarning("Publish", "Cannot publish. Draft not presented.")

class Review(State):
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

class Poster(State):
    def publish(self, context):
        messagebox.showinfo("Publish", "Publishing poster...")
        context.set_state(Published())

    def check(self, context):
        messagebox.showinfo("Check", "Poster already reviewed.")

class Published(State):
    def publish(self, context):
        messagebox.showinfo("Publish", "Already published.")

    def check(self, context):
        messagebox.showwarning("Check", "Cannot check. Already published.")

class Context:
    def __init__(self, label):
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
        self.label.config(text=f"Current State: {state_name}")

def check_action():
    context.check()

def publish_action():
    context.publish()

# 创建GUI应用
app = tk.Tk()
app.title("Document State Manager")
app.geometry("400x300")

# 状态标签
state_label = tk.Label(app, text="Current State: Draft", font=("Arial", 12))
state_label.pack(pady=10)

context = Context(state_label)

# 检查按钮
check_button = tk.Button(app, text="Check", command=check_action, width=20)
check_button.pack(pady=5)

# 发布按钮
publish_button = tk.Button(app, text="Publish", command=publish_action, width=20)
publish_button.pack(pady=5)

app.mainloop()
