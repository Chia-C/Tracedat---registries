import tkinter as tk
from tkinter import ttk
import threading
from NotaInformativaMercantil import NotaInformativaMercantil
from DepositoDeCuentas import DepositoDeCuentas  # Import the DepositoDeCuentas function

def submit_request_nota(company_name, reference_text, registry_option, use_captcha_solver):
    NotaInformativaMercantil(company_name, registry_option, reference_text, use_captcha_solver)

def submit_request_deposito(company_name, reference_text, registry_option, ejercicio, use_captcha_solver):
    DepositoDeCuentas(company_name, registry_option, reference_text, ejercicio, use_captcha_solver)

def black_button_action(frame):
    frame.tkraise()

def create_gui():
    root = tk.Tk()
    root.title("Automated Web Interaction")

    # Function to show the selected frame
    def show_frame(frame):
        frame.tkraise()

    # List of registry options
    registros = ["Seleccione el Registro", "A CORUÑA", "ALACANT/ALICANTE", "ALBACETE", "ALMERIA",  
              "ARABA/ALAVA", "ARRECIFE", "ASTURIAS", "AVILA", "BADAJOZ", "BARCELONA", "BIZKAIA", "BURGOS", 
              "CACERES", "CADIZ", "CASTELLO/CASTELLON", "CEUTA", "CIUDAD REAL", "CORDOBA", 
              "CUENCA", "EIVISSA", "GIPUZKOA", "GIRONA", "GRANADA", "GUADALAJARA", "HUELVA", 
              "HUESCA", "JAEN", "LA RIOJA", "LAS PALMAS DE GRAN CANARIA", "LEON", "LLEIDA", 
              "LUGO", "MADRID", "MALAGA", "MAO", "MELILLA", "MURCIA", "NAVARRA", "OURENSE", 
              "PALENCIA", "PALMA DE MALLORCA", "PONTEVEDRA", "PUERTO DEL ROSARIO", "SALAMANCA", 
              "SAN SEBASTIAN DE LA GOMERA", "SANTA CRUZ DE LA PALMA", "SANTA CRUZ DE TENERIFE", 
              "SANTANDER", "SANTIAGO DE COMPOSTELA", "SEGOVIA", "SEVILLA", "SORIA", "TARRAGONA", 
              "TERUEL", "TOLEDO", "VALENCIA", "VALLADOLID", "VALVERDE", "ZAMORA", "ZARAGOZA"]
    
    # Create frames for each section
    home_frame = ttk.Frame(root)
    nota_frame = ttk.Frame(root)
    deposito_frame = ttk.Frame(root)

    for frame in (home_frame, nota_frame, deposito_frame):
        frame.grid(row=0, column=0, sticky='nsew')

    # Function to center the window
    def center_window(window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        window.geometry(f"{width}x{height}+{x}+{y}")

    # Set window dimensions
    window_width = 460
    window_height = 300

    # Center the window
    center_window(root, window_width, window_height)

    # Home frame contents
    home_label = ttk.Label(home_frame, text="Select an option:")
    home_label.pack(pady=10)

    nota_button = ttk.Button(home_frame, text="Nota informativa mercantil", command=lambda: show_frame(nota_frame))
    nota_button.pack(pady=5)

    deposito_button = ttk.Button(home_frame, text="Depósito de cuentas", command=lambda: show_frame(deposito_frame))
    deposito_button.pack(pady=5)

    # Nota informativa mercantil frame contents
    nota_label = ttk.Label(nota_frame, text="Escriba la denominación social:")
    nota_label.grid(row=0, column=0, padx=10, pady=10)

    nota_entry = ttk.Entry(nota_frame)
    nota_entry.grid(row=0, column=1, padx=10, pady=10)

    referencia_label = ttk.Label(nota_frame, text="Añadir su referencia:")
    referencia_label.grid(row=1, column=0, padx=10, pady=10)

    referencia_entry = ttk.Entry(nota_frame)
    referencia_entry.insert(0, "PEDIDO ")  # Set default value
    referencia_entry.grid(row=1, column=1, padx=10, pady=10)

    registro_label = ttk.Label(nota_frame, text="Afinar la búsqueda por Registro (Opcional):")
    registro_label.grid(row=2, column=0, padx=10, pady=10)

    registro_var = tk.StringVar()
    registro_var.set("Seleccione el Registro")  # Set default value
    registro_dropdown = ttk.Combobox(nota_frame, textvariable=registro_var, values=registros)
    registro_dropdown.grid(row=2, column=1, padx=10, pady=10)

    captcha_var_nota = tk.BooleanVar()
    captcha_checkbutton_nota = ttk.Checkbutton(nota_frame, text="Utilice el solucionador de captcha", variable=captcha_var_nota)
    captcha_checkbutton_nota.grid(row=3, columnspan=2, pady=10)

    def on_submit_nota():
        company_name = nota_entry.get()
        reference_text = referencia_entry.get()
        registry_option = registro_var.get()
        use_captcha_solver = captcha_var_nota.get()
        threading.Thread(target=submit_request_nota, args=(company_name, reference_text, registry_option, use_captcha_solver)).start()

    nota_button = ttk.Button(nota_frame, text="Solicitar", command=on_submit_nota)
    nota_button.grid(row=4, column=0, columnspan=2, pady=10)

    black_button_nota = ttk.Button(nota_frame, text="Back", command=lambda: black_button_action(home_frame))
    black_button_nota.grid(row=5, column=0, columnspan=2, pady=10)

    # Depósito de cuentas frame contents
    deposito_label = ttk.Label(deposito_frame, text="Escriba la denominación social:")
    deposito_label.grid(row=0, column=0, padx=10, pady=10)

    deposito_entry = ttk.Entry(deposito_frame)
    deposito_entry.grid(row=0, column=1, padx=10, pady=10)

    deposito_referencia_label = ttk.Label(deposito_frame, text="Añadir su referencia:")
    deposito_referencia_label.grid(row=1, column=0, padx=10, pady=10)

    deposito_referencia_entry = ttk.Entry(deposito_frame)
    deposito_referencia_entry.insert(0, "PEDIDO ")  # Set default value
    deposito_referencia_entry.grid(row=1, column=1, padx=10, pady=10)

    deposito_registro_label = ttk.Label(deposito_frame, text="Afinar la búsqueda por Registro (Opcional):")
    deposito_registro_label.grid(row=2, column=0, padx=10, pady=10)

    deposito_registro_var = tk.StringVar()
    deposito_registro_var.set("Seleccione el Registro")  # Set default value
    deposito_registro_dropdown = ttk.Combobox(deposito_frame, textvariable=deposito_registro_var, values=registros)
    deposito_registro_dropdown.grid(row=2, column=1, padx=10, pady=10)

    ejercicio_label = ttk.Label(deposito_frame, text="Ejercicio:")
    ejercicio_label.grid(row=3, column=0, padx=10, pady=10)

    ejercicio_entry = ttk.Entry(deposito_frame)
    ejercicio_entry.grid(row=3, column=1, padx=10, pady=10)

    captcha_var_deposito = tk.BooleanVar()
    captcha_checkbutton_deposito = ttk.Checkbutton(deposito_frame, text="Utilice el solucionador de captcha", variable=captcha_var_deposito)
    captcha_checkbutton_deposito.grid(row=4, columnspan=2, pady=10)

    def on_submit_deposito():
        company_name = deposito_entry.get()
        reference_text = deposito_referencia_entry.get()
        registry_option = deposito_registro_var.get()
        ejercicio = ejercicio_entry.get()
        use_captcha_solver = captcha_var_deposito.get()
        threading.Thread(target=submit_request_deposito, args=(company_name, reference_text, registry_option, ejercicio, use_captcha_solver)).start()

    deposito_button = ttk.Button(deposito_frame, text="Solicitar", command=on_submit_deposito)
    deposito_button.grid(row=5, column=0, columnspan=2, pady=10)

    black_button_deposito = ttk.Button(deposito_frame, text="Back", command=lambda: black_button_action(home_frame))
    black_button_deposito.grid(row=6, column=0, columnspan=2, pady=10)

    # Show the initial frame
    show_frame(home_frame)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
