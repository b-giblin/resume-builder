import tkinter as tk
from tkinter import simpledialog, messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class ResumeApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Resume Generator")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Choose a Template Style:")
        self.label.pack(pady=20)

        # Buttons for different styles
        self.style1_btn = tk.Button(self.root, text="Style 1", command=self.generate_style1)
        self.style1_btn.pack(pady=10)

        self.style2_btn = tk.Button(self.root, text="Style 2", command=self.generate_style2)
        self.style2_btn.pack(pady=10)

    def collect_user_input(self):
        user_data = {}
        user_data['name'] = simpledialog.askstring("Input", "Enter your name:")
        user_data['address'] = simpledialog.askstring("Input", "Enter your address:")
        user_data['email'] = simpledialog.askstring("Input", "Enter your email:")
        return user_data

    def generate_style1(self):
        data = self.collect_user_input()
        c = canvas.Canvas("resume_style1.pdf", pagesize=letter)
        width, height = letter

        c.drawString(100, height - 100, f"Name: {data['name']}")
        c.drawString(100, height - 130, f"Address: {data['address']}")
        c.drawString(100, height - 160, f"Email: {data['email']}")

        c.save()
        messagebox.showinfo("Info", "Resume generated as 'resume_style1.pdf'")

    def generate_style2(self):
        data = self.collect_user_input()
        c = canvas.Canvas("resume_style2.pdf", pagesize=letter)
        width, height = letter

        c.drawString(100, height - 100, f"==== {data['name']} ====")
        c.drawString(100, height - 130, f"[Address] {data['address']}")
        c.drawString(100, height - 160, f"[Email] {data['email']}")

        c.save()
        messagebox.showinfo("Info", "Resume generated as 'resume_style2.pdf'")

if __name__ == "__main__":
    root = tk.Tk()
    app = ResumeApp(root)
    root.mainloop()