import sqlite3
import pandas as pd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import random
from time import sleep
from PIL import Image
from io import BytesIO


class PyhtonSelenium():

    def __init__(self):
        self.my_conexion = sqlite3.connect("database/mydatabase")

    def selenium_p(self):
        self.database = pd.DataFrame(columns=['ID', 'href', 'nombre', 'detalle', 'precio', 'cant_review'])  # noqa
        try:
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # noqa
            sleep(random.uniform(0.0, 2.0))
            url = 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops'  # noqa
            self.driver.get(url)
            count = 2
            p = 0
            cont = 0
            while p == 0:
                self.rows = self.driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div[@class="row"]//div[@class="col-sm-4 col-lg-4 col-md-4"]')  # noqa
                try:
                    for row in self.rows:
                        href = row.find_element_by_xpath('.//div/div[1]/h4[2]/a').get_attribute('href')  # noqa
                        self.database.loc[cont, 'href'] = href
                        cont += 1

                    url_1 = f'{url}?page={count}'
                    self.driver.get(url_1)
                    count += 1

                    if count > 21:
                        p = 1
                    else:
                        p = 0
                except Exception as e:
                    print(e)
                    pass
            self.database['ID'] = self.database['href'].apply(lambda x: x.replace('https://webscraper.io/test-sites/e-commerce/static/product/', ''))  # noqa
            list_href = self.database['href'].to_list()
            contador = 0
            for href in list_href:
                try:
                    self.driver.get(href)
                    nombre = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/h4[2]').text  # noqa
                    self.database.loc[contador, 'nombre'] = nombre
                    detalle = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/p').text  # noqa
                    self.database.loc[contador, 'detalle'] = detalle
                    precio = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/h4[1]').text  # noqa
                    self.database.loc[contador, 'precio'] = precio
                    review = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[3]/p').text  # noqa
                    self.database.loc[contador, 'cant_review'] = review
                    review_number = int(review.replace(' reviews', '').strip())
                    contador += 1
                    if review_number >= 10:
                        png = self.driver.get_screenshot_as_png()
                        im = Image.open(BytesIO(png))
                        nombre = nombre.replace('/', ' ').replace('"', '')
                        im.save(f'{nombre}.png')
                    else:
                        pass

                except Exception as e:
                    print(e)
                    break

            self.database.to_sql("prueba_selenium", self.my_conexion)
            self.my_conexion.close()
            self.driver.implicitly_wait(3)
            self.driver.close()
            return("ok")
        except Exception as e:
            return(e)


if __name__ == "__main__":
    p = PyhtonSelenium()
    print(p.selenium_p())
