import tkinter as tk
from tkinter import ttk, messagebox
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import red

class ResumeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Resume Generator")
        self.create_widgets()

    def create_widgets(self):
        # Name
        self.name_label = ttk.Label(self.root, text="Name:")
        self.name_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.name_entry = ttk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Email
        self.email_label = ttk.Label(self.root, text="Email:")
        self.email_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.email_entry = ttk.Entry(self.root)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)

        # Address
        self.address_label = ttk.Label(self.root, text="Address:")
        self.address_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.address_entry = ttk.Entry(self.root)
        self.address_entry.grid(row=2, column=1, padx=5, pady=5)

        # Phone
        self.phone_label = ttk.Label(self.root, text="Phone:")
        self.phone_label.grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.phone_entry = ttk.Entry(self.root)
        self.phone_entry.grid(row=3, column=1, padx=5, pady=5)

        # Summary
        self.summary_label = ttk.Label(self.root, text="Summary:")
        self.summary_label.grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.summary_entry = tk.Text(self.root, height=5, width=40)
        self.summary_entry.grid(row=4, column=1, padx=5, pady=5)

        # Experience
        self.exp_label = ttk.Label(self.root, text="Experience:")
        self.exp_label.grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.exp_entry = tk.Text(self.root, height=5, width=40)
        self.exp_entry.grid(row=5, column=1, padx=5, pady=5)

        # Education
        self.edu_label = ttk.Label(self.root, text="Education:")
        self.edu_label.grid(row=6, column=0, sticky="w", padx=5, pady=5)
        self.edu_entry = tk.Text(self.root, height=5, width=40)
        self.edu_entry.grid(row=6, column=1, padx=5, pady=5)

        # Button to generate the resume
        self.generate_btn = ttk.Button(self.root, text="Generate Resume", command=self.generate_resume)
        self.generate_btn.grid(row=7, column=0, columnspan=2, pady=20)

    def collect_user_input(self):
        return {
            'name': self.name_entry.get(),
            'email': self.email_entry.get(),
            'address': self.address_entry.get(),
            'phone': self.phone_entry.get(),
            'summary': self.summary_entry.get(1.0, "end-1c"),
            'experience': self.exp_entry.get(1.0, "end-1c"),
            'education': self.edu_entry.get(1.0, "end-1c")
        }

    def generate_resume(self):
        data = self.collect_user_input()
        self.create_pdf(data)
        messagebox.showinfo("Info", "Resume generated as 'resume.pdf'")

    def create_pdf(self, data):
        doc = SimpleDocTemplate("resume.pdf", pagesize=letter)
        story = []

        styles = getSampleStyleSheet()
        custom_style = ParagraphStyle(
            "CustomStyle",
            parent=styles["BodyText"],
            textColor=red,
            fontSize=14,
            spaceAfter=6
        )

        name = Paragraph(f"<font size=24><b>{data['name']}</b></font>", styles['Heading1'])
        email = Paragraph(f"<font color=blue>{data['email']}</font>", custom_style)
        address = Paragraph(data['address'], custom_style)
        phone = Paragraph(data['phone'], custom_style)
        summary = Paragraph(data['summary'], styles['BodyText'])
        experience = Paragraph(data['experience'], styles['BodyText'])
        education = Paragraph(data['education'], styles['BodyText'])

        story.extend([
            name, Spacer(1, 0.2 * inch), 
            email, Spacer(1, 0.2 * inch), 
            address, Spacer(1, 0.2 * inch), 
            phone, Spacer(1, 0.5 * inch), 
            summary, Spacer(1, 0.5 * inch), 
            experience, Spacer(1, 0.5 * inch), 
            education
        ])

        doc.build(story)

if __name__ == "__main__":
    root = tk.Tk()
    app = ResumeApp(root)
    root.mainloop()
