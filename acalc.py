from tkinter import *
from tkinter import ttk
import math

from numpy import math

#Method to evaluate formula 1
def Calculate_Formula1():
    try:
        n=textBox_n.get(1.0, "end-1c")
        r=textBox_r.get(1.0, "end-1c")
        l=textBox_w.get(1.0, "end-1c")
        thitha=textBox_thitha.get(1.0, "end-1c")
        #Formula for calculation
        cal_value=(math.pi/30)*(float(n)*float(r)
                        *(
                            round(math.sin(math.radians(float(thitha))),2)
                            + (
                                (float(r)*(round(math.sin(math.radians(float(thitha)*2)),2)))/(2*float(l))
                               )
                        )
                   )
        succssText = Label(text=f"Velocity of Slider is: {cal_value}",foreground='green')
        succssText.place(x=15,y=360)
    except Exception as error:
        print(error)
        errorText = Label(text="Error in calculation",foreground='red')
        errorText.place(x=15,y=360)
#Method to evaluate formula 2
def Calculate_Formula2():
    try:
        n=textBox_n.get(1.0, "end-1c")
        r=textBox_r.get(1.0, "end-1c")
        l=textBox_w.get(1.0, "end-1c")
        thitha=textBox_thitha.get(1.0, "end-1c")
        #Formula for calculation
        cal_value=(math.pi*math.pi*float(n)*float(n)*float(r)
                        *(
                            round(math.cos(math.radians(float(thitha))),2)
                            + (
                                ((float(r)*round(math.cos(math.radians(float(thitha)*2)),2)))/float(l)
                               )
                        )
                   )/900
        succssText = Label(text=f"Acceleration ofSlider is: {cal_value}",foreground='green')
        succssText.place(x=15,y=360)
    except Exception as error:
        print(error)
        errorText = Label(text="Error in calculation",foreground='red')
        errorText.place(x=15,y=360)

# formula 3 calculation
def Calculate_Formula3():
    try:
        n=textBox_n.get(1.0, "end-1c")
        r=textBox_r.get(1.0, "end-1c")
        l=textBox_w.get(1.0, "end-1c")
        thitha=textBox_thitha.get(1.0, "end-1c")
        # Formula for calculation
        cal_value = (math.pi / 30) * (float(n) * float(r)
                                      * (
                                              round(math.cos(math.radians

                                                             (float(thitha))), 2)
                                               / (float(l))
                                              )
                                      )

        succssText = Label(text=f"Velocity of Connecting rod is: {cal_value}", foreground='green')
        succssText.place(x=15, y=360)
    except Exception as error:
        print(error)
        errorText = Label(text="Error in calculation", foreground='red')
        errorText.place(x=15, y=360)

#Method for formula 4
def Calculate_Formula4():
    try:
        n=textBox_n.get(1.0, "end-1c")
        r=textBox_r.get(1.0, "end-1c")
        l=textBox_w.get(1.0, "end-1c")
        thitha=textBox_thitha.get(1.0, "end-1c")
        #Formula for calculation
        cal_value=(-(math.pi*math.pi*float(n)*float(n)*float(r)
                        *(
                            round(math.sin(math.radians(float(thitha))),2))
                            /float(l)
                               )

                   )/900
        succssText = Label(text=f"Acceleration of connecting rod is: {cal_value}",foreground='green')
        succssText.place(x=15,y=360)
    except Exception as error:
        print(error)
        errorText = Label(text="Error in calculation",foreground='red')
        errorText.place(x=15,y=360)

#Code to show data on GUI
app = Tk()
app.geometry("600x600")
app.title("Slider Crank Mechnism")
heading = Label(text="This application will be used for calculating several Formula",fg="black",bg="pink",width="500",height="3",font="15")
heading.pack()

#Creating all the labels
variable_n = Label(text="Enter value of n :",font="10")
variable_r = Label(text="Enter value of r :",font="10")
variable_w = Label(text="Enter value of l :",font="10")
variable_thitha = Label(text="Enter value of θ :",font="10")
variable_n.place(x=15,y=80)
variable_r.place(x=15,y=115)
variable_w.place(x=15,y=145)
variable_thitha.place(x=15,y=180)

#Create all the txt boxes
textBox_n=Text(app, height=2, width=10)
textBox_r=Text(app, height=2, width=10)
textBox_w=Text(app, height=2, width=10)
textBox_thitha=Text(app, height=2, width=10)
textBox_n.pack()
textBox_r.pack()
textBox_w.pack()
textBox_thitha.pack()

#take all the variables
variable_n_val = StringVar()
variable_r_val = StringVar()
variable_w_val = StringVar()


#Creating Button for Formula 1
formula_1_button = Button(app,text="Velocity of Slider",command=Calculate_Formula1,width="15",height="2",bg="grey")
formula_1_button.place(x=15,y=290)
formula_2_button = Button(app,text="Acceleration of Slider",command=Calculate_Formula2,width="15",height="2",bg="grey")
formula_2_button.place(x=140,y=290)
formula_3_button = Button(app,text="Velocity of connectig rod",command=Calculate_Formula3,width="20",height="2",bg="grey")
formula_3_button.place(x=265,y=290)
formula_4_button = Button(app,text="Acceleration of connecting rod",command=Calculate_Formula4,width="25",height="2",bg="grey")
formula_4_button.place(x=390,y=290)
mainloop()