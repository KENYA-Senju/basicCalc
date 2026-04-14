import tkinter as tk 
from math import cos, sin, tan, radians
from math import pi
import re
window = tk.Tk()
window.title("Basic Calculator") 

display_frame = tk.Frame(window)
display_frame.pack(fill = "both", expand = True) 

standard_font = ("Times", 20)


display_variable = tk.StringVar()

Text = tk.Label(display_frame, text = "Calculation Portal", font = standard_font).pack(padx =5, pady = 5)
de = tk.Entry(display_frame, justify = "left", font  = standard_font, textvariable = display_variable)
de.pack(fill = "y", padx = 10, pady = 10) 

rd = tk.StringVar()
rad_degrees = tk.Spinbox(display_frame, values = ["Radians", "Degrees"] , textvariable = rd).pack()

radeg_index = {"Radians": "r", 
               "Degrees": "d"}
#TODO: build the entry involved

button_frame = tk.Frame(window) 
button_frame.pack()

#TODO: create a loop that iterates over the enumerated list 
buttons = [["7", "8", "9", "/"], 
           ["4","5", "6", "*"], 
           ["1", "2", "3", "-"], 
           ["0", ".", "=", "+"]
]

def convert_radians(expression, mode): 
    def repl(match): 
        func = match.group(1) # for sine, cosine, and tangent

        argument = match.group(2)

        val  = eval(argument)

        if mode == "Degrees":value = radians(value)
        return f"{func}({val})"
    

    pattern = r"(sin|cos|tan)\((.*?)\)"
    return re.sub(pattern,repl,expression)
#Evaluate the Expression with KNOWN OPERATIONS
def calculateVal():
    expr = display_variable.get()
    mod = rd.get()

    expr = convert_radians(expr, mod)
    operation = str(eval(expr))
    display_variable.set(operation)



non_operator = ["="] 
def addVal(number): 
    if number in non_operator: 
        calculateVal()
    else:
        display_variable.set(display_variable.get() + number)

#Main Buttons 
for r,row  in enumerate(buttons): 
    for c, column  in enumerate(row): 
        bt = tk.Button(button_frame,  
                    width =4, 
                    height = 2, 
                    font = standard_font, 
                    text= column,
                    command = lambda val = column: addVal(val) )
        bt.grid(row = r, column = c, padx = 5 , pady =5 )

#Cancel Option
CE  = tk.Button(button_frame,  text = "CE", height = 2, width = 4, font = standard_font, command = lambda: display_variable.set(''))
CE.grid(row = 3, column = 4, padx = 5,pady = 5, rowspan = 1)

#Math.Tangent Button
Tan  = tk.Button(button_frame,  text = "tan", height = 2, width = 4, font = standard_font, command = lambda: addVal("tan("))
Tan.grid(row = 2, column = 4, padx = 5,pady = 5, rowspan = 1)


#TODO: Add cos,sin, and tangent buttons, and respective functions Eval 
#SIN
Sine = tk.Button(button_frame,  text = "sin", height = 2, width = 4, font = standard_font, command = lambda: addVal(f"sin("))
Sine.grid(row = 2, column = 5, padx = 5,pady = 5, rowspan = 1)

#COSINE
Cosine  = tk.Button(button_frame,  text = "cos", height = 2, width = 4, font = standard_font, command = lambda: addVal(f"cos("))
Cosine.grid(row = 3, column = 5, padx = 5,pady = 5, rowspan = 1)

#TODO: add sqrt, and percent buttons and respective functions with Eval  (2)


#TODO: add parenthesies to help the  UI control order of operations (1)
pr1  = tk.Button(button_frame,  text = "(", height = 2, width = 4, font = standard_font, command = lambda: addVal("("))
pr1.grid(row = 1, column = 4, padx = 5,pady = 5, rowspan = 1)

pr2 = tk.Button(button_frame,  text = ")", height = 2, width = 4, font = standard_font, command = lambda: addVal(")"))
pr2.grid(row = 1, column = 5, padx = 5,pady = 5, rowspan = 1)

pie = tk.Button(button_frame,  text = "π", height = 2, width = 4, font = standard_font, command = lambda: addVal("pi"))
pie.grid(row = 0, column = 5, padx = 5,pady = 5, rowspan = 1)




delete = tk.Button(button_frame, text = "X" ,
                height = 2, width = 4, font = standard_font, 
                command = lambda: display_variable.set(display_variable.get()[:-1])
                ).grid(row = 0, column = 4, padx = 5,pady = 5, rowspan = 1)


window.bind('<Return>',lambda event: calculateVal())

#create spinbox

window.mainloop()