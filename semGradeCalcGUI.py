import tkinter as tk

def getTarget():
    global q1Input
    global q2Input
    global desInput

    return ((float)(desInput.get()) - ((float)(q1Input.get()) * 0.4) - ((float)(q2Input.get()) * 0.4)) / 0.2

def calcFunc():
    global outputContents
    outputContents["text"] = str(getTarget()) 
    if(not clicked):
        global outputLabel
        outputLabel.pack()
        outputContents.pack()

window = tk.Tk()

global clicked
clicked = False

q1Msg = tk.Label(text="Enter Q1 Grade")
global q1Input
q1Input = tk.Entry()
q2Msg = tk.Label(text="Enter Q2 Grade")
global q2Input
q2Input = tk.Entry()
desMsg = tk.Label(text="Enter Your Desired Grade")
global desInput
desInput = tk.Entry()
calculate = tk.Button(text="Calculate", command=calcFunc)
global outputLabel 
outputLabel = tk.Label(text="You need:")
global outputContents
outputContents = tk.Label()


q1Msg.pack()
q1Input.pack()
q2Msg.pack()
q2Input.pack()
desMsg.pack()
desInput.pack()
calculate.pack()

window.mainloop()
