from tkinter import *

window = Tk()


def kg_to_grams_pounds_ounces():
    inputValue = float(e1_value.get())
    grams = inputValue * 1000
    pounds = inputValue * 2.20462
    ounces = inputValue * 35.274

    tx_grams.insert(END, grams)
    tx_pounds.insert(END, pounds)
    tx_ounces.insert(END, ounces)


b1 = Button(window, text="convert", command=kg_to_grams_pounds_ounces)
b1.grid(row=0, column=2)


label1 = Label(window, text="Kg")
label1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

tx_grams = Text(window, height=1, width=20)
tx_grams.grid(row=1, column=0)

tx_pounds = Text(window, height=1, width=20)
tx_pounds.grid(row=1, column=1)


tx_ounces = Text(window, height=1, width=20)
tx_ounces.grid(row=1, column=2)

# always at the end of the code
window.mainloop()
