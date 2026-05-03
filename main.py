import tkinter as tk
from tkinter import *
from tkinter import ttk

class main: 
    def formulario():
        try:
            base = Tk()
            base.geometry("750x450")
            base.title("Gestor de ropa")

            groupbox = LabelFrame(base, text="Datos de la ropa", padx=10, pady=10)
            groupbox.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

            # Aseguramos que las columnas no tengan peso para que no se separen
            groupbox.columnconfigure(0, weight=0)
            groupbox.columnconfigure(1, weight=0)

            # --- CAMPOS DE ENTRADA ---
            
            # ID
            Label(groupbox, text="id", font=("Roboto", 12)).grid(row=0, column=0, sticky="w", padx=5, pady=2)
            textBoxID = Entry(groupbox, state="disabled")
            textBoxID.grid(row=0, column=1, sticky="w", pady=2)

            # Nombre
            Label(groupbox, text="Nombre", font=("Roboto", 12)).grid(row=1, column=0, sticky="w", padx=5, pady=2)
            textBoxRopa = Entry(groupbox)
            textBoxRopa.grid(row=1, column=1, sticky="w", pady=2)

            # Color
            Label(groupbox, text="Color", font=("Roboto", 12)).grid(row=2, column=0, sticky="w", padx=5, pady=2)
            textBoxColor = Entry(groupbox)
            textBoxColor.grid(row=2, column=1, sticky="w", pady=2)

            # Cantidad
            Label(groupbox, text="Cantidad", font=("Roboto", 12)).grid(row=3, column=0, sticky="w", padx=5, pady=2)
            textBoxCantidad = Entry(groupbox)
            textBoxCantidad.grid(row=3, column=1, sticky="w", pady=2)

            # Talle
            Label(groupbox, text="Talle", font=("Roboto", 12)).grid(row=4, column=0, sticky="w", padx=5, pady=2)
            seleccionTalle = tk.StringVar()
            combo_talle = ttk.Combobox(groupbox, values=["XS", "S", "M", "L", "XL", "T2", "T3", "T6", "UNICO"], 
                                       textvariable=seleccionTalle, state="readonly")
            combo_talle.grid(row=4, column=1, sticky="w", pady=2)
            
            #Botones
            botones_frame=Frame(groupbox)
            botones_frame.grid(row=6,column=0,columnspan=2,pady=10)

            Button(botones_frame,text="Guardar",width=10).grid(row=0,column=0,padx=5)
            Button(botones_frame,text="Modificar",width=10).grid(row=0,column=1,padx=5)
            Button(botones_frame,text="Eliminar",width=10).grid(row=0,column=2,padx=5)  


            # --- TABLA DE STOCK ---
            
            tree = ttk.Treeview(groupbox, columns=("ID", "Nombre", "Color", "Cantidad", "Talle","Modificacion"), show="headings", height=8)
            
            tree.heading("ID", text="ID")
            tree.heading("Nombre", text="Nombre")
            tree.heading("Color", text="Color")
            tree.heading("Cantidad", text="Cantidad")
            tree.heading("Talle", text="Talle")
            tree.heading("Modificacion",text="Modificacion")

            # Configuración de ancho de columnas
            tree.column("ID", width=50, anchor=CENTER)
            tree.column("Nombre", width=250, anchor=W)
            tree.column("Color", width=100, anchor=CENTER)
            tree.column("Cantidad", width=100, anchor=CENTER)
            tree.column("Talle", width=100, anchor=CENTER)
            tree.column("Modificacion",width=100,ancho=CENTER)

            # tree.grid con columnspan=2 para que abarque el ancho de los labels y entries
            tree.grid(row=5, column=0, columnspan=2, padx=5, pady=15, sticky="nsew")

            base.mainloop()

        except Exception as e:
            print(f"Error al cargar la interfaz: {e}")

# Ejecución del programa
if __name__ == "__main__":
    main.formulario()