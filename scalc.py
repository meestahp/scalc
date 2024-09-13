from tkinter import *
scalc = Tk()
scalc.title("Calculator")
scalc.rowconfigure(0, weight=2)
scalc.rowconfigure(1, weight=3)
scalc.columnconfigure(0, weight=1)


def btn_click(item):
    global expression
    expression = expression + str(item)
    lcd_val.set(expression)


def btn_clear():
    global expression
    expression = ""
    lcd_val.set("")


def btn_equal():
    global expression
    try:
        result = str(eval(expression))  # Evaluate expression
    except:
        result = "E"

    lcd_val.set(result)
    expression = result  # ""


expression = ""

lcd_val = StringVar()
# Input Field Frame
lcd_frame = Frame(scalc, bd=10, highlightbackground="black",
                  highlightcolor="black", highlightthickness=10)
lcd_frame.grid(row=0, column=0, sticky="NSEW")
lcd_frame.columnconfigure(0, weight=1)
lcd_frame.rowconfigure(0, weight=1)
input_field = Entry(lcd_frame, font=('Arial', 54, 'bold'),
                    textvariable=lcd_val, bg="#dfd", bd=16, justify=RIGHT)
input_field.grid(row=0, column=0, sticky="NSEW")

# Frame for the buttons to go
btns_frame = Frame(scalc, bg="red")
btns_frame.grid(row=1, column=0, sticky="NSEW")

btns_frame.columnconfigure(0, weight=1)
btns_frame.columnconfigure(1, weight=1)
btns_frame.columnconfigure(2, weight=1)
btns_frame.columnconfigure(3, weight=1)
btns_frame.rowconfigure(0, weight=1)
btns_frame.rowconfigure(1, weight=1)
btns_frame.rowconfigure(2, weight=1)
btns_frame.rowconfigure(3, weight=1)
btns_frame.rowconfigure(4, weight=1)
# Row 0
clear = Button(btns_frame, text="C", fg="white", bd=2, bg="#f33", font=(
    'arial', 26, 'bold'), command=lambda: btn_clear()).grid(row=0, column=0, columnspan=3, sticky=NSEW)
divide = Button(btns_frame, text="/", fg="white", bd=2, bg="#444", font=('arial',
                26, 'bold'),  command=lambda: btn_click("/")).grid(row=0, column=3, sticky=NSEW)
# Row 1
seven = Button(btns_frame, text="7", fg="black", bd=2, bg="#ddd", font=(
    'arial', 26, 'bold'),  command=lambda: btn_click(7)).grid(row=1, column=0, sticky=NSEW)
eight = Button(btns_frame, text="8", fg="black", bd=2, bg="#ddd", font=(
    'arial', 26, 'bold'),  command=lambda: btn_click(8)).grid(row=1, column=1, sticky=NSEW)
nine = Button(btns_frame, text="9", fg="black", bd=2, bg="#ddd", font=(
    'arial', 26, 'bold'),  command=lambda: btn_click(9)).grid(row=1, column=2, sticky=NSEW)
multiply = Button(btns_frame, text="*", fg="white", bd=2, bg="#444", font=('arial',
                  26, 'bold'),  command=lambda: btn_click("*")).grid(row=1, column=3, sticky=NSEW)
# Row 2
four = Button(btns_frame, text="4", fg="black", bd=2, bg="#ddd", font=(
    'arial', 26, 'bold'),  command=lambda: btn_click(4)).grid(row=2, column=0, sticky=NSEW)
five = Button(btns_frame, text="5", fg="black", bd=2, bg="#ddd", font=(
    'arial', 26, 'bold'),  command=lambda: btn_click(5)).grid(row=2, column=1, sticky=NSEW)
six = Button(btns_frame, text="6", fg="black", bd=2, bg="#ddd", font=(
    'arial', 26, 'bold'),  command=lambda: btn_click(6)).grid(row=2, column=2, sticky=NSEW)
minus = Button(btns_frame, text="-", fg="white", bd=2, bg="#444", font=('arial',
               26, 'bold'),  command=lambda: btn_click("-")).grid(row=2, column=3, sticky=NSEW)
# Row 3
one = Button(btns_frame, text="1", fg="black", bd=2, bg="#ddd", font=(
    'arial', 26, 'bold'),  command=lambda: btn_click(1)).grid(row=3, column=0, sticky=NSEW)
two = Button(btns_frame, text="2", fg="black", bd=2, bg="#ddd", font=(
    'arial', 26, 'bold'),  command=lambda: btn_click(2)).grid(row=3, column=1, sticky=NSEW)
three = Button(btns_frame, text="3", fg="black", bd=2, bg="#ddd", font=(
    'arial', 26, 'bold'),  command=lambda: btn_click(3)).grid(row=3, column=2, sticky=NSEW)
plus = Button(btns_frame, text="+", fg="white", bd=2, bg="#444", font=('arial',
              26, 'bold'),  command=lambda: btn_click("+")).grid(row=3, column=3, sticky=NSEW)
# Row 4
zero = Button(btns_frame, text="0", fg="black", bd=2, bg="#ddd", font=('arial', 26, 'bold'),
              command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, sticky=NSEW)
point = Button(btns_frame, text=".", fg="white", bd=2, bg="#444", font=(
    'arial', 26, 'bold'),  command=lambda: btn_click(".")).grid(row=4, column=2, sticky=NSEW)
equals = Button(btns_frame, text="=", fg="white", bd=2, bg="#444", font=(
    'arial', 26, 'bold'),  command=lambda: btn_equal()).grid(row=4, column=3, sticky=NSEW)

scalc.mainloop()
