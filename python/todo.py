from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class Task:
    def __init__(self, name):
        self.name = name


class ToDoListApp(App):
    def build(self):
        self.tasks = []
        self.main_layout = BoxLayout(orientation='vertical')
        self.add_task_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        self.add_task_input = TextInput(hint_text="Enter task", multiline=False, size_hint=(0.8, 1))
        self.add_task_button = Button(text="Add Task", on_press=self.add_task, size_hint=(0.2, 1))

        self.add_task_layout.add_widget(self.add_task_input)
        self.add_task_layout.add_widget(self.add_task_button)
        self.main_layout.add_widget(self.add_task_layout)

        return self.main_layout

    def add_task(self, instance):
        task_name = self.add_task_input.text.strip()
        if task_name:
            task = Task(task_name)
            self.tasks.append(task)
            self.add_task_input.text = ""
            self.refresh_task_list()

    def refresh_task_list(self):
        task_list_layout = self.main_layout.children[1:]
        self.main_layout.clear_widgets()
        self.main_layout.add_widget(self.add_task_layout)

        for task in self.tasks:
            task_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
            task_input = TextInput(text=task.name, multiline=False, size_hint=(0.6, 1))
            edit_button = Button(text="Edit", on_press=self.edit_task, size_hint=(0.2, 1))
            delete_button = Button(text="Delete", on_press=self.delete_task, size_hint=(0.2, 1))

            task_layout.add_widget(task_input)
            task_layout.add_widget(edit_button)
            task_layout.add_widget(delete_button)
            self.main_layout.add_widget(task_layout)

    def edit_task(self, instance):
        task_layout = instance.parent
        task_input = task_layout.children[0]
        edited_task_name = task_input.text.strip()

        if edited_task_name:
            task_index = self.main_layout.children.index(task_layout) - 1
            self.tasks[task_index].name = edited_task_name

    def delete_task(self, instance):
        task_layout = instance.parent
        task_index = self.main_layout.children.index(task_layout) - 1
        del self.tasks[task_index]
        self.refresh_task_list()


if __name__ == "__main__":
    ToDoListApp().run()
