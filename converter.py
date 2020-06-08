from tkinter import *
from tkinter.ttk import *
import webbrowser
from functools import partial





def open_link(link):
    webbrowser.open(link, new=2)


def convert(units, value_box, first_measure_box, second_measure_box, output):
    try:
        value = float(value_box.get())
    except ValueError:
        output.set("Неправильный ввод")
        return
    first_measure = units[first_measure_box.get()]
    second_measure = units[second_measure_box.get()]
    result = value * first_measure / second_measure
    output.set(result)


def create_converter(master, units, title):
    units_names = list(units.keys())
    label = Label(master, text=title, font=("Courier", 36))
    label.pack(pady=(20, 0))

    converter = Frame(master)

    left_field = Entry(converter, width=30)
    left_field.grid(column=0, row=0)
    
    left_unit_box = Combobox(converter, width=30,
            values=units_names, state='readonly')
    left_unit_box.set(units_names[1])
    left_unit_box.grid(column=0, row=1)

    output = StringVar()
    right_field = Entry(converter, state='readonly', width=30,
            textvariable=output)
    right_field.grid(column=2, row=0)
    
    right_unit_box = Combobox(converter, width=30,
            values=units_names, state='readonly')
    right_unit_box.set(units_names[0])
    right_unit_box.grid(column=2, row=1) 

    convert_button = Button(converter, text='>', width=1,
            command=partial(convert, units, left_field,
                left_unit_box, right_unit_box, output))
    convert_button.grid(column=1, row=0)

    converter.pack()


def create_info_buttons(master):
    label = Label(master, text="Рецепты", font=("Courier", 36))
    label.pack(pady=(30, 0))
    for i in range(3):
        button = Button(master, width=20, text=button_data[i][0],
                command=partial(open_link, button_data[i][1]))
        button.pack()


app = Tk()
app.title("Конвертеры и рецепты")
app.geometry('600x400+200+100')
create_converter(app, mass_units, "Конвертер масс")
create_converter(app, volume_units, "Конвертер объёмов")
create_info_buttons(app)
app.mainloop()
