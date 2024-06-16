import time
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import tkinter as tk
from tkinter import messagebox, ttk

def show_verification_popup():
    # Create the main window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Show the message box
    messagebox.showinfo("Confirmación", "¿Confirmado?")

    # Destroy the main window after the user clicks "OK"
    root.destroy()

def DepositoDeCuentas(company_name, registry_option, reference_text, ejercicio, use_captcha_solver):
    chrome_options = webdriver.ChromeOptions()
    if use_captcha_solver:
        chrome_options.add_extension('CAPTCHASolver.crx')

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get("https://sede.registradores.org/sede/sede-corpme-web/home")
    driver.set_window_size(950, 1000)
    time.sleep(5)

    try:
        accept_button = driver.find_element(By.CSS_SELECTOR, ".cm-btn-success")
        webdriver.ActionChains(driver).move_to_element(accept_button).perform()
        accept_button.click()

        user_access_button = driver.find_element(By.CSS_SELECTOR, '.topbar__user-text')
        user_access_button.click()
    
        login_button = driver.find_element(By.CSS_SELECTOR, '.login-card-container:nth-child(3) .btn-primary')
        login_button.click()    

        driver.find_element(By.ID, "input_1").click()
        driver.find_element(By.ID, "input_1").send_keys("Tracedat")
        driver.find_element(By.ID, "input_2").click()
        driver.find_element(By.ID, "input_2").send_keys("Trace7785+@6")
        driver.find_element(By.CSS_SELECTOR, ".credentials_input_submit").click()
        time.sleep(5)
        
        driver.find_element(By.LINK_TEXT, "Solicitar nota informativa mercantil").click()

        element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".mb-8 .rb-option:nth-child(2) > .rb-label")))
        element.click()

        driver.find_element(By.ID, "closeCookiesInfo").click()

        search_box = driver.find_element(By.ID, "terminoBusquedaMerc")
        search_box.clear()
        search_box.send_keys(company_name)

        select_registro = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "selectRegistro")))
        select_registro.click()

        dropdown_denomination = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "selectRegistro")))
        dropdown_denomination.send_keys(registry_option)
        
        show_verification_popup()

        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit")))
        submit_button.click()
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, ".form-action > .btn").click()
        driver.find_element(By.CSS_SELECTOR, '.rb-group:nth-child(9) > fieldset > .rb-option .rb-text > span').click()
        driver.find_element(By.CSS_SELECTOR, '.submit').click()

        driver.find_element(By.ID, 'selectEjercicio').click()
        Select(driver.find_element(By.ID, 'selectEjercicio')).select_by_visible_text(ejercicio)
        driver.find_element(By.CSS_SELECTOR, '.submit').click()

        driver.find_element(By.CSS_SELECTOR, '.cb-label:nth-child(1) > .cb-text').click()

        driver.find_element(By.ID, 'informationTypeRef').click()
        driver.find_element(By.ID, 'informationTypeRef').send_keys(reference_text)

        show_verification_popup()
        time.sleep(1)

    except TimeoutException as e:
        print(f"Error: {e}")

    finally:
        driver.close()

def NotaInformativaMercantil(company_name, registry_option, reference_text, use_captcha_solver):
    chrome_options = webdriver.ChromeOptions()
    if use_captcha_solver:
        chrome_options.add_extension('CAPTCHASolver.crx')

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get("https://sede.registradores.org/sede/sede-corpme-web/home")
    driver.set_window_size(950, 1000)
    time.sleep(5)

    try:
        accept_button = driver.find_element(By.CSS_SELECTOR, ".cm-btn-success")
        webdriver.ActionChains(driver).move_to_element(accept_button).perform()
        accept_button.click()

        user_access_button = driver.find_element(By.CSS_SELECTOR, '.topbar__user-text')
        user_access_button.click()
    
        login_button = driver.find_element(By.CSS_SELECTOR, '.login-card-container:nth-child(3) .btn-primary')
        login_button.click()    

        driver.find_element(By.ID, "input_1").click()
        driver.find_element(By.ID, "input_1").send_keys("Tracedat")
        driver.find_element(By.ID, "input_2").click()
        driver.find_element(By.ID, "input_2").send_keys("Trace7785+@6")
        driver.find_element(By.CSS_SELECTOR, ".credentials_input_submit").click()
        time.sleep(5)
        
        driver.find_element(By.LINK_TEXT, "Solicitar nota informativa mercantil").click()

        element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".mb-8 .rb-option:nth-child(2) > .rb-label")))
        element.click()

        driver.find_element(By.ID, "closeCookiesInfo").click()

        search_box = driver.find_element(By.ID, "terminoBusquedaMerc")
        search_box.clear()
        search_box.send_keys(company_name)

        select_registro = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "selectRegistro")))
        select_registro.click()

        dropdown_denomination = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "selectRegistro")))
        dropdown_denomination.send_keys(registry_option)
        
        show_verification_popup()

        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit")))
        submit_button.click()
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, ".form-action > .btn").click()
        driver.find_element(By.CSS_SELECTOR, ".submit").click()
        driver.find_element(By.CSS_SELECTOR, ".panel .cb-pick").click()
        driver.find_element(By.CSS_SELECTOR, ".add-ref .cb-pick").click()

        reference_input = driver.find_element(By.ID, "informationTypeRef")
        reference_input.clear()
        reference_input.send_keys(reference_text)

        driver.find_element(By.CSS_SELECTOR, ".form-action .submit").click()
        show_verification_popup()
        time.sleep(1)

    except TimeoutException as e:
        print(f"Error: {e}")

    finally:
        driver.close()

def submit_request_nota(company_name, reference_text, registry_option, use_captcha_solver):
    NotaInformativaMercantil(company_name, registry_option, reference_text, use_captcha_solver)

def submit_request_deposito(company_name, reference_text, registry_option, ejercicio, use_captcha_solver):
    DepositoDeCuentas(company_name, registry_option, reference_text, ejercicio, use_captcha_solver)

def black_button_action(frame):
    frame.tkraise()

