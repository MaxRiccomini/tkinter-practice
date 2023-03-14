import tkinter as tk
from tkinter import *

background = "#F5F8FA"

root = tk.Tk()
root.title("Budget Tracker")
root.geometry("1000x400")
root.config(background='#E0E0E0')


def calculateMonthlyNet():
    hrPay = int(main_entry.get())
    weeklyHours = int(main_entry1.get())
    gross = hrPay * weeklyHours
    print(gross)
    main_label["text"] = f"Monthly Gross Income: {gross}"

# Custom Buttons Class

class CustomButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        # initialization of button using color theme-based configs
        self.config(bg="#003366", fg='#003366', font=("Arial", 14))


class CustomEntry(tk.Entry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        # initialization of entry using color theme-based configs
        self.config(bg="#E0E0E0")

class CustomLabel(tk.Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        # initialization of entry using color theme-based configs
        self.config(bg="#003366", fg='#003366', font=("Arial", 14))


main_entry = CustomEntry(root, )
main_entry.place(x=10, y=10)

main_entry1 = CustomEntry(root, )
main_entry1.place(x=10, y=45)

main_button = CustomButton(root, text="Calculate Gross Monthly Income", command=calculateMonthlyNet)
main_button.place(x=750, y=30)

main_label = CustomLabel(root)
main_label.place(x=10, y=80)

root.mainloop()
