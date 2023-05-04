from tkinter import *

root = Tk()

root.title("BMI Calculator")
root.geometry("750x750")

titleLabel = Label(text = "BMI Calculator", font = ("Arial Narrow", 60))
titleLabel.grid(row = 0, column= 1, sticky="W")

def calculateBmi ():
    bmi = round(float(givenWeight.get())/(float(givenHeight.get())**2),2)
    bmiLabel = Label(text=f"BMI: {bmi}", font=("Arial Narrow", 40), width=15)
    bmiLabel.grid(row=4,column=1,sticky = "W", columnspan=2)
    if(bmi<18):
        underweightLabel = Label(text="You are underweight.", font=("Arial Narrow", 40), bg="red", width = 20)
        underweightLabel.grid(row=5,column=1, sticky = "W", columnspan=2)
    elif(bmi>25):
        overweightLabel = Label(text="You are overweight.", font=("Arial Narrow", 40), bg="red", width = 20)
        overweightLabel.grid(row=5,column=1, sticky = "W", columnspan=2)
    else:
        healthlyLabel = Label(text="You are healthly.", font=("Arial Narrow", 40), bg = "green", width = 20)
        healthlyLabel.grid(row=5,column=1,sticky = "W", columnspan=2)


givenWeight = StringVar() #Structure
givenHeight = StringVar()

weightLabel = Label(text="Enter your weight: ", font = ("Arial Narrow", 40))
weightLabel.grid(row=1, column=1, sticky = "W")

weightEntry = Entry(textvariable = givenWeight, font =("Arial Narrow", 40), bg="orange", fg = "black")
weightEntry.grid(row=1,column=2, sticky = "W")

weightLabel = Label(text="Enter your height: ", font = ("Arial Narrow", 40))
weightLabel.grid(row=2, column=1, sticky = "W")

heightEntry = Entry(textvariable = givenHeight, font =("Arial Narrow", 40),bg="orange", fg = "black")
heightEntry.grid(row=2,column=2, sticky = "W")

bmiButton = Button(text="Find BMI", command = calculateBmi, font =("Arial Narrow",40), fg = "white", bg = "purple")
bmiButton.grid(row=3,column=1, sticky = "W")


root.mainloop()