import tkinter as tk
from tkinter import messagebox

def calcular_temps():
    if tbCelcius.get() or tbFahrenheit.get() or tbKelvin.get():
        try:
            if tbCelcius.get():
                celsius_val = float(tbCelcius.get())
                fahrenheit_val = (celsius_val * 9/5) + 32
                kelvin_val = celsius_val + 273.15
                tbFahrenheit.delete(0, tk.END)
                tbFahrenheit.insert(0, str(round(fahrenheit_val, 2)))
                tbKelvin.delete(0, tk.END)
                tbKelvin.insert(0, str(round(kelvin_val, 2)))
            elif tbFahrenheit.get():
                fahrenheit_val = float(tbFahrenheit.get())
                celsius_val = (fahrenheit_val - 32) * 5/9
                kelvin_val = celsius_val + 273.15
                tbCelcius.delete(0, tk.END)
                tbCelcius.insert(0, str(round(celsius_val, 2)))
                tbKelvin.delete(0, tk.END)
                tbKelvin.insert(0, str(round(kelvin_val, 2)))
            elif tbKelvin.get():
                kelvin_val = float(tbKelvin.get())
                celsius_val = kelvin_val - 273.15
                fahrenheit_val = (celsius_val * 9/5) + 32
                tbCelcius.delete(0, tk.END)
                tbCelcius.insert(0, str(round(celsius_val, 2)))
                tbFahrenheit.delete(0, tk.END)
                tbFahrenheit.insert(0, str(round(fahrenheit_val, 2)))
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores validos para el calculo.")
    else:
        messagebox.showwarning("Advertencia", "Ingrese valores para el calculo de temperatura.")

def limpiar():
    tbCelcius.delete(0, tk.END)
    tbFahrenheit.delete(0, tk.END)
    tbKelvin.delete(0, tk.END)
    messagebox.showinfo("Limpiar", "Se borraron los valores de los campos")



# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Conversor basico de temperatura")

# Etiquetas
#tk.Label(ventana, text="Celsius:").grid(row=0, column=0, padx=10, pady=10)
lbCelcius = tk.Label(ventana, text="Celsius :")
lbCelcius.grid(row = 0, column = 0, padx = 10, pady = 10 )
#tk.Label(ventana, text="Fahrenheit:").grid(row=1, column=0, padx=10, pady=10)
lbFahrenheit = tk.Label(ventana, text="Fahrenheit :")
lbFahrenheit.grid(row = 1, column = 0, padx = 10, pady = 10 )
#tk.Label(ventana, text="Kelvin:").grid(row=2, column=0, padx=10, pady=10)
lbKelvin = tk.Label(ventana, text = "Kelvin : ")
lbKelvin.grid(row = 2, column = 0, padx = 10, pady = 10 )

# row es fila column columna y padx pady son las coordenadas que tendra respecto a ejes X,Y
# Entradas
tbCelcius = tk.Entry(ventana)
tbFahrenheit = tk.Entry(ventana)
tbKelvin = tk.Entry(ventana)

tbCelcius.grid(row=0, column=1, padx=10, pady=10)
tbFahrenheit.grid(row=1, column=1, padx=10, pady=10)
tbKelvin.grid(row=2, column=1, padx=10, pady=10)

# command es una propiedad de Button que llama a una funcion declarada previamente
# Botones
btnCalcular = tk.Button(ventana, text="Calcular", command=calcular_temps)
btnLimpiar = tk.Button(ventana, text="Limpiar", command=limpiar)

btnCalcular.grid(row = 3, column = 0, padx = 10, columnspan = 2, pady = 10)
btnLimpiar.grid(row = 4, column = 0, padx = 10, columnspan = 2, pady = 10)

#btn_calcular.grid(row=3, column=0, columnspan=2, pady=10)
#btn_limpiar.grid(row=4, column=0, columnspan=2, pady=10)

ventana.mainloop()
