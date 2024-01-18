import time
import undetected_chromedriver as uc
import pandas as pd
from src.data.extract.util.scrape_data import scrape_data

def get_data(start, finish):
    startTime = time.time()

    df = pd.DataFrame()
    driver = uc.Chrome()

    for page in range(start, finish):
        URL = "https://www.vivareal.com.br/venda/bahia/salvador/?pagina={0}".format(page)
        driver.get(URL)
        time.sleep(2)

        parsed_data = scrape_data(driver.page_source)
        
        df = pd.concat([df, pd.DataFrame(parsed_data)])
    
        print("Scraped page number {0}".format(page))

    driver.close()
    time.sleep(1)

    finishTime = time.time()
    duration = finishTime - startTime
    print("Finished web scraping in {0} seconds.".format(round(duration, 2)))

    return df


if __name__ == "__main__":
    data = get_data(1, 2)
    data.to_csv("./data/scraped_data.csv", index=False)
