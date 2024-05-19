import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import traceback
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.webdriver import WebDriver as Edge
import random
import re


class InterfaceTests:

    def setup(self):
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        edge_options.add_argument('--headless') #arka planda calisir.
        edge_options.add_argument('--disable-gpu')
        edge_options.add_argument('--no-sandbox')
        edge_options.add_argument('--disable-dev-shm-usage')
        edge_options.add_argument('--ignore-certificate-errors')
        edge_options.add_argument('--disable-web-security')
        edge_service = EdgeService("C:/Users/rabii/OneDrive/Masaüstü/edgedriver_win64/msedgedriver.exe")
        self.driver = Edge(service=edge_service, options=edge_options)


    def tearDown(self):
        self.driver.quit()


    def register_testi(self):
        try:
            self.driver.get("http://127.0.0.1:3000/")
            print("Sayfa yüklendi: ", self.driver.title)

            # Sayfanın tam yüklenmesi bekleniyor.
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, "login-icon"))
            )

            # Login butonuna tıklama
            loginButton = self.driver.find_element(By.ID, "login-icon")
            self.driver.execute_script("arguments[0].click();", loginButton)
            sleep(2)

            # Register Here butonuna tıklama
            buttonRegisterHere = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.ID, "go-register"))
            )
            buttonRegisterHere.click()
            sleep(2)

            # Kayıt formunu doldurma
            input_register_email = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, "register-email"))
            )

            # Kullanım:
            email = self.generate_email()
            input_register_email.send_keys(email)

            input_register_password = self.driver.find_element(By.ID, "register-password")
            input_register_password.send_keys("denemepsw")

            checkbox = self.driver.find_element(By.ID, "customCheck2")
            self.driver.execute_script("arguments[0].click();", checkbox)

            registerButton = self.driver.find_element(By.ID, "register")
            registerButton.click()

            # URL'nin kontrol edilmesi
            expected_url = "http://127.0.0.1:3000/#go-login"
            try:
                WebDriverWait(self.driver, 5).until(EC.url_to_be(expected_url))
                print("Register url kontrolü başarılı.")
            except Exception as e:
                print(" Register url kontrolünde bir hata oluştu:", e)

        except Exception as e:
            print("Hata oluştu:", e)
            traceback.print_exc()

            
    def unsuccess_register_testi(self):
        try:
            #kayıtlı olan bir mail ile yeniden register yapılırsa hatalı olur.
            self.driver.get("http://127.0.0.1:3000/")
            print("Sayfa yüklendi: ", self.driver.title)

            # Sayfanın tam yüklenmesi bekleniyor.
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, "login-icon"))
            )

            # Login butonuna tıklama
            loginButton = self.driver.find_element(By.ID, "login-icon")
            self.driver.execute_script("arguments[0].click();", loginButton)
            sleep(2)

            # Register Here butonuna tıklama
            buttonRegisterHere = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.ID, "go-register"))
            )
            buttonRegisterHere.click()
            sleep(2)

            # Kayıt formunu doldurma
            input_register_email = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, "register-email"))
            )

            # Kullanım:
            email ="heittxw@hotmail.com"
            input_register_email.send_keys(email)

            input_register_password = self.driver.find_element(By.ID, "register-password")
            input_register_password.send_keys("denemepsw")

            checkbox = self.driver.find_element(By.ID, "customCheck2")
            self.driver.execute_script("arguments[0].click();", checkbox)

            registerButton = self.driver.find_element(By.ID, "register")
            registerButton.click()

            # URL'nin kontrol edilmesi, işlem başarısız ise yalnızca a dönülür.
            expected_url = "http://127.0.0.1:3000/"
            try:
                WebDriverWait(self.driver, 15).until(EC.url_to_be(expected_url))
                print("Başarısız Register Denemesi")
            except Exception as e:
                print(" Register işleminde bir hata oluştu:", e)

        except Exception as e:
            print("Hata oluştu:", e)
            traceback.print_exc()


    def login_testi(self):
        self.login()

    def unsuccess_login_testi(self):
        try:
            self.driver.get("http://127.0.0.1:3000/")
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
            
            #kayıtlı olmayan bir mail adresi kullanıyoruz
            input_login_email.send_keys("belirsiz@out.tr")

            input_login_password = self.driver.find_element(By.ID, "login-password")
            input_login_password.send_keys("denemepsw")

            # loginButton'un tıklanabilir olması bekleniyor
            loginButton = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.ID, "login"))
            )
            loginButton.click()

            # URL kontrolü
            expected_url = "http://127.0.0.1:3000/#go-login"
            try:
                WebDriverWait(self.driver, 5).until(EC.url_to_be(expected_url))
                print("Başarısız Login Denemesi.")
            except Exception as e:
                print(" Login işlemi kontrolünde bir hata oluştu:", e)
                
        except Exception as e:
            print("Hata oluştu:", e)
            traceback.print_exc()

    def logout_test(self):
        try:
            self.login()

            # Çıkış butonunun tıklanabilir olması bekleniyor.
            logout_form = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div/header/nav/div/div[1]/ul/li/ul/li/form"))
            )
            href = logout_form.get_attribute("action")  
            self.driver.get(href)
            
            expected_url = "http://127.0.0.1:3000/"
            try:
                WebDriverWait(self.driver, 15).until(EC.url_to_be(expected_url))
                print("Logout kontrolü başarılı.")
            except Exception as e:
                print("Logout kontrolünde bir hata oluştu:", e)
            
        except Exception as e:
            print("Hata oluştu:", e)
            traceback.print_exc()
            
    def userInfo_test(self):
        try:
            self.login()
            
            #user home sayfasında element kontrolü
            #Beklenen metin, login işleminden sonra açılan sayfada bulunur.
            expected_text = "Heittxw@Hotmail.Com"
            # Metnin bulunduğu elementin XPath veya CSS selector'ı
            element_locator = (By.ID, "username")
            # Elementin metnini almak için WebDriverWait kullanarak bekleme yap
            element_text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element_locator)).text
            # Gerçek metni ve beklenen metni karşılaştırın
            assert element_text == expected_text, f"Metin beklenenden farklı: {element_text}"
            print("User info testi başarılı. Kullanıcı adı, kullanıcı anasayfasında görüntülenmekte.")
            
        except Exception as e:
            print("Hata oluştu:", e)
            traceback.print_exc()
            
        
    def industry_list_test(self):
    
        self.login()
        self.openIndustryPage()    
  
    def industry_list_test_with_url(self):
        self.login()
        try:
            self.driver.get( "http://127.0.0.1:3000/industries")
            element_industries = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID , "industry-single")))
           
            print("Url girişi ile İndustry sayfasının açılması başarılı.")
            
        except Exception as e:
            print("Hata oluştu:", e)
            traceback.print_exc()
                
    
    def industry_single_test(self):
        try:
            self.login()
            self.openIndustryPage()
            
            element_single = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID , "industry-single"))
        )
            href_single = element_single.get_attribute("href") 
            
            self.driver.get(href_single ) #id belirtiliyor.
            sleep(2)
            print(href_single)
           
            expected_url = "http://127.0.0.1:3000/single-industry/1/"
            try:
                WebDriverWait(self.driver, 15).until(EC.url_to_be(expected_url))
                print("industry-single url kontrolü başarılı.")
            except Exception as e:
                print("industry-single url kontrolünde bir hata oluştu:", e)
                
        except Exception as e:
            print("Hata oluştu:", e)
            traceback.print_exc()



    def industry_popup_açma_testi(self):
        try:
            self.login()
            self.openIndustryPage()
                
                
            industryPopup = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID , "industry-popup"))
            )
            
            openIndustryFormButton = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID , "openIndustryForm"))
            )
            
            first_display_state =industryPopup.get_attribute("style")
            print("first state " + first_display_state)
            
            openIndustryFormButton.click()
            second_display_state =industryPopup.get_attribute("style")
            print("second state" + second_display_state)
            
            if first_display_state== "display: none;" and second_display_state == "display: block;":
                print( "İndustry ekleme popup açma testi başarılı.")
            
        except Exception as e:
            print("Hata oluştu:", e)
            traceback.print_exc()
            
    def industry_popup_kapatma_testi(self):
        try:
            self.login()
            self.openIndustryPage()
                
            industryPopup = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID , "industry-popup"))
            )
            
            openIndustryFormButton = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID , "openIndustryForm"))
            )
            
            first_display_state =industryPopup.get_attribute("style")
            print("first state " + first_display_state)
            
            openIndustryFormButton.click()
            
            second_display_state =industryPopup.get_attribute("style")
            print("second state " + second_display_state)
            
            openIndustryFormButton.click()
            
            third_display_state =industryPopup.get_attribute("style")
            print("third state " + third_display_state)

            
            if first_display_state== "display: none;" and second_display_state == "display: block;" and third_display_state=="display: none;":
                print( "İndustry ekleme popup kapatma testi başarılı.")
            
        except Exception as e:
            print("Hata oluştu:", e)
            traceback.print_exc()


    def add_industry_test(self):
        try:
            self.login()
            self.openIndustryPage()

            
            add_button = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH , "/html/body/div/section[1]/div/div[1]/div[3]/button"))
            )
            add_button.click() 
            sleep(1)
            
            input_title=WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH , "/html/body/div/section[1]/div/div[2]/div/form/div[1]/input"))
            )
            input_description=WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH , "/html/body/div/section[1]/div/div[2]/div/form/div[2]/textarea"))
            ) 
            input_content=WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH , "/html/body/div/section[1]/div/div[2]/div/form/div[3]/textarea"))
            )
            
            file_input = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH , "/html/body/div/section[1]/div/div[2]/div/form/div[4]/input"))
            )  # veya By.CSS_SELECTOR, By.XPATH gibi

            # Dosya yolu belirle
            file_path = os.path.abspath("odev2/static/assets/images/services/1.jpg")  # Yüklemek istediğiniz dosyanın mutlak yolu

            # Dosya seçimi gönder
            input_title.send_keys("Deneme Endüstri Başlık")
            input_description.send_keys("Deneme Endüstri Açıklama")
            input_content.send_keys("Deneme Endüstri İçerik")
            file_input.send_keys(file_path)

            sleep(3)
            button_add =WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH , "/html/body/div/section[1]/div/div[2]/div/form/button"))
            ) 
            button_add.click()
            
            message =WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH , "/html/body/div/section[1]/div/div[1]/div[2]/div/h5"))
            ).text
            expected_text = "Industry Added Successfully."
            print(message)
            assert message == expected_text, f"False: {message}"
            print("İndustry ekleme testi başarılı.")
              
        except Exception as e:
            print("Hata oluştu:", e)
            traceback.print_exc()
    
            
    def blog_list_test(self):
        
        self.login()
        self.openBlogPage()
    
    def blog_list_test_with_url(self):
        self.login()
        try:
            self.driver.get( "http://127.0.0.1:3000/blog")
            element_blog= WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID , "single-blog-pk")))
           
            print("Url girişi ile blog sayfasının açılması başarılı.")
            
        except Exception as e:
            print("Hata oluştu:", e)
            traceback.print_exc()
        
    def blog_single_test(self):
        try:
            self.login()
            self.openBlogPage()
            
            element_single = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID , "single-blog-pk"))
        )
            href_single = element_single.get_attribute("href") 
            
            self.driver.get(href_single ) #id belirtiliyor.0
            print(href_single)
            expected_url = "http://127.0.0.1:3000/blog-single-post/1/"
            try:
                WebDriverWait(self.driver, 15).until(EC.url_to_be(expected_url))
                print("blog-single post url kontrolü başarılı.")
              
            except Exception as e:
                print("blog-single post url kontrolünde bir hata oluştu:", e)
                print(False)
        except Exception as e:
            print("Hata oluştu:", e)
            traceback.print_exc()

    def blog_popup_açma_testi(self):
        try:
            self.login()
            self.openBlogPage()
                
                
            blogPopup = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID , "blog-popup"))
            )
            
            openBlogFormButton = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID , "openBlogForm"))
            )
            
            first_display_state =blogPopup.get_attribute("style")
            print("first state " + first_display_state)
            
            openBlogFormButton.click()
            second_display_state =blogPopup.get_attribute("style")
            print("second state " + second_display_state)
            
            if first_display_state== "display: none;" and second_display_state == "display: block;":
                print("Blog ekleme popupu açma testi başarılı.")
            
            
        except Exception as e:
            print("Hata oluştu:", e)
            traceback.print_exc()
    
    def blog_popup_kapatma_testi(self):
        try:
            self.login()
            
            self.openBlogPage()
                
                
            blogPopup = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID , "blog-popup"))
            )
            
            openBlogFormButton = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID , "openBlogForm"))
            )
            
            first_display_state =blogPopup.get_attribute("style")
            print("first state " + first_display_state)
            
            openBlogFormButton.click()
            
            second_display_state =blogPopup.get_attribute("style")
            print("second state " + second_display_state)
            
            openBlogFormButton.click()
            
            third_display_state =blogPopup.get_attribute("style")
            print("third state " + third_display_state)
            
            if first_display_state== "display: none;" and second_display_state == "display: block;" and third_display_state== "display: none;":
                print("Blog ekleme popupu kapatma testi başarılı.")
            
            
        except Exception as e:
            print("Hata oluştu:", e)
            traceback.print_exc()
        
        
    def add_blog_post_test(self):
        try:
            self.login()
            self.openBlogPage()
   
            
            add_button = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH , "/html/body/div/section[1]/div/div[1]/div[3]/button"))
            )
            add_button.click() 
            sleep(1)
            
            input_title=WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH , "/html/body/div/section[1]/div/div[2]/div/form/div[1]/input"))
            )
            file_input = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH , "/html/body/div/section[1]/div/div[2]/div/form/div[2]/input"))
            )
            input_content=WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH , "/html/body/div/section[1]/div/div[2]/div/form/div[3]/textarea"))
            )
            
            # Dosya yolu belirle
            file_path = os.path.abspath("odev2/static/assets/images/services/1.jpg")  # Yüklemek istediğiniz dosyanın mutlak yolu

            # Dosya seçimi gönder
            input_title.send_keys("Deneme Blog Başlık")
            input_content.send_keys("Deneme Blog İçerik")
            file_input.send_keys(file_path)

            sleep(3)
            button_add =WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH , "/html/body/div/section[1]/div/div[2]/div/form/button"))
            ) 
            button_add.click()
            
            message =WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH , "/html/body/div/section[1]/div/div[1]/div[2]/div/h5"))
            ).text
            expected_text = "Blog Post Added Successfully."
            print(message)
            assert message == expected_text, f"False : {message}"
            print(True)
            
        except Exception as e:
            print("Hata oluştu:", e)
            traceback.print_exc()

    def unsuccess_add_blog_post_test(self):
        try:
            #bu fonksşyon ile forma eksik veri yollanarak yeni post ekleme işleminin başarısız olması durumu kurgulanmıştır.
            self.login()
            self.openBlogPage()
            
            add_button = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH , "/html/body/div/section[1]/div/div[1]/div[3]/button"))
            )
            add_button.click() 
            sleep(1)
            
            input_title=WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH , "/html/body/div/section[1]/div/div[2]/div/form/div[1]/input"))
            )
            file_input = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH , "/html/body/div/section[1]/div/div[2]/div/form/div[2]/input"))
            )
            input_content=WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH , "/html/body/div/section[1]/div/div[2]/div/form/div[3]/textarea"))
            )
            
            # Dosya yolu belirle
            file_path = os.path.abspath("odev2/static/assets/images/services/1.jpg")  # Yüklemek istediğiniz dosyanın mutlak yolu

            # Dosya seçimi gönder
            input_title.send_keys("Deneme Blog Başlık")
            input_content.send_keys("Deneme Blog İçerik")
            
            #eksik veri gönderme 
            #file_input.send_keys(file_path)

            sleep(3)
            button_add =WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH , "/html/body/div/section[1]/div/div[2]/div/form/button"))
            ) 
            button_add.click()
            
            message =WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH , "/html/body/div/section[1]/div/div[1]/div[2]/div/h5"))
            ).text
            expected_text = "Failed To Add Blog Post. Please Check Your Input."
            print(message)
            assert message == expected_text, f"False : {message}"
            print(True)
            
        except Exception as e:
            print("Hata oluştu:", e)
            traceback.print_exc()
    
    def unsuccess_add_industry_test(self):
        #formda eksik veri gönderiliyor.ekleme işlemi başarısız olmalı.
        try:
            self.login()
            self.openIndustryPage()
   
            
            add_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH , "/html/body/div/section[1]/div/div[1]/div[3]/button"))
            )
            add_button.click() 
            sleep(1)
            
            input_title=WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH , "/html/body/div/section[1]/div/div[2]/div/form/div[1]/input"))
            )
            input_description=WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH , "/html/body/div/section[1]/div/div[2]/div/form/div[2]/textarea"))
            ) 
            input_content=WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH , "/html/body/div/section[1]/div/div[2]/div/form/div[3]/textarea"))
            )
            
            file_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH , "/html/body/div/section[1]/div/div[2]/div/form/div[4]/input"))
            )  # veya By.CSS_SELECTOR, By.XPATH gibi

            # Dosya yolu belirle
            file_path = os.path.abspath("odev2/static/assets/images/services/1.jpg")  # Yüklemek istediğiniz dosyanın mutlak yolu

            #eksik veri
            #input_title.send_keys("Deneme Endüstri Başlık")
            
            input_description.send_keys("Deneme Endüstri Açıklama")
            input_content.send_keys("Deneme Endüstri İçerik")
            file_input.send_keys(file_path)

            sleep(3)
            button_add =WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH , "/html/body/div/section[1]/div/div[2]/div/form/button"))
            ) 
            button_add.click()
            
            message =WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH , "/html/body/div/section[1]/div/div[1]/div[2]/div/h5"))
            ).text
            expected_text = "Failed To Add Industry. Please Check Your Input."
            print(message)
            assert message == expected_text, f"False: {message}"
            print(True)
                  
        except Exception as e:
            print("Hata oluştu:", e)
            traceback.print_exc()

    def url_ile_login_popup_açma(self):
        try:
            self.driver.get("http://127.0.0.1:3000/#go-login")
            
             # login formunu doldurma
            input_login_email = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, "login-email"))
            )
            print("Login popup başarıyla açıldı.")
            
        except Exception as e:
            print("Hata oluştu:", e)
            traceback.print_exc()
    
    def url_ile_register_popup_açma(self):
        try:
            self.driver.get("http://127.0.0.1:3000/#go-register")
            
            input_register_email = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, "register-email")))
            print("Register popup başarıyla açıldı.")

        except Exception as e:
            print("Hata oluştu:", e)
            traceback.print_exc()
    
    def single_blog_image_test(self):
        self.blog_single_test()
        blog_image= WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, " /html/body/div/section[2]/div/div/div[1]/div[1]/div[1]/a/img")))
        source= blog_image.get_attribute("src")
        print(source)
        print("image başarıyla yüklendi.")
       
    
    def blog_list_image_test(self):
        self.blog_list_test()
        try:
           
            blog_list_image = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div/section[2]/div/div[1]/div[1]/div/div[1]/img")))
            
            source= blog_list_image.get_attribute("src")
            print(source)
            #<img src="/static/assets/images/blog/single/1.jpg" alt="blog image">
            print("image başarıyla yüklendi.")
        
        except Exception as e:
            print("Hata oluştu:", e)
            traceback.print_exc()
        
    def industry_list_image_test(self):
        
        self.industry_list_test()
        try:
            industry_list_image = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div/section[2]/div/div[2]/div[1]/div/div[1]/a/img")))
            source= industry_list_image.get_attribute("src")
            print(source)
            #<img src="/static/assets/images/about/4.jpg" alt="industry image" style="width: 350px; height: 350px;">
            print("image başarıyla yüklendi.")
        
        except Exception as e:
            print("Hata oluştu:", e)
            traceback.print_exc()
        
    def single_industry_image_test(self):
        try:
            self.industry_single_test()
            industry_image = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div/section[3]/div/div/div[2]/div/div/img")))
            source= industry_image.get_attribute("src")
            print(source)
            print("image başarıyla yüklendi.")
        
        except Exception as e:
            print("Hata oluştu:", e)
            traceback.print_exc()
            
    def index_image_test(self):
        try:
            self.driver.get("http://127.0.0.1:3000")
            index_image = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div/header/nav/div/a/img[2]")))
            source= index_image.get_attribute("src")
            print(source)
            print("image başarıyla yüklendi.")
        except Exception as e:
            print("Hata oluştu:", e)
            traceback.print_exc()
        

    def menu(self):
        print("Web Sitesi Arayüz Testi")
        print("1. Pop-up Testlerini Çalıştır")
        print("2. İmaj Kontrol Testlerini Çalıştır")
        print("3. Listeleme Testlerini Çalıştır")
        print("4. Nesne Ekleme Testlerini Çalıştır")
        print("5. Diğer Testleri Çalıştır")
        print("0. Çıkış")


    def run_popup_tests(self):
        print("Pop-up testleri çalıştırılıyor...")
        self.setup()
        self.register_testi()
        self.tearDown()
        
        self.setup()
        self.unsuccess_register_testi()
        self.tearDown()


        self.setup()
        self.login_testi()
        self.tearDown()
        
        self.setup()
        self.unsuccess_login_testi()
        self.tearDown()
        
        self.setup()
        self.industry_popup_açma_testi()
        self.tearDown()
        
        self.setup()
        self.industry_popup_kapatma_testi()
        self.tearDown()
        
        self.setup()
        self.url_ile_login_popup_açma()
        self.tearDown()
        
        self.setup()
        self.url_ile_register_popup_açma()
        self.tearDown()
        
        self.setup()
        self.blog_popup_açma_testi()
        self.tearDown()
        
        self.setup()
        self.blog_popup_kapatma_testi()
        self.tearDown()
        
        

    def run_image_tests(self):
        print("İmaj kontrol testleri çalıştırılıyor... ")
        #alt metin kontrolu ve resimlerin varlıgının kontrolunu yapabilirsin., boyutunun kontrolunu yapabilirsin.
        #datasoft yuklenıyor mu kontrol et.
        
        self.setup()
        self.single_blog_image_test()
        self.tearDown()
        
        self.setup()
        self.single_industry_image_test()
        self.tearDown()
        
        self.setup()
        self.blog_list_image_test()
        self.tearDown()
        
        self.setup()
        self.industry_list_image_test()
        self.tearDown()
        
        self.setup()
        self.index_image_test()
        self.tearDown()


    def run_list_tests(self):
        print("Listeleme testleri çalışıyor...")             

        self.setup()
        self.industry_list_test()
        self.tearDown()
        
        self.setup()
        self.blog_list_test()
        self.tearDown()
        
        self.setup()
        self.industry_list_test_with_url()
        self.tearDown()
        
        self.setup()
        self.blog_list_test_with_url()
        self.tearDown()
        
        
    def run_add_tests(self):
        print("Nesne Ekleme testleri çalıştırılıyor...")             

        self.setup()
        self.add_industry_test()
        self.tearDown()
        
        self.setup()
        self.unsuccess_add_industry_test()
        self.tearDown()
        
        self.setup()
        self.add_blog_post_test()
        self.tearDown()
        
        self.setup()
        self.unsuccess_add_blog_post_test()
        self.tearDown()
        
        
    def run_other_tests(self):
        print("Diğer testler çalıştırılıyor...")             
      
        self.setup()
        self.industry_single_test()
        self.tearDown()
        
        self.setup()
        self.blog_single_test()
        self.tearDown()
        
        self.setup()
        self.logout_test()
        self.tearDown()
        
        self.setup()
        self.userInfo_test()
        self.tearDown()
    
    
    def login(self):
        try:
            self.driver.get("http://127.0.0.1:3000/")
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
            input_login_email.send_keys("heittxw@hotmail.com")

            input_login_password = self.driver.find_element(By.ID, "login-password")
            input_login_password.send_keys("denemepsw")

            # loginButton'un tıklanabilir olması bekleniyor
            loginButton = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.ID, "login"))
            )
            loginButton.click()

            # Login işlemi için URL kontrolü yapılıyor.
            expected_url = "http://127.0.0.1:3000/login/"
            try:
                WebDriverWait(self.driver, 15).until(EC.url_to_be(expected_url))
                print("Login url kontrolü başarılı.")
            except Exception as e:
                print("Login url kontrolünde bir hata oluştu:", e)
            
        except Exception as e:
            print("Hata oluştu:", e)
            traceback.print_exc()
            
    def openBlogPage(self):
        try:
            #blog sayfasına gidilmesi
            element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID , "blog"))
        )
            href = element.get_attribute("href")  
            self.driver.get(href)
            sleep(2)
            #industreiese gitti mi kontrol et. expected values ile..
            expected_url = "http://127.0.0.1:3000/blog/"
            try:
                WebDriverWait(self.driver, 15).until(EC.url_to_be(expected_url))
                print("blog url kontrolü başarılı.")
               
            except Exception as e:
                print("blog url kontrolünde bir hata oluştu:", e)
                print(False)    
        except Exception as e:
            print("Hata oluştu:", e)
            traceback.print_exc()        

    def openIndustryPage(self):
        try:
            #industries sayfasına gidilmesi
            element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID , "industries"))
        )
            href = element.get_attribute("href")  
            self.driver.get(href)
            sleep(2)
            #industreiese gitti mi kontrol et. expected values ile..
            expected_url = "http://127.0.0.1:3000/industries/"
            try:
                WebDriverWait(self.driver, 15).until(EC.url_to_be(expected_url))
                print("industries url kontrolü başarılı.")
            except Exception as e:
                print("industries url kontrolünde bir hata oluştu:", e)
            
        except Exception as e:
            print("Hata oluştu:", e)
            traceback.print_exc() 
    
    
    def generate_email(self):
        domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'icloud.com']
        name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(7))
        domain = random.choice(domains)
        email = f"{name}@{domain}"
        return email

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
            interface_tests.run_list_tests()
        elif choice == "4":
            interface_tests.run_add_tests() 
        elif choice == "5":
            interface_tests.run_other_tests()
        elif choice == "0":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek! Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()