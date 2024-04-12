import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog


class BloodSugarScreen:
    def __init__(self, root, user_name):
        self.root = root
        self.root.title("Blood Sugar Monitoring")
        self.root.geometry('900x700')
        self.user_name = user_name
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        self.patient_data = self.get_patient_data(user_name)
        self.create_widgets(self.user_name)
        
        patientID = "00000"
        doctorName = "N/A"
        doctorNumber = "0000"
        lowGlucose = 0
        highGlucose = 0

    def get_patient_data(self,user_name):
        if user_name == "Sara Norman":
            patientID = "5344-9709"
            doctorName = "Dr. Jason Rosenberg"
            doctorNumber = "579-0432"
            lowGlucose = 80
            highGlucose = 140
        else:
            patientID = "1275-4307"
            doctorName = "Dr. Nikhil Singh"
            doctorNumber = "334-2309"
            lowGlucose = 70
            highGlucose = 120
        return{
            "patientID": patientID,
            "doctorName": doctorName,
            "doctorNumber": doctorNumber,
            "lowGlucose": lowGlucose,
            "highGlucose": highGlucose
        }

    def create_widgets(self,user_name):

        # Display user's name and ID in the corner
        nameID = tk.Label(self.root, text=f"{self.user_name}: {self.patient_data['patientID']}", font=("Helvetica", 12))
        nameID.place(x=750,y=0)


        # Display user's name
        tk.Label(self.root, text=f"Welcome, {self.user_name}!", font=("Helvetica", 16)).pack()

        #Ask user if they have taken their blood reading
        blood_reading = tk.Label(self.root, text=f"Have you taken your blood reading today?", font=("Helvetica", 16))
        blood_reading.pack()
        self.yes_button=tk.Button(self.root, text="Yes", command=self.record_reading).pack()
        self.no_button=tk.Button(self.root, text="No", command=self.record_reading_no).pack()

        # Label for "Take your reading"
        self.take_reading_label = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.take_reading_label.pack()

        # Record results
        self.record_results = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.record_results.pack()

        self.blood_sugar_entry = tk.Entry(self.root)

        # Record button
        self.record_button=tk.Button(self.root, text="Record Reading", command=self.record_reading)
        ToolTip(self.record_button, "Click once reading has been entered")

        # Ketones button
        self.ketones = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.ketones_yes = tk.Button(self.root, text="Yes",command=self.ketones_msg)
        self.ketones_no = tk.Button(self.root, text="No",command=self.ketones_msg_no)
        ToolTip(self.ketones_yes, "Click if ketones are present in your urine")
        ToolTip(self.ketones_no, "Click if no ketones are present in your urine")

        # Logout button
        self.logout_button=tk.Button(self.root, text="Logout", command=self.logout)
        ToolTip(self.logout_button, "Click to end session")
        self.logout_button.place(x=0,y=0)

    def record_reading_no(self):
        self.take_reading_label.config(text="Please take your reading immediately.")
        self.record_reading
        
    def record_reading(self):

        self.record_results.config(text="Record your results in mg/dL. (Must be 0-999) ")
        self.record_button.pack()
        self.blood_sugar_entry.pack()
        

        reading = int(self.blood_sugar_entry.get())
        low_glucose = self.patient_data["lowGlucose"]
        high_glucose = self.patient_data["highGlucose"]
        docter = self.patient_data['doctorName']
     

        if reading < low_glucose:
                self.handle_low_reading()
                if reading < 50:
                     self.explain_reason()
        elif low_glucose <= reading <= high_glucose:
                self.handle_normal_reading()
        else:
                self.handle_high_reading()
                if reading > 160:
                     self.explain_reason()


    def handle_low_reading(self):
        messagebox.showinfo("Low Reading", "Your reading is low. Eat a sugar source, take your medicine, and follow your doctor's meal plan.")

    def handle_normal_reading(self):
        messagebox.showinfo("Normal Reading", "Your reading is within the normal range.")

    def handle_high_reading(self):
        messagebox.showinfo("High Reading", f"Your blood sugar is high. Call your doctor ({self.patient_data['doctorName']}, Phone: {self.patient_data['doctorNumber']}) immediately.")
        self.ketones.config(text = "Is there a presence of ketones in your urine?")
        self.ketones.pack()
        self.ketones_yes.pack()
        self.ketones_no.pack()
    
    def ketones_msg(self):
        messagebox.showinfo("Ketones Detected", "Ketones are present in your urine. Seek medical attention promptly.")

    def ketones_msg_no(self):
        messagebox.showinfo("No Ketones Detected", "No need to call doctor for ketones")

    def explain_reason(user):
        reason = simpledialog.askstring("Explanation", "Please explain why you feel your reading isn't normal:")
        user.reason = reason

    def show_tooltip(self, text):
        self.tooltip = tk.Toplevel(self.root)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{self.root.winfo_pointerx()}+{self.root.winfo_pointery()}")
        tk.Label(self.tooltip, text=text, background="lightyellow", relief="solid", borderwidth=1).pack()

    def hide_tooltip(self, event):
        if hasattr(self, "tooltip"):
            self.tooltip.destroy()
    def logout(self):
        self.root.destroy()  # Close the blood sugar screen
        
class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        tk.Label(self.tooltip, text=self.text, background="lightyellow", relief="solid", borderwidth=1).pack()

    def hide_tooltip(self, event):
        if hasattr(self, "tooltip"):
            self.tooltip.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BloodSugarScreen(root)  # Pass the actual user name here
    root.mainloop()
