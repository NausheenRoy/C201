from tkinter import *
window=Tk()
def calculate_interest():
    p = float(principle.get())
    r = float(rate.get())
    t = float(time.get())
    i =(p*r*t)/100
    interest = round(i, 2)
    outputmessage=Label(result_frame,text= ' Your interest is'+str(i), bg = "lightcyan", font=("Calibri", 12), width=33)
    outputmessage.place(x=20,y=20)
    outputmessage.pack()


window.title('Simple interest Calculator')
window.geometry("580x400")
window.configure(bg='lightcyan')


app_label=Label(window, text="Interest CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

principle_label=Label(window, text="Principle Amount", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
principle_label.place(x=20, y=90)

principle=Entry(window, text="", bd=2, width=22)
principle.place(x=150, y=92)

rate_label=Label(window, text="Rate", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
rate_label.place(x=20, y=120)
rate=Entry(window, text="", bd=2, width=22)
rate.place(x=150, y=120)

time_label=Label(window, text=" time", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
time_label.place(x=20, y=150)
time=Entry(window, text="", bd=2, width=22)
time.place(x=150, y=150)

result_button = Button(window, text='Calculate', fg = "black", bg = "cyan", font=("Calibri", 15),bd=4, command=calculate_interest)
result_button.place(x=20, y=250)




result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=50)
result_label.place(x=20,y=20)
result_label.pack()
window.mainloop()