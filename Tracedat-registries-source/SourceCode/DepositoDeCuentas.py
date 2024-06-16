import time
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import tkinter as tk
from tkinter import messagebox

def show_verification_popup():
    # Create the main window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Show the message box
    messagebox.showinfo("Confirmación", "¿Confirmado?")

    # Destroy the main window after the user clicks "OK"
    root.destroy()

def DepositoDeCuentas(company_name, registry_option, reference_text, ejercicio, use_captcha_solver):
    # Chrome plugin path
    chrome_options = webdriver.ChromeOptions()
    if use_captcha_solver:
        chrome_options.add_extension('CAPTCHASolver.crx')

    # Initialize Chrome WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    # Set implicit wait time
    driver.implicitly_wait(10)

    # Open the URL
    driver.get("https://sede.registradores.org/sede/sede-corpme-web/home")

    # Set Window Size
    driver.set_window_size(950, 1000)

    # Add a delay to ensure the plugin loads properly
    time.sleep(5)

    try:
        # Mouse over the "Aceptar" button
        accept_button = driver.find_element(By.CSS_SELECTOR, ".cm-btn-success")
        webdriver.ActionChains(driver).move_to_element(accept_button).perform()

        # Click on the "Aceptar" button
        accept_button.click()

        # Click on the user access button
        user_access_button = driver.find_element(By.CSS_SELECTOR, '.topbar__user-text')
        user_access_button.click()
    
        # Click on the primary button in the login card container
        login_button = driver.find_element(By.CSS_SELECTOR, '.login-card-container:nth-child(3) .btn-primary')
        login_button.click()    

        # Perform login
        driver.find_element(By.ID, "input_1").click()
        driver.find_element(By.ID, "input_1").send_keys("Tracedat")
        driver.find_element(By.ID, "input_2").click()
        driver.find_element(By.ID, "input_2").send_keys("Trace7785+@6")
        driver.find_element(By.CSS_SELECTOR, ".credentials_input_submit").click()
        time.sleep(5)
        
        # Click on "Solicitar nota informativa mercantil" link
        driver.find_element(By.LINK_TEXT, "Solicitar nota informativa mercantil").click()

        # Denomination social
        element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".mb-8 .rb-option:nth-child(2) > .rb-label")))
        element.click()

        # Turn off cookie notifications
        driver.find_element(By.ID, "closeCookiesInfo").click()

        # Enter text into an input field
        search_box = driver.find_element(By.ID, "terminoBusquedaMerc")
        search_box.clear()
        search_box.send_keys(company_name)

        # Select an option from a dropdown
        select_registro = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "selectRegistro")))
        select_registro.click()

        # Select an option from a dropdown (Escriba la denominación social)
        dropdown_denomination = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "selectRegistro")))
        dropdown_denomination.send_keys(registry_option)
        
        # Show verification popup
        show_verification_popup()

        # Click on a submit button
        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit")))
        submit_button.click()
        time.sleep(1)

        # Click on the continue button
        driver.find_element(By.CSS_SELECTOR, ".form-action > .btn").click()

        # Select the checkbox
        driver.find_element(By.CSS_SELECTOR, '.rb-group:nth-child(9) > fieldset > .rb-option .rb-text > span').click()

        # Click on continue button again
        driver.find_element(By.CSS_SELECTOR, '.submit').click()

        # Select the year 
        driver.find_element(By.ID, 'selectEjercicio').click()
        Select(driver.find_element(By.ID, 'selectEjercicio')).select_by_visible_text(ejercicio)

        # Click on continue button once more
        driver.find_element(By.CSS_SELECTOR, '.submit').click()

        # Click on adding reference checkbox
        driver.find_element(By.CSS_SELECTOR, '.cb-label:nth-child(1) > .cb-text').click()

        # Fill in the reference
        driver.find_element(By.ID, 'informationTypeRef').click()
        driver.find_element(By.ID, 'informationTypeRef').send_keys(reference_text)

        # Show verification popup
        show_verification_popup()
        time.sleep(1)

    except TimeoutException as e:
        print(f"Error: {e}")

    finally:
        driver.close()

if __name__ == "__main__":
    DepositoDeCuentas("VOLKSWAGEN NAVARRA", "NAVARRA", "PEDIDO", "2022", use_captcha_solver=False)
    # test
    # DepositoDeCuentas("VOLKSWAGEN NAVARRA", "NAVARRA", "PEDIDO", "2022", use_captcha_solver=False)
