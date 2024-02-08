from tkinter import *
from math import sqrt
from PyDesmos import Graph


# Credits for reference
# Stackoverflow copied code (src: https://stackoverflow.com/questions/59838116/how-to-input-use-float-through-entry-box-tkinter-python)
# 2 Circle 1 Square on Youtube (src: https://www.youtube.com/watch?v=qOOnBTaHG_Q)
# PyDesmos integration (src: https://pypi.org/project/PyDesmos/)

# --- Calculation function ---
def circle_sq(input_radius):
    # Finding length of square inside 2 identical
    # circles with a given radius of the circle

    a = 5
    b = (-12 * input_radius)
    c = (2 * input_radius) ** 2

    discriminant = (b ** 2) - (4 * a * c)

    # Take -ve ans, correct ans
    sq_length = (-b - sqrt(discriminant)) / (2 * a)

    return sq_length


# Generate output from window input
def calculate():
    # Testing for errors
    try:
        result = circle_sq(input_radius.get())
        desmos(input_radius.get(), result)
    except Exception as ex:
        # If input value is not a number, throws error
        print(ex)
        result = 'error'

    # Outputs square length, else error statement
    output_value.set(result)



# --- Desmos visual proof --- -> GPT-assisted code (structure)
def desmos(input_value, output_value):
    graph = Graph()
    pt_half = output_value / 2

    circ_1 = f'(x - {input_value})^2 + (y - {input_value})^2 = {input_value}^2'
    graph.append(circ_1)

    circ_2 = f'(x + {input_value})^2 + (y - {input_value})^2 = {input_value}^2'
    graph.append(circ_2)

    pt_1 = f'({pt_half}, 0)'
    graph.append(pt_1)

    pt_2 = f'({pt_half}, {output_value})'
    graph.append(pt_2)

    pt_3 = f'(-{pt_half}, 0)'
    graph.append(pt_3)

    pt_4 = f'(-{pt_half}, {output_value})'
    graph.append(pt_4)

    graph.open()
# --- Tkinter code ---

# Initialising window, fixed size setting
window = Tk()
window.title("2 Circle 1 Square")
window.geometry('220x85')
window.resizable(False, False)

# Initialising variable type for input and output
input_radius = DoubleVar()
output_value = DoubleVar()

# Question label asking for input radius
question = Label(window, text="Input radius:")
question.grid(row=0, column=0)

# Output label
output = Label(window, text="Result:")
output.grid(row=1, column=0)

# Text box to input radius value
input_entry = Entry(window, textvariable=input_radius)
input_entry.grid(row=0, column=1)

# Text box to output square length value
show_output = Entry(window, textvariable=output_value)
show_output.grid(row=1, column=1)

# Button to call calculate() function and perform required task
button = Button(window, text="Calculate", command=calculate)
button.grid(row=2, column=1)


# Run window
window.mainloop()
