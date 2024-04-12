import tkinter as tk
from tkinter import messagebox
from bloodsugar import BloodSugarScreen

class LoginScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Diabetes Monitoring System")
        self.create_widgets()

    def create_widgets(self):
        # Create a label
        tk.Label(self.root, text="Select your name:").pack()

        # Create a dropdown menu with user names
        self.user_var = tk.StringVar()
        self.user_var.set("Select User")  # Default value
        user_names = ["Sara Norman", "Greg Norman"]
        user_dropdown = tk.OptionMenu(self.root, self.user_var, *user_names)
        user_dropdown.pack()

        # Create a login button
        tk.Button(self.root, text="Login", command=self.login).pack()

        # Exit button
        tk.Button(self.root, text="Exit", command=self.exit).pack()

        #Help button
        self.help_button = tk.Button(self.root, text="Help", command=self.show_help)
        self.help_button.pack(pady=10)

    def login(self):
        selected_user = self.user_var.get()
        if selected_user == "Select User":
            messagebox.showerror("Error", "Please select a valid user.")
        else:
            self.show_blood_sugar_screen(selected_user)

    def show_blood_sugar_screen(self, user_name):
        # Create and show the BloodSugarScreen
        blood_sugar_root = tk.Tk()  # Create a new window for blood sugar screen
        blood_sugar_screen = BloodSugarScreen(blood_sugar_root, user_name)
    def show_help(self):
        self.help_text = """
    Welcome to the Diabetic Monitoring System!\n\n
    This system assists in tracking your blood sugar levels and offers guidance based on your readings.\n
    Here's how to use the system:\n
    1. Choose your name from the dropdown menu and click Login.\n
    2. If you haven't taken your blood sugar reading yet, select "No" and measure it promptly.\n
    3. Once you have taken your reading, enter your blood sugar reading (0-999) and click "Record Reading"\n
    4. You'll receive information on whether it's low, normal, or high.\n
    5. If your reading is abnormal (too high or too low), you'll be prompted to provide an explanation.\n
    6. If your reading is high, you'll be asked about the presence of ketones.\n
    7. To exit the system, click Logout after use.\n
    For further assistance, please consult your doctor.\n
    """
        messagebox.showinfo("Help", self.help_text)

    def exit(self):
        self.root.destroy()  # Close the window
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginScreen(root)
    root.mainloop()
