from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.genealog.cl/")
ruts=['92580000-7','90413000-1','76.102.960-6','76124890-1','96.799.250-K','77013680-6']
df_rut=pd.DataFrame()
list_rut=[]
time_start=time.time()

for rut in (ruts):
    WebDriverWait(driver, 600).until(EC.visibility_of_element_located((By.ID,'s')))
    buscador= driver.find_element(By.ID,'s')
    buscador.send_keys(rut)
    driver.find_element(By.CLASS_NAME,'material-icons').click()
    WebDriverWait(driver, 600).until(EC.visibility_of_element_located((By.CLASS_NAME,'material-icons')))
    driver.find_element(By.XPATH,'//*[@id="results-content"]/tr[2]/td[1]/a/span').click()
    WebDriverWait(driver, 600).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="results-content"]/tr[2]/td[1]/a/span')))
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 600).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="results-container"]/div[1]/div/table[2]/tbody/tr[1]/td[2]')))
    elem=driver.find_element(By.XPATH,'//*[@id="results-container"]/div[1]/div/table[2]/tbody/tr[1]/td[2]').text
    rut_ar= pd.DataFrame.from_records([{'RUT':rut, 'Direccion':elem}])
    list_rut.append(rut_ar)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.get("https://www.genealog.cl/")
    
df_rut=pd.concat(list_rut,axis=0)
time_end=time.time()
print(time_end-time_start)
driver.close()

