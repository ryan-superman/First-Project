import tkinter as tk
from tkinter import font

HEIGHT = 500
WIDTH = 600

root = tk.Tk()
root.title("Speedups Calculator")
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()


def calculate():
    one_min     = int(e1.get())
    five_min    = (int(e2.get())) * 5
    ten_min     = (int(e3.get())) * 10 
    fifteen     = (int(e4.get())) * 15
    thirty      = (int(e5.get())) * 30
    sixty       = (int(e6.get())) * 60
    three_hr    = (int(e7.get())) * 3
    eight_hr    = (int(e8.get())) * 8
    fifteen_hr  = (int(e9.get())) * 15
    one_day     = int(e10.get())
    three_day   = (int(e11.get())) * 3

    days = ((one_min/60)/24) + ((five_min/60)/24) + ((ten_min/60)/24) + ((fifteen/60)/24) + ((thirty/60)/24) + ((sixty/60)/24) + (three_hr/24) + (eight_hr/24) + (fifteen_hr/24) + (one_day) + (three_day)
    result_label['text'] = format(days, '.2f'), "days"

    
##Background Image##
background_image = tk.PhotoImage(file="rok.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

##Parent##
frame = tk.Frame(root, bg ="#ccd9ff", bd=5)
frame.place(relx= 0.3, rely = 0.2, relwidth = 0.5, relheight = 0.7, anchor="n")


##Label##
#1min
label = tk.Label(frame, text = "1 Minute  = ", bg ="#ccd9ff", font=('Courier', 14))
label.grid(row=0)
#5min
label = tk.Label(frame, text = "5 Minute  = ", bg ="#ccd9ff", font=('Courier', 14))
label.grid(row=1)
#10min
label = tk.Label(frame, text = "10 Minute = ", bg ="#ccd9ff", font=('Courier', 14))
label.grid(row=2)
#15min
label = tk.Label(frame, text = "15 Minute = ", bg ="#ccd9ff", font=('Courier', 14))
label.grid(row=3)
#30min
label = tk.Label(frame, text = "30 Minute = ", bg ="#ccd9ff", font=('Courier', 14))
label.grid(row=4)
#60min
label = tk.Label(frame, text = "60 Minute = ", bg ="#ccd9ff", font=('Courier', 14))
label.grid(row=5)
#3hr
label = tk.Label(frame, text = "3 Hours   = ", bg ="#ccd9ff", font=('Courier', 14))
label.grid(row=6)
#8hr
label = tk.Label(frame, text = "8 Hours   = ", bg ="#ccd9ff", font=('Courier', 14))
label.grid(row=7)
#15hr
label = tk.Label(frame, text = "15 Hours  = ", bg ="#ccd9ff", font=('Courier', 14))
label.grid(row=8)
#24hr
label = tk.Label(frame, text = "24 Hours  = ", bg ="#ccd9ff", font=('Courier', 14))
label.grid(row=9)
#3days
label = tk.Label(frame, text = "3 Days    = ", bg ="#ccd9ff", font=('Courier', 14))
label.grid(row=10)

##Input##
e1 = tk.Entry(frame, font=('Courier', 14),width = 10)
e2 = tk.Entry(frame, font=('Courier', 14),width = 10)
e3 = tk.Entry(frame, font=('Courier', 14),width = 10)
e4 = tk.Entry(frame, font=('Courier', 14),width = 10)
e5 = tk.Entry(frame, font=('Courier', 14),width = 10)
e6 = tk.Entry(frame, font=('Courier', 14),width = 10)
e7 = tk.Entry(frame, font=('Courier', 14),width = 10)
e8 = tk.Entry(frame, font=('Courier', 14),width = 10)
e9 = tk.Entry(frame, font=('Courier', 14),width = 10)
e10 = tk.Entry(frame, font=('Courier', 14),width = 10)
e11 = tk.Entry(frame, font=('Courier', 14),width = 10)

##Default Value##
e1.insert(0, "0")
e2.insert(0, "0")
e3.insert(0, "0")
e4.insert(0, "0")
e5.insert(0, "0")
e6.insert(0, "0")
e7.insert(0, "0")
e8.insert(0, "0")
e9.insert(0, "0")
e10.insert(0, "0")
e11.insert(0, "0")


##Placement##
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
e4.grid(row=3,column=1)
e5.grid(row=4,column=1)
e6.grid(row=5,column=1)
e7.grid(row=6,column=1)
e8.grid(row=7,column=1)
e9.grid(row=8,column=1)
e10.grid(row=9,column=1)
e11.grid(row=10,column=1)



##Results##
#Button
button = tk.Button(frame, text = "Calculate", font=('Courier', 11), command=calculate)
button.grid(row = 11)
#Label Text
result_label = tk.Label(frame, font=('Courier', 9), width = 15, justify='left',anchor='nw', bd=4 )
result_label.grid(row = 11, column = 1)

#Credit
creds = tk.Frame(root, bg ="#ffb3b3", bd=5)
creds.place(relx= 0.95, rely = 0.95, relwidth = 0.2, relheight = 0.05, anchor="se")
label = tk.Label(creds, text = "By Ryan S.",bg ="#ffb3b3", font=('Courier', 10), fg='white')
label.pack()


root.mainloop()
