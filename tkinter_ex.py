import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("My First GUI")

# widget tk.Label
label = tk.Label(root, text="Hello World", font=('Ariel', 18))
label.pack(padx= 20, pady= 20)

# textbox
# height == lines
textbox = tk.Text(root, height=3, font=('Ariel', 16))
textbox.pack(padx=10, pady=10)

# one line entry (will probably use for project)
# myentry = tk.Entry(root)
# myentry.pack()

# BUTTON
button = tk.Button(root, text="Click Me!", font=('Arial', 18))
button.pack(padx=10, pady=10)

root.mainloop()