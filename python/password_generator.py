import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # Username Entry
        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(root, width=30)
        self.username_entry.pack(pady=5)

        # Password Length Entry
        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack(pady=5)
        self.length_entry = tk.Entry(root, width=10)
        self.length_entry.pack(pady=5)

        # Generate Password Button
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        # Display Password
        self.password_display = tk.Label(root, text="", font=("Courier", 12))
        self.password_display.pack(pady=10)

        # Accept Button
        self.accept_button = tk.Button(root, text="Accept", command=self.accept_password)
        self.accept_button.pack(pady=5)

        # Reset Button
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_password)
        self.reset_button.pack(pady=5)

    def generate_password(self):
        length = int(self.length_entry.get())

        if length <= 0:
            self.password_display.config(text="Invalid password length")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = ''.join(random.choice(characters) for _ in range(length))
        self.password_display.config(text=generated_password)

    def accept_password(self):
        username = self.username_entry.get()
        password = self.password_display.cget("text")
        if username and password:
            # You can add your desired functionality here, like storing the username and password.
            print("Accepted: Username:", username, "Password:", password)
            self.reset_password()

    def reset_password(self):
        self.username_entry.delete(0, tk.END)
        self.length_entry.delete(0, tk.END)
        self.password_display.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
