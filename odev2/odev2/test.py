from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import traceback
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.webdriver import WebDriver as Edge
import random
import string
from django.test import Client
from django.contrib.auth.models import User

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import traceback
import random
import string
import os
from django.core.wsgi import get_wsgi_application
from dj_static import Cling


class InterfaceTests():
    
    def setup(self):
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        edge_options.add_argument('--disable-gpu')
        edge_options.add_argument('--no-sandbox')
        edge_options.add_argument('--disable-dev-shm-usage')
        edge_options.add_argument('--ignore-certificate-errors')
        edge_options.add_argument('--disable-web-security')
        edge_service = EdgeService("C:/Users/rabii/OneDrive/Masaüstü/edgedriver_win64/msedgedriver.exe")
        self.driver = Edge(service=edge_service, options=edge_options)
        


        # Django uygulamasının settings modülünü belirtin
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "odev2.settings")  # Projeye özgü settings modülünü burada belirtin

        # WSGI uygulamasını oluşturun
        application = Cling(get_wsgi_application())

        
        # self.global_email = None
        # self.global_password = None
        
    def tearDown(self):
       self.driver.quit()

    def register_testi(self):
        try:
            self.driver.get("http://127.0.0.1:8000/")
            print("Sayfa yüklendi: ", self.driver.title)

            # Sayfanın tam yüklenmesi bekleniyor.
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "login-icon"))
            )

            # Login butonuna tıklama
            loginButton = self.driver.find_element(By.ID, "login-icon")
            self.driver.execute_script("arguments[0].click();", loginButton)
            sleep(2)

            # Register Here butonuna tıklama
            buttonRegisterHere = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.ID, "go-register"))
            )
            buttonRegisterHere.click()
            sleep(2)

            # Kayıt formunu doldurma
            input_register_email = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "register-email"))
            )

            # Kullanım:
            email = self.generate_email()
            #self.global_email = email
            #sleep(2)
            input_register_email.send_keys(email)
            
            input_register_password = self.driver.find_element(By.ID, "register-password")
            input_register_password.send_keys("denemepsw")
            #self.global_password = "denemepsw"
            
            checkbox = self.driver.find_element(By.ID, "customCheck2")
            self.driver.execute_script("arguments[0].click();", checkbox)
           
            registerButton = self.driver.find_element(By.ID, "register")
            registerButton.click()
            
            # URL'nin kontrol edilmesi
            expected_url = "http://127.0.0.1:8000/#go-login"
            try:
                WebDriverWait(self.driver, 5).until(EC.url_to_be(expected_url))
                print("Register url kontrolü başarılı.")
            except Exception as e:
                print(" Register url kontrolünde bir hata oluştu:", e)

        except Exception as e:
            print("Hata oluştu:", e)
            traceback.print_exc()

    def generate_email(self):
        domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'icloud.com']
        name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(7))
        domain = random.choice(domains)
        email = f"{name}@{domain}"
        return email
    
    def login_testi(self):
        try:
            self.driver.get("http://127.0.0.1:8000/")
            print("Sayfa yüklendi: ", self.driver.title)
            # Sayfanın tam yüklenmesi bekleniyor
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "login-icon"))
            )

            # Login butonuna tıklama
            buttonLogin = self.driver.find_element(By.ID, "login-icon")
            self.driver.execute_script("arguments[0].click();", buttonLogin)
            sleep(2)
            

            # login formunu doldurma
            input_login_email = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, "login-email"))
            )
            #input_login_email.send_keys(self.global_email)
            input_login_email.send_keys("heittxw@hotmail.com")
            
            input_login_password = self.driver.find_element(By.ID, "login-password")
            #input_login_password.send_keys(self.global_password)
            input_login_password.send_keys("denemepsw")

            # loginButton'un tıklanabilir olması bekleniyor
            loginButton = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.ID, "login"))
            )
            loginButton.click()
            
            # URL kontrolü
            expected_url = "http://127.0.0.1:8000/login/"
            try:
                WebDriverWait(self.driver, 15).until(EC.url_to_be(expected_url))
                print("Login url kontrolü başarılı.")
            except Exception as e:
                print(" Login url kontrolünde bir hata oluştu:", e)

        
        except Exception as e:
            print("Hata oluştu:", e)
            traceback.print_exc()



    def industry_list_test(self):
        try:

            # Örnek bir kullanıcı oluşturun
            user = User.objects.create_user(username="heittxw@hotmail.com", email="heittxw@hotmail.com", password="denemepsw")

            # Test ortamında bir Django Client oluşturun
            client = Client()

            # Kullanıcı oturumunu açın
            client.login(username="heittxw@hotmail.com", password="denemepsw")

            # Selenium testlerini burada devam ettirin
            # Örnek: self.driver.get("http://127.0.0.1:8000/")

            self.driver.get("http://127.0.0.1:8000/login/")
   
            # Beklenen metin
            expected_text = "WELCOME"
            # Metnin bulunduğu elementin XPath veya CSS selector'ı
            element_locator = (By.CLASS_NAME, "slide__title")
            # Elementin metnini almak için WebDriverWait kullanarak bekleme yap
            element_text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element_locator)).text
            # Gerçekleşen metni ve beklenen metni karşılaştırın
            assert element_text == expected_text, f"Metin beklenenden farklı: {element_text}"
            print(element_text) 
            
        except Exception as e:
            print("Hata oluştu:", e)
            traceback.print_exc()
 


    def menu(self):
        print("Web Sitesi Arayüz Testi")
        print("1. Pop-up Testlerini Calistir")
        print("2. İmaj Kontrol Testlerini Calistir")
        print("3. Diğer Testler")
        print("0. Çıkış")

    def run_popup_tests(self):
        self.setup()
        self.register_testi()
        self.tearDown()

        self.setup()
        self.login_testi()
        self.tearDown()
        print("Pop-up testleri calistiriliyor...")
        #self.driver.quit()  # Tarayıcı oturumunu kapat


    def run_image_tests(self):
        print("İmaj kontrol testleri calistiriliyor... ")

    def run_other_tests(self):
        self.setup()
        self.industry_list_test()
        self.tearDown()
        print("Diğer testler calistiriliyor...")

def main():
    interface_tests = InterfaceTests()
    while True:
        print()
        interface_tests.menu()
        choice = input("Seçiminizi yapın: ")
        if choice == "1":
            interface_tests.run_popup_tests()
        elif choice == "2":
            interface_tests.run_image_tests()
        elif choice == "3":
            interface_tests.run_other_tests()
        elif choice == "0":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek! Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
