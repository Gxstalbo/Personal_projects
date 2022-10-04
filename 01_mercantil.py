from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.mercantil.com/")
ruts=['92580000-7','90413000-1','76.102.960-6','76124890-1','96.799.250-K','77013680-6']
df_rut=pd.DataFrame()
list_rut=[]
time_start=time.time()

for rut in (ruts):
    WebDriverWait(driver, 600).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="keywords"]')))
    buscador= driver.find_element(By.XPATH,'//*[@id="keywords"]')
    buscador.send_keys(rut)
    driver.find_element(By.XPATH,'//*[@id="contenedor"]/div[2]/div/div/div[2]/form/div/input[2]').click()
    WebDriverWait(driver, 600).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div/div[3]/div/div[2]/div[3]/div[3]/div/div[2]/div[2]/a')))
    driver.find_element(By.XPATH,'/html/body/div/div[3]/div/div[2]/div[3]/div[3]/div/div[2]/div[2]/a').click()
    WebDriverWait(driver, 600).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="results-content"]/tr[2]/td[1]/a/span')))
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 600).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="address"]')))
    elem=driver.find_element(By.XPATH,'//*[@id="address"]').text
    #rut_ar= pd.DataFrame.from_records([{'RUT':rut, 'Direccion':elem}])
    #list_rut.append(rut_ar)
    #driver.close()
    #driver.switch_to.window(driver.window_handles[0])
    #driver.get("https://www.genealog.cl/")
    
df_rut=pd.concat(list_rut,axis=0)
time_end=time.time()
print(time_end-time_start)
#driver.close()

