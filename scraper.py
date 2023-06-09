from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://www.woolworths.com.au/shop/productgroup/070623-wk50-kitchen-sepcials-offertile?icmpid=sm-hp-specials-tile2:kitchen-specials%7Cwk50::0037644')

products= []
for product in driver.find_elements(by=By.CSS_SELECTOR,value='.product-tile-v2'):
        product_titre = product.find_element(by=By.CSS_SELECTOR,value='.product-tile-title').text
        price = product.find_element(by=By.CSS_SELECTOR,value='.primary').text
        products.append({'title':product_titre,'price':price})

print(products)
driver.quit()

with open('sortie.txt', 'w', encoding='utf-8') as file:
    for product in products:
        file.write(product.text + '\n')
