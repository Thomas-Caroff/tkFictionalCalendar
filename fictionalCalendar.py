import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import os

print(os.getcwd())


class Calendar(tk.Frame):
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
        
        icon_image = Image.open("icon.png")
        icon_photo = ImageTk.PhotoImage(icon_image)
        
        button_with_icon = [3,16]

        for row in range(num_rows):
            row_frame = tk.Frame(self)
            row_frame.pack()

            for col in range(num_cols):
                button = tk.Button(row_frame, text=str(current_num), width=9, height=4)
                
                if current_num in button_with_icon:
                    button.config(image=icon_photo, compound="top")  # Vous pouvez également utiliser "left", "right", ou "bottom"
                    button.image = icon_photo  # Garder une référence à l'image

                button.pack(side=tk.LEFT, padx=3, pady=3)
                current_num += 1
                
                if (max_days !=0) and current_num > max_days:
                    break

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Fictionnal calendar")
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.geometry(f"{screen_width}x{screen_height}")

    title_text = "Année"
    subtitle_text = "Mois"
    
    width = 960
    height = 540
    
    frame = tk.Frame(width=width, height=height, borderwidth=4, relief="sunken")
    frame.place(anchor="nw")

    component = Calendar(frame, title_text, subtitle_text)
    component.pack(fill=tk.BOTH, expand=True)

    root.mainloop()
