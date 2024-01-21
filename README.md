# Salvador Housing Price Predictor

## A Machine Learning API for prediction of housing prices in Salvador/Bahia 📈.

This is an educational personal project for Web Scraping and Machine Learning. All data was scraped from the [VivaReal](https://www.vivareal.com.br) website.

## Installation and usage:

### Makefile

If you have ```make``` installed, you can use ```make <target>``` for interaction with the app.

```make init``` creates the python virtual environment and installs dependencies;

```make load_data``` runs the data Scraping/Cleaning pipeline;

```make train_xgb``` trains and pickles a XGBoost model for the API;

```make app``` runs the API locally;

```make app_dev``` runs the API locally on development mode (auto reload).


Alternatively, you can run the commands manually:

### 1. Set virtual environment

Set a Python Virtual Environment. You may use ```python3 -m venv .venv``` on your terminal inside the project folder or any other method you prefer. 

With your venv created, activate it with ```source .venv/Scripts/activate``` on Windows or ```source .venv/bin/activate``` on Linux/Mac.

### 2. Install dependencies

Install the dependencies with ```pip install -r requirements.txt```.

### 3. Run API

To run the server locally, run ```uvicorn app:app``` on the terminal.

And voila, the server will be running on ```http://127.0.0.1:8000/``` and you can check the docs on ```http://127.0.0.1:8000/docs```.

## Tools used ⚙️:

- [Selenium](https://www.selenium.dev/) and [undetected_chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/)
- [Scikit-learn](https://scikit-learn.org/stable/)
- [FastAPI](https://fastapi.tiangolo.com/)
