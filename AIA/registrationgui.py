import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk  # Pillow library for image processing (install with: pip install Pillow)
from datetime import datetime

class AccessControlGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Access Control System")

        # Load and resize images
        logo_image = Image.open(r"C:\\Users\\hp\\OneDrive\\Documents\\sap Automation\\logo.png")  # Replace "logo.png" with your image file
        logo_image = logo_image.resize((100, 100), Image.Resampling.LANCZOS)
        self.logo = ImageTk.PhotoImage(logo_image)

        exit_image = Image.open(r"C:\\Users\\hp\\OneDrive\\Documents\\sap Automation\\exit.png")  # Replace with your exit image file
        exit_image = exit_image.resize((30, 30), Image.Resampling.LANCZOS)
        self.exit_icon = ImageTk.PhotoImage(exit_image)

        # Create labels
        logo_label = tk.Label(root, image=self.logo)
        logo_label.grid(row=0, column=0, columnspan=2, pady=10)

        access_label = tk.Label(root, text="Access Control System", font=("Helvetica", 16))
        access_label.grid(row=1, column=0, columnspan=2, pady=10)

        employee_id_label = tk.Label(root, text="Employee ID:")
        employee_id_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

        name_label = tk.Label(root, text="Name:")
        name_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")

        joining_date_label = tk.Label(root, text="Date of Joining (DD/MM/YYYY):")
        joining_date_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")

        validity_label = tk.Label(root, text="Validity of Contract (DD/MM/YYYY):")
        validity_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")

        gender_label = tk.Label(root, text="Gender:")
        gender_label.grid(row=6, column=0, padx=10, pady=5, sticky="e")

        mobile_label = tk.Label(root, text="Mobile Number:")
        mobile_label.grid(row=7, column=0, padx=10, pady=5, sticky="e")

        # Create entry widgets
        self.employee_id_entry = tk.Entry(root)
        self.employee_id_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        self.employee_id_entry.config(validate="key", validatecommand=(root.register(self.validate_employee_id), "%P"))

        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        self.name_entry.config(validate="key", validatecommand=(root.register(self.validate_name), "%P"))

        self.joining_date_entry = tk.Entry(root)
        self.joining_date_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        self.validity_entry = tk.Entry(root)
        self.validity_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        gender_options = ["Male", "Female"]
        self.gender_var = tk.StringVar(root)
        self.gender_var.set(gender_options[0])  # Default value
        gender_dropdown = ttk.OptionMenu(root, self.gender_var, *gender_options)
        gender_dropdown.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        self.mobile_entry = tk.Entry(root)
        self.mobile_entry.grid(row=7, column=1, padx=10, pady=5, sticky="w")
        self.mobile_entry.config(validate="key", validatecommand=(root.register(self.validate_mobile_number), "%P"))

        # Create Exit button
        exit_button = tk.Button(root, image=self.exit_icon, command=self.root.destroy, bd=0)
        exit_button.grid(row=0, column=1, pady=10)

        # Create Submit button
        submit_button = ttk.Button(root, text="Submit", command=self.submit_data)
        submit_button.grid(row=8, column=0, columnspan=2, pady=10)

    def validate_employee_id(self, new_text):
        return new_text.isalnum() or new_text == ""

    def validate_name(self, new_text):
        return new_text.isalpha() or new_text == ""

    def validate_mobile_number(self, new_text):
        return new_text.isdigit() and len(new_text) <= 10 or new_text == ""

    def validate_date(self, date_text):
        try:
            datetime.strptime(date_text, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def submit_data(self):
        employee_id = self.employee_id_entry.get()
        name = self.name_entry.get()
        joining_date = self.joining_date_entry.get()
        validity_date = self.validity_entry.get()
        gender = self.gender_var.get()
        mobile_number = self.mobile_entry.get()

        if not employee_id or not name or not joining_date or not validity_date or not mobile_number:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if not self.validate_date(joining_date) or not self.validate_date(validity_date):
            messagebox.showerror("Error", "Invalid date format. Please use DD/MM/YYYY.")
            return

        print("Employee ID:", employee_id)
        print("Name:", name)
        print("Joining Date:", joining_date)
        print("Validity Date:", validity_date)
        print("Gender:", gender)
        print("Mobile Number:", mobile_number)
        print("Data submitted")

if __name__ == "__main__":
    root = tk.Tk()
    app = AccessControlGUI(root)
    root.mainloop()
