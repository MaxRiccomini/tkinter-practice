import tkinter as tk

root = tk.Tk()

# Create a label widget and place it in row 0, column 0
label1 = tk.Label(root, text="Label 1")
label1.grid(row=0, column=0, sticky="nsew")

# Create a button widget and place it in row 1, column 0
button1 = tk.Button(root, text="Button 1")
button1.grid(row=1, column=0, sticky="nsew")

# Create another label widget and place it in row 0, column 1
label2 = tk.Label(root, text="Label 2")
label2.grid(row=0, column=1, sticky="nsew")

# Create another button widget and place it in row 1, column 1
button2 = tk.Button(root, text="Button 2")
button2.grid(row=1, column=1, sticky="nsew")

root.mainloop()
