from tkinter import *

window = Tk()
window.title("Mile to KM Convertor")
window.configure(padx=20, pady=20, bg="white")

entry = Entry(width=10)
entry.config(bg="white", fg="black")
entry.insert(END, string="0")
entry.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.config(bg="white", fg="black")
mile_label.grid(column=2, row=0)

equal_label = Label(text="is Equal to")
equal_label.config(bg="white", fg="black")
equal_label.grid(column=0, row=1)

km_out = Label(text="0.0")
km_out.config(bg="white", fg="black")
km_out.grid(column=1, row=1)

km_label = Label(text="KM")
km_label.config(bg="white", fg="black")
km_label.grid(column=2, row=1)


def calculate():
    miles = int(entry.get())
    km = miles * 1.60934
    km_out.config(text=km)


button = Button(text="Calculate", command=calculate, bg="black")
button.grid(column=1, row=2)

window.mainloop()
