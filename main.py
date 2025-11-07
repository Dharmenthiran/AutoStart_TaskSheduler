import sys
import tkinter as tk
import os
import subprocess

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("300x400")
        self.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        # Input field
        input_frame = tk.Frame(self, height=50, bg="lightgrey")
        input_frame.pack(side="top", fill="x")
        input_field = tk.Entry(input_frame, textvariable=self.input_text,
                               font=('arial', 18, 'bold'),
                               bd=5, relief="ridge", justify="right")
        input_field.pack(fill="both", expand=True, padx=5, pady=5)

        # Buttons
        btns_frame = tk.Frame(self)
        btns_frame.pack(fill="both", expand=True)

        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+')
        ]

        for row in buttons:
            row_frame = tk.Frame(btns_frame)
            row_frame.pack(expand=True, fill="both")
            for btn in row:
                button = tk.Button(row_frame, text=btn, font=('arial', 18),
                                   relief="ridge", bd=3,
                                   command=lambda x=btn: self.on_click(x))
                button.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == "=":
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)


# 🔹 Add program to Task Scheduler (all users)
def add_to_task_scheduler(task_name="MyCalculatorApp"):
    # If running as exe, use sys.executable
    if getattr(sys, 'frozen', False):
        exe_path = sys.executable
    else:
        # Development path (when running .py directly)
        exe_path = r"D:\AutoStart\dist\main.exe"

    # Create a scheduled task that runs at user login (better for GUI apps)
    cmd = f'schtasks /Create /SC ONLOGON /TN "{task_name}" /TR "{exe_path}" /RL HIGHEST /F'

    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print("Task Scheduler entry created successfully.")
        else:
            print("Error:", result.stderr)
    except Exception as e:
        print("Failed to create Task Scheduler entry:", e)


if __name__ == "__main__":
    # Add task to scheduler
    add_to_task_scheduler()

    # Start calculator
    app = Calculator()
    app.mainloop()
