from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa el web driver de Chrome o el navegador de preferencia

def initialize_driver():
    options = webdriver.ChromeOptions()

    # Definir un User-Agent falso (simulamos un usuario real en Chrome en Windows 10)

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    options.add_argument(f"user-agent={user_agent}")

    # Opciones de Chrome

    #options.add_argument("--headless") # Modo "headless" (sin interfaz gráfica) → Si descomentas esta línea, el navegador se ejecutará en segundo plano, sin abrir una ventana visual. Ideal para pruebas automatizadas en servidores.
    options.add_argument("--disable-gpu") #Desactiva el uso de la GPU → Se usa cuando el navegador está en modo headless, ya que algunas versiones de Chrome pueden fallar sin esta opción.
    options.add_argument("--incognito") # -> Ejecuta Chrome en modo incógnito → Esto significa que el navegador no guardará caché, cookies ni historial.
    #options.add_argument("--start-maximized") # -> Abre el navegador en pantalla completa
    options.add_argument("--no-sandbox") #-> Desactiva el "sandboxing" → Útil en entornos como Docker o Linux, donde la seguridad del sandbox puede causar problemas al ejecutar Selenium.
    options.add_argument("--disable-dev-shm-usage") #->  Evita problemas de memoria compartida → En algunos sistemas, el navegador puede quedarse sin memoria compartida y fallar. Esta opción previene ese problema.
    options.add_experimental_option("excludeSwitches", ["enable-automation"]) # -> Evita que el sitio web detecte que estás usando Selenium → Algunos sitios web pueden comportarse de forma diferente si detectan que estás usando un bot de pruebas.
    options.add_experimental_option('useAutomationExtension', False) # -> Deshabilita la extensión de automatización de Chrome → Algunos sitios web pueden detectar la extensión de automatización y comportarse de forma diferente.
    driver = webdriver.Chrome(options=options)
    return driver

#Función para crear un puntero rojo en la página
def add_pointer(driver):
    script = """
    var pointer = document.createElement('div');
    pointer.id = 'selenium-pointer';
    pointer.style.position = 'absolute';
    pointer.style.width = '10px';
    pointer.style.height = '10px';
    pointer.style.background = 'red';
    pointer.style.borderRadius = '50%';
    pointer.style.zIndex = '9999';
    pointer.style.transition = 'top 0.2s ease-out, left 0.2s ease-out';
    document.body.appendChild(pointer);
    """
    driver.execute_script(script)

#Función para mover el puntero rojo a un elemento
def move_pointer(driver, element):
    script = """
    var pointer = document.getElementById('selenium-pointer');
    var rect = arguments[0].getBoundingClientRect();
    pointer.style.left = (rect.left + window.scrollX + rect.width / 2) + 'px';
    pointer.style.top = (rect.top + window.scrollY + rect.height / 2) + 'px';
    """
    driver.execute_script(script, element)
    time.sleep(0.5)  # Pequeña pausa para visualizar el movimiento

# Función para realizar login con puntero rojo guiando los pasos

def login(driver):
    add_pointer(driver)  # Agrega el puntero rojo

    input_username = driver.find_element(By.ID, "user-name")
    move_pointer(driver, input_username)  # Mueve el puntero al campo de usuario
    container_username = driver.find_element(By.XPATH, "//*[@id='login_credentials']")
    #print(container_username.text)
    split_container = container_username.text.split("\n")
    #print(split_container)
    user_name = split_container[1]
    input_username.send_keys(user_name)
    print(user_name)
    time.sleep(1)

    input_password = driver.find_element(By.ID, "password")
    move_pointer(driver, input_password)  # Mueve el puntero al campo de contraseña
    container_password = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[2]')
    #print(container_password.text)
    split_container_password = container_password.text.split("\n")
    password = split_container_password[1]
    print(password)
    input_password.send_keys(password)
    time.sleep(1)

    login_button = driver.find_element(By.ID, "login-button")
    move_pointer(driver, login_button)  # Mueve el puntero al botón de login
    login_button.click()
    time.sleep(1)
    return driver

