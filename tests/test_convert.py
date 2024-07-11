from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_converted_rate(from_currency, to_currency, amount):
    try:
        driver = webdriver.Chrome()
        driver.get('https://finance.rambler.ru/calculators/converter/')

        # Ожидание загрузки элементов
        WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.ID, 'converterFrom'))
        )
        WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.ID, 'converterTo'))
        )
        WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.ID, 'converterAmount'))
        )

        # Выбор исходной валюты
        driver.find_element(By.ID, 'converterFrom').send_keys(from_currency)
        # Выбор целевой валюты
        driver.find_element(By.ID, 'converterTo').send_keys(to_currency)
        # Ввод количества единиц
        driver.find_element(By.ID, 'converterAmount').send_keys(str(amount))

        # Ожидание обновления результата
        WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.ID, 'converterResult'))
        )

        # Получение результата
        result = driver.find_element(By.ID, 'converterResult').text

    except Exception as e:
        print(f'Error: {e}')
        result = None
    finally:
        driver.quit()

    return result

if __name__ == '__main__':
    from_currency = 'EUR'
    to_currency = 'AUD'
    amount = 10
    try:
        converted_rate = get_converted_rate(from_currency, to_currency, amount)
        print(f'Converted rate from {from_currency} to {to_currency} for {amount} units: {converted_rate}')
    except Exception as e:
        print(f'Error: {e}')