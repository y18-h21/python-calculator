import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Advanced Calculator")
        self.geometry("340x470")
        self.resizable(False, False)
        self.create_widgets()
        self.history = []  # To keep track of calculation history

    def create_widgets(self):
        self.expression = ""

        # Entry widget to display expressions and results
        self.entry = tk.Entry(self, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, pady=10, padx=5, sticky="nsew")

        # Button colors
        button_colors = {
            'numbers': "#CCCCCC",
            'operators': "#FFB74D",
            'equals': "#81C784",
            'clear': "#E57373",
            'delete': "#64B5F6",
            'history': "#BA68C8",
            'back': "#FFD54F"
        }

        # Buttons layout with color categories
        buttons = [
            ('7', 1, 0, 'numbers'), ('8', 1, 1, 'numbers'), ('9', 1, 2, 'numbers'), ('/', 1, 3, 'operators'),
            ('4', 2, 0, 'numbers'), ('5', 2, 1, 'numbers'), ('6', 2, 2, 'numbers'), ('*', 2, 3, 'operators'),
            ('1', 3, 0, 'numbers'), ('2', 3, 1, 'numbers'), ('3', 3, 2, 'numbers'), ('-', 3, 3, 'operators'),
            ('0', 4, 0, 'numbers'), ('.', 4, 1, 'numbers'), ('=', 4, 2, 'equals'), ('+', 4, 3, 'operators'),
            ('C', 5, 0, 'clear'), ('Del', 5, 1, 'delete'), ('Back', 5, 2, 'back'), ('Hist', 5, 3, 'history')
        ]

        for (text, row, col, category) in buttons:
            action = lambda x=text: self.on_button_click(x)
            tk.Button(
                self,
                text=text,
                width=5,
                height=2,
                font=("Arial", 16),
                bg=button_colors.get(category, "#FFFFFF"),
                activebackground="#BDBDBD",
                command=action
            ).grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.entry.delete(0, tk.END)
        elif char == 'Del':
            self.expression = self.expression[:-1]
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.history.append(f"{self.expression} = {result}")
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
                self.expression = result
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.expression = ""
        elif char == 'Back':
            if self.history:
                last_calc = self.history.pop()
                expression = last_calc.split(' = ')[0]
                self.expression = expression
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, expression)
        elif char == 'Hist':
            self.show_history()
        else:
            self.expression += str(char)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)

    def show_history(self):
        history_window = tk.Toplevel(self)
        history_window.title("Calculation History")
        history_window.geometry("300x300")
        
        history_text = tk.Text(history_window, font=("Arial", 12), wrap='word')
        history_text.pack(expand=True, fill='both')

        if self.history:
            for calc in reversed(self.history):
                history_text.insert(tk.END, calc + "\n")
        else:
            history_text.insert(tk.END, "No history available.")

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
