import time
import undetected_chromedriver as uc
import pandas as pd
from util.scrape_data import scrape_data

def get_data():
    df = pd.DataFrame()

    driver = uc.Chrome()

    for page in range(1, 10):
        URL = "https://www.vivareal.com.br/venda/bahia/salvador/?pagina={0}".format(page)
        driver.get(URL)
        time.sleep(2)

        parsed_data = scrape_data(driver.page_source)
        
        df = pd.concat([df, pd.DataFrame(parsed_data)])
    
    driver.close()
    time.sleep(1)
    return df


startTime = time.time()

data = get_data()
data.to_csv("./data/scraped_data.csv", encoding='utf-8')

finishTime = time.time()
duration = finishTime - startTime
print("Finished in {0} seconds.".format(duration))
