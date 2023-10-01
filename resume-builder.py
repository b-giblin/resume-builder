import tkinter as tk
from tkinter import ttk, messagebox
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import requests


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
        
        message = f"Generate a detailed resume using the following details:\n"
        for key, value in data.items():
            message += f"{key.capitalize()}: {value}\n"

        response = self.request_openai_api(message)

        if response and 'choices' in response and len(response['choices']) > 0:
            detailed_resume = response['choices'][0]['text'].strip()
            self.create_pdf(detailed_resume)
            messagebox.showinfo("Info", "Resume generated as 'resume.pdf'")
        else:
            messagebox.showerror("Error", "Failed to generate the resume.")

    def request_openai_api(self, message):
        endpoint = "https://api.openai.com/v1/engines/davinci/completions"
        headers = {
            "Authorization": f"Bearer YOUR_OPENAI_API_KEY",  # Replace with your API key
            "Content-Type": "application/json"
        }
        data = {
            "prompt": message,
            "max_tokens": 500
        }
        response = requests.post(endpoint, headers=headers, json=data).json()
        return response

    def create_pdf(self, detailed_resume):
        doc = SimpleDocTemplate("resume.pdf", pagesize=letter)
        story = []
        styles = getSampleStyleSheet()
        content = Paragraph(detailed_resume, styles['BodyText'])
        story.extend([content])
        doc.build(story)


if __name__ == "__main__":
    root = tk.Tk()
    app = ResumeApp(root)
    root.mainloop()