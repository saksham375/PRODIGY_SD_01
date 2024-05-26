import tkinter as tk

def convert_temperature():
    value = float(entry_value.get())
    unit = entry_unit.get()

    if unit.lower() == "c" or unit.lower() == "celsius":
        fahrenheit = (value * 9/5) + 32
        kelvin = value + 273.15
        label_result.config(text=f"Fahrenheit: {fahrenheit:.2f}\nKelvin: {kelvin:.2f}")

    elif unit.lower() == "f" or unit.lower() == "fahrenheit":
        celsius = (value - 32) * 5/9
        kelvin = celsius + 273.15
        label_result.config(text=f"Celsius: {celsius:.2f}\nKelvin: {kelvin:.2f}")

    elif unit.lower() == "k" or unit.lower() == "kelvin":
        celsius = value - 273.15
        fahrenheit = (celsius * 9/5) + 32
        label_result.config(text=f"Celsius: {celsius:.2f}\nFahrenheit: {fahrenheit:.2f}")

    else:
        label_result.config(text="Invalid unit")

root = tk.Tk()
root.title("Temperature Converter")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label_value = tk.Label(frame, text="Enter temperature value:")
label_value.grid(row=0, column=0)

entry_value = tk.Entry(frame, width=10)
entry_value.grid(row=0, column=1)

label_unit = tk.Label(frame, text="Enter unit (C/F/K):")
label_unit.grid(row=1, column=0)

entry_unit = tk.Entry(frame, width=10)
entry_unit.grid(row=1, column=1)

button_convert = tk.Button(frame, text="Convert", command=convert_temperature)
button_convert.grid(row=2, column=0, columnspan=2)

label_result = tk.Label(frame, text="")
label_result.grid(row=3, column=0, columnspan=2)

root.mainloop()