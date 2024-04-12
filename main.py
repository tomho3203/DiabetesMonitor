# main.py
# Tom Ho
import tkinter as tk
from login_screen import LoginScreen
from bloodsugar import BloodSugarScreen

class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Diabetes Monitoring System")
        self.root.geometry('800x700')  # Set window size to maximum

        # Create and run the login screen
        self.login_screen = LoginScreen(self.root)
        
    def run(self):
        self.root.mainloop()
        

if __name__ == "__main__":
    app = MainApp()
    app.run()