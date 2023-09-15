import tkinter as tk

class Calendar(tk.Frame):
    def __init__(self, master, title, subtitle, info_editor):
        super().__init__(master)
        self.master = master
        self.title = title
        self.subtitle = subtitle
        self.info_editor = info_editor
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text=self.title, font=("Helvetica", 12)).pack()
        tk.Label(self, text=self.subtitle, font=("Helvetica", 12)).pack()
        self.create_button_grid()

    def create_button_grid(self, rows=4, cols=5, max_days=18):
        num_rows = rows
        num_cols = cols
        current_num = 1

        for row in range(num_rows):
            row_frame = tk.Frame(self)
            row_frame.pack()

            for col in range(num_cols):
                button = tk.Button(row_frame, text=str(current_num), width=9, height=4,
                                   command=lambda num=current_num: self.on_button_click(num))
                button.pack(side=tk.LEFT, padx=3, pady=3)
                current_num += 1
                
                if (max_days != 0) and current_num > max_days:
                    break

    def on_button_click(self, button_num):
        self.info_editor.update_info(button_num)

class InfoEditor(tk.Frame):
    def __init__(self, master):
        super().__init__(master, borderwidth=2, relief="solid")
        self.master = master
        self.title_label = tk.Label(self, text="", font=("Helvetica", 12))
        self.subtitle_label = tk.Label(self, text="", font=("Helvetica", 12))
        self.button_clicked_label = tk.Label(self, text="Bouton cliqué : N/A")
        self.editable_text = tk.Text(self, wrap=tk.WORD, height=10, width=40)
        
        self.title_label.pack()
        self.subtitle_label.pack()
        self.button_clicked_label.pack()
        self.editable_text.pack()

    def update_info(self, button_num):
        self.button_clicked_label.config(text=f"Bouton cliqué : {button_num}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Mon Application")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.geometry(f"{screen_width}x{screen_height}")

    title_text = "Année"
    subtitle_text = "Mois"

    width = 960
    height = 540

    frame_calendar = tk.Frame(root, width=width, height=height, borderwidth=4, relief="sunken")
    frame_calendar.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    frame_info_editor = tk.Frame(root, width=width, height=height, borderwidth=4, relief="sunken")
    frame_info_editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    component_info_editor = InfoEditor(frame_info_editor)
    component_info_editor.pack(fill=tk.BOTH, expand=True)

    component_calendar = Calendar(frame_calendar, title_text, subtitle_text, component_info_editor)
    component_calendar.pack(fill=tk.BOTH, expand=True)

    root.mainloop()