def create_gui():
    root = tk.Tk()
    root.title("Automated Web Interaction")

    def show_frame(frame):
        frame.tkraise()

    registros = ["Seleccione el Registro", "A CORUÑA", "ALACANT/ALICANTE", "ALBACETE", "ALMERIA",  
                 "ARABA/ALAVA", "ARRECIFE", "ASTURIAS", "AVILA", "BADAJOZ", "BARCELONA", "BIZKAIA", "BURGOS", 
                 "CACERES", "CADIZ", "CASTELLO/CASTELLON", "CEUTA", "CIUDAD REAL", "CORDOBA", 
                 "CUENCA", "EIVISSA", "GIPUZKOA", "GIRONA", "GRANADA", "GUADALAJARA", "HUELVA", 
                 "HUESCA", "JAEN", "LA RIOJA", "LAS PALMAS DE GRAN CANARIA", "LEON", "LLEIDA", 
                 "LUGO", "MADRID", "MALAGA", "MAO", "MELILLA", "MURCIA", "NAVARRA", "OURENSE", 
                 "PALENCIA", "PALMA DE MALLORCA", "PONTEVEDRA", "PUERTO DEL ROSARIO", "SALAMANCA", 
                 "SAN SEBASTIAN DE LA GOMERA", "SANTA CRUZ DE LA PALMA", "SANTA CRUZ DE TENERIFE", 
                 "SANTANDER", "SANTIAGO DE COMPOSTELA", "SEGOVIA", "SEVILLA", "SORIA", "TARRAGONA", 
                 "TERUEL", "TOLEDO", "VALENCIA", "VALLADOLID", "ZAMORA", "ZARAGOZA"]

    # Frame for Nota Informativa Mercantil
    frame_nota = ttk.Frame(root)
    frame_nota.grid(row=0, column=0, sticky='nsew')

    label_company_nota = ttk.Label(frame_nota, text="Company Name:")
    label_company_nota.grid(row=0, column=0, padx=10, pady=10)
    entry_company_nota = ttk.Entry(frame_nota)
    entry_company_nota.grid(row=0, column=1, padx=10, pady=10)

    label_reference_nota = ttk.Label(frame_nota, text="Reference Text:")
    label_reference_nota.grid(row=1, column=0, padx=10, pady=10)
    entry_reference_nota = ttk.Entry(frame_nota)
    entry_reference_nota.grid(row=1, column=1, padx=10, pady=10)

    label_registry_nota = ttk.Label(frame_nota, text="Registry Option:")
    label_registry_nota.grid(row=2, column=0, padx=10, pady=10)
    combo_registry_nota = ttk.Combobox(frame_nota, values=registros)
    combo_registry_nota.grid(row=2, column=1, padx=10, pady=10)
    combo_registry_nota.set("Seleccione el Registro")

    checkbutton_captcha_nota_var = tk.BooleanVar()
    checkbutton_captcha_nota = ttk.Checkbutton(frame_nota, text="Use CAPTCHA Solver", variable=checkbutton_captcha_nota_var)
    checkbutton_captcha_nota.grid(row=3, columnspan=2, pady=10)

    button_submit_nota = ttk.Button(frame_nota, text="Submit", command=lambda: submit_request_nota(
        entry_company_nota.get(),
        entry_reference_nota.get(),
        combo_registry_nota.get(),
        checkbutton_captcha_nota_var.get()
    ))
    button_submit_nota.grid(row=4, columnspan=2, pady=10)

    button_back_nota = ttk.Button(frame_nota, text="Back", command=lambda: show_frame(frame_main))
    button_back_nota.grid(row=5, columnspan=2, pady=10)

    # Frame for Deposito de Cuentas
    frame_deposito = ttk.Frame(root)
    frame_deposito.grid(row=0, column=0, sticky='nsew')

    label_company_deposito = ttk.Label(frame_deposito, text="Company Name:")
    label_company_deposito.grid(row=0, column=0, padx=10, pady=10)
    entry_company_deposito = ttk.Entry(frame_deposito)
    entry_company_deposito.grid(row=0, column=1, padx=10, pady=10)

    label_reference_deposito = ttk.Label(frame_deposito, text="Reference Text:")
    label_reference_deposito.grid(row=1, column=0, padx=10, pady=10)
    entry_reference_deposito = ttk.Entry(frame_deposito)
    entry_reference_deposito.grid(row=1, column=1, padx=10, pady=10)

    label_registry_deposito = ttk.Label(frame_deposito, text="Registry Option:")
    label_registry_deposito.grid(row=2, column=0, padx=10, pady=10)
    combo_registry_deposito = ttk.Combobox(frame_deposito, values=registros)
    combo_registry_deposito.grid(row=2, column=1, padx=10, pady=10)
    combo_registry_deposito.set("Seleccione el Registro")

    label_ejercicio = ttk.Label(frame_deposito, text="Ejercicio:")
    label_ejercicio.grid(row=3, column=0, padx=10, pady=10)
    entry_ejercicio = ttk.Entry(frame_deposito)
    entry_ejercicio.grid(row=3, column=1, padx=10, pady=10)

    checkbutton_captcha_deposito_var = tk.BooleanVar()
    checkbutton_captcha_deposito = ttk.Checkbutton(frame_deposito, text="Use CAPTCHA Solver", variable=checkbutton_captcha_deposito_var)
    checkbutton_captcha_deposito.grid(row=4, columnspan=2, pady=10)

    button_submit_deposito = ttk.Button(frame_deposito, text="Submit", command=lambda: submit_request_deposito(
        entry_company_deposito.get(),
        entry_reference_deposito.get(),
        combo_registry_deposito.get(),
        entry_ejercicio.get(),
        checkbutton_captcha_deposito_var.get()
    ))
    button_submit_deposito.grid(row=5, columnspan=2, pady=10)

    button_back_deposito = ttk.Button(frame_deposito, text="Back", command=lambda: show_frame(frame_main))
    button_back_deposito.grid(row=6, columnspan=2, pady=10)

    # Main frame
    frame_main = ttk.Frame(root)
    frame_main.grid(row=0, column=0, sticky='nsew')

    button_nota = ttk.Button(frame_main, text="Nota Informativa Mercantil", command=lambda: show_frame(frame_nota))
    button_nota.grid(row=0, columnspan=2, pady=10)

    button_deposito = ttk.Button(frame_main, text="Deposito de Cuentas", command=lambda: show_frame(frame_deposito))
    button_deposito.grid(row=1, columnspan=2, pady=10)

    show_frame(frame_main)
    root.mainloop()

create_gui()
