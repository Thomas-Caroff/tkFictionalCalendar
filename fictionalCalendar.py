<<<<<<< HEAD
import tkinter as tk

class MyComponent(tk.Frame):
    def __init__(self, master, title, subtitle):
        super().__init__(master)
        self.master = master
        self.title = title
        self.subtitle = subtitle
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text=self.title, font=("Helvetica", 12)).pack()
        tk.Label(self, text=self.subtitle, font=("Helvetica", 12)).pack()
        self.create_button_grid()

    def create_button_grid(self, rows = 4, col = 5, max_days = 18):
        num_rows = rows  # Nombre de lignes
        num_cols = col  # Nombre de colonnes
        current_num = 1

        for row in range(num_rows):
            row_frame = tk.Frame(self)
            row_frame.pack()

            for col in range(num_cols):
                button = tk.Button(row_frame, text=str(current_num))
                button.pack(side=tk.LEFT)
                current_num += 1
                
                if (max_days !=0) and current_num > max_days:
                    break

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Mon Composant tkinter")

    title_text = "Titre de mon composant"
    subtitle_text = "Sous-titre de mon composant"

    component = MyComponent(root, title_text, subtitle_text)
    component.pack()

    root.mainloop()
=======
import tkinter as tk

class MyComponent(tk.Frame):
    def __init__(self, master, title, subtitle):
        super().__init__(master)
        self.master = master
        self.title = title
        self.subtitle = subtitle
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text=self.title, font=("Helvetica", 12)).pack()
        tk.Label(self, text=self.subtitle, font=("Helvetica", 12)).pack()
        self.create_button_grid()

    def create_button_grid(self, rows = 4, col = 5, max_days = 18):
        num_rows = rows  # Nombre de lignes
        num_cols = col  # Nombre de colonnes
        current_num = 1

        for row in range(num_rows):
            row_frame = tk.Frame(self)
            row_frame.pack()

            for col in range(num_cols):
                button = tk.Button(row_frame, text=str(current_num))
                button.pack(side=tk.LEFT)
                current_num += 1
                
                if (max_days !=0) and current_num > max_days:
                    break

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Mon Composant tkinter")

    title_text = "Titre de mon composant"
    subtitle_text = "Sous-titre de mon composant"

    component = MyComponent(root, title_text, subtitle_text)
    component.pack()

    root.mainloop()
>>>>>>> d9c5d03115c53e69c8fb3e8a45a36490a3f58a5b