def check_backpack(driver):
    backpack_button = driver.find_element(By.XPATH, '//*[@id="item_4_img_link"]/img')
    move_pointer(driver, backpack_button)
    backpack_button.click()
    time.sleep(1)
    return driver

def add_to_cart(driver):
    add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart"]')
    move_pointer(driver, add_to_cart_button)
    add_to_cart_button.click()
    time.sleep(1)
    return driver

def check_cart(driver):
    cart_button = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    move_pointer(driver, cart_button)
    cart_button.click()
    time.sleep(1)
    return driver

def chechout(driver):
    checkout_button = driver.find_element(By.ID, 'checkout')
    move_pointer(driver, checkout_button)
    checkout_button.click()
    time.sleep(1)
    return driver

def input_first_name(driver):
    first_name = driver.find_element(By.ID, 'first-name')
    move_pointer(driver, first_name)
    first_name.send_keys("Juan")
    time.sleep(1)
    return driver

def input_last_name(driver):
    last_name = driver.find_element(By.ID, 'last-name')
    move_pointer(driver, last_name)
    last_name.send_keys("Perez")
    time.sleep(1)
    return driver

def input_postal_code(driver):
    postal_code = driver.find_element(By.ID, 'postal-code')
    move_pointer(driver, postal_code)
    postal_code.send_keys("12345")
    time.sleep(1)
    return driver

def button_continue_click(driver):
    continue_button = driver.find_element(By.ID, 'continue')
    move_pointer(driver, continue_button)
    continue_button.click()
    time.sleep(1)
    return driver

def button_finish_click(driver):
    finish_button = driver.find_element(By.ID, 'finish')
    move_pointer(driver, finish_button)
    finish_button.click()
    time.sleep(1)
    return driver

def button_back_home_click(driver):
    back_home_button = driver.find_element(By.ID, 'back-to-products')
    move_pointer(driver, back_home_button)
    back_home_button.click()
    time.sleep(1)
    return driver

def menu_button_click(driver):
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    move_pointer(driver, menu_button)
    menu_button.click()
    print("Menu button clicked")
    time.sleep(1)
    return driver

def logout_login(driver):
    menu_button = driver.find_element(By.ID, "logout_sidebar_link")
    move_pointer(driver, menu_button)
    menu_button.click()
    time.sleep(1)
    return driver

def main():
    driver = initialize_driver()
    driver.get("http://www.saucedemo.com")
    driver = login(driver)
    if driver.current_url == "https://www.saucedemo.com/inventory.html":
        print("Login exitoso")
        time.sleep(2)

        driver = check_backpack(driver)
        print("Backpack clicked")
        time.sleep(2)

        driver = add_to_cart(driver)
        print("Added to cart")
        time.sleep(2)

        driver = check_cart(driver)
        print("Cart checked")
        time.sleep(2)

        driver = chechout(driver)
        print("Checkout clicked")
        time.sleep(2)

        driver = input_first_name(driver)
        print("First name input")   
        time.sleep(2)

        driver = input_last_name(driver)
        print("Last name input")
        time.sleep(2)

        driver = input_postal_code(driver)
        print("Postal code input")  
        time.sleep(2)

        driver = button_continue_click(driver)
        print("Continue button clicked")
        time.sleep(2)
        
        driver = button_finish_click(driver)
        print("Finish button clicked")
        time.sleep(2)

        driver = button_back_home_click(driver)
        print("Back home button clicked")
        time.sleep(2)


        driver = menu_button_click(driver)
        print("Menu button clicked")
        time.sleep(2)

        driver = logout_login(driver)
        print("Logout button clicked")
        time.sleep(2)
        print("logout exitoso")
        
        driver.quit()
        print("Driver closed")
    else:
        print("Login fallido")


if __name__ == "__main__":
    main()