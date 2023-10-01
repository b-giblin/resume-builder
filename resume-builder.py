import tkinter as tk
from tkinter import ttk, messagebox
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

class ResumeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Resume Generator")
        self.create_widgets()

    def create_widgets(self):
        self.name_label = ttk.Label(self.root, text="Name:")
        self.name_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.name_entry = ttk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.email_label = ttk.Label(self.root, text="Email:")
        self.email_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.email_entry = ttk.Entry(self.root)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)

        self.summary_label = ttk.Label(self.root, text="Summary:")
        self.summary_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.summary_entry = tk.Text(self.root, height=5, width=40)
        self.summary_entry.grid(row=2, column=1, padx=5, pady=5)

        self.generate_btn = ttk.Button(self.root, text="Generate Resume", command=self.generate_resume)
        self.generate_btn.grid(row=4, column=0, columnspan=2, pady=20)

    def collect_user_input(self):
        return {
            'name': self.name_entry.get(),
            'email': self.email_entry.get(),
            'summary': self.summary_entry.get(1.0, "end-1c")
        }

    def generate_resume(self):
        data = self.collect_user_input()
        self.create_pdf(data)
        messagebox.showinfo("Info", "Resume generated as 'resume.pdf'")

    def create_pdf(self, data):
        doc = SimpleDocTemplate("resume.pdf", pagesize=letter)
        story = []

        styles = getSampleStyleSheet()

        name = Paragraph(f"<font size=18><b>{data['name']}</b></font>", styles['Heading1'])
        email = Paragraph(data['email'], styles['BodyText'])
        summary = Paragraph(data['summary'], styles['BodyText'])

        story.extend([name, Spacer(1, 0.2 * inch), email, Spacer(1, 0.5 * inch), summary])

        doc.build(story)

if __name__ == "__main__":
    root = tk.Tk()
    app = ResumeApp(root)
    root.mainloop()