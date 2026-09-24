"""A simple Tkinter form that validates and displays user information."""

import re
import tkinter as tk
from tkinter import messagebox, ttk


EMAIL_PATTERN = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"


class InformationForm:
    """Create and manage the information-entry window."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Personal Information")
        self.root.geometry("500x560")
        self.root.minsize(420, 500)

        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.color_var = tk.StringVar()
        self.status_var = tk.StringVar()

        self.build_interface()

    def build_interface(self) -> None:
        """Build the form, buttons, and output area."""
        main_frame = ttk.Frame(self.root, padding=24)
        main_frame.pack(fill="both", expand=True)

        ttk.Label(
            main_frame,
            text="Personal Information",
            font=("TkDefaultFont", 16, "bold"),
        ).pack(anchor="w")
        ttk.Label(
            main_frame,
            text="Enter your details below, then select Submit.",
        ).pack(anchor="w", pady=(4, 18))

        form_frame = ttk.Frame(main_frame)
        form_frame.pack(fill="x")
        form_frame.columnconfigure(1, weight=1)

        self.add_field(form_frame, "Name:", self.name_var, 0)
        self.add_field(form_frame, "Age:", self.age_var, 1)
        self.add_field(form_frame, "Email:", self.email_var, 2)
        self.add_field(form_frame, "Favorite color:", self.color_var, 3)

        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill="x", pady=(20, 10))
        ttk.Button(button_frame, text="Submit", command=self.submit).pack(side="left")
        ttk.Button(button_frame, text="Clear", command=self.clear).pack(
            side="left", padx=(10, 0)
        )

        ttk.Label(
            main_frame,
            textvariable=self.status_var,
            foreground="#b00020",
            wraplength=440,
        ).pack(anchor="w", pady=(0, 12))

        ttk.Label(main_frame, text="Output:").pack(anchor="w")
        self.output = tk.Text(
            main_frame,
            height=10,
            wrap="word",
            state="disabled",
            background="#f4f4f4",
        )
        self.output.pack(fill="both", expand=True, pady=(5, 0))

        self.name_entry.focus_set()
        self.root.bind("<Return>", lambda _event: self.submit())

    def add_field(
        self,
        parent: ttk.Frame,
        label_text: str,
        variable: tk.StringVar,
        row: int,
    ) -> None:
        """Add a labeled input field to the form."""
        ttk.Label(parent, text=label_text).grid(
            row=row, column=0, sticky="w", padx=(0, 12), pady=6
        )
        entry = ttk.Entry(parent, textvariable=variable)
        entry.grid(row=row, column=1, sticky="ew", pady=6)
        if row == 0:
            self.name_entry = entry

    def validate(self) -> tuple[bool, str]:
        """Validate all fields and return a useful message for invalid input."""
        name = self.name_var.get().strip()
        age_text = self.age_var.get().strip()
        email = self.email_var.get().strip()
        color = self.color_var.get().strip()

        if not name:
            return False, "Please enter your name."
        if len(name) > 100:
            return False, "Name must be 100 characters or fewer."
        if not age_text:
            return False, "Please enter your age."
        try:
            age = int(age_text)
        except ValueError:
            return False, "Age must be a whole number, such as 25."
        if not 0 <= age <= 120:
            return False, "Age must be between 0 and 120."
        if not re.fullmatch(EMAIL_PATTERN, email):
            return False, "Please enter a valid email address."
        if not color:
            return False, "Please enter your favorite color."
        if len(color) > 50:
            return False, "Favorite color must be 50 characters or fewer."

        return True, ""

    def submit(self) -> None:
        """Validate the form and display the submitted information."""
        valid, error_message = self.validate()
        if not valid:
            self.status_var.set(error_message)
            self.output.configure(state="normal")
            self.output.delete("1.0", tk.END)
            self.output.configure(state="disabled")
            return

        self.status_var.set("Information submitted successfully.")
        result = (
            f"Name: {self.name_var.get().strip()}\n"
            f"Age: {int(self.age_var.get().strip())}\n"
            f"Email: {self.email_var.get().strip()}\n"
            f"Favorite color: {self.color_var.get().strip()}"
        )
        self.output.configure(state="normal")
        self.output.delete("1.0", tk.END)
        self.output.insert("1.0", result)
        self.output.configure(state="disabled")

    def clear(self) -> None:
        """Clear all fields, messages, and displayed output."""
        fields = (self.name_var, self.age_var, self.email_var, self.color_var)
        if any(value.get().strip() for value in fields):
            if not messagebox.askyesno("Clear form", "Are you sure you want to clear the form?"):
                return

        for variable in fields:
            variable.set("")
        self.status_var.set("")
        self.output.configure(state="normal")
        self.output.delete("1.0", tk.END)
        self.output.configure(state="disabled")
        self.name_entry.focus_set()


def main() -> None:
    root = tk.Tk()
    InformationForm(root)
    root.mainloop()


if __name__ == "__main__":
    main()
