# Salvador Housing Price Predictor

## A Machine Learning API for prediction of housing prices in Salvador/Bahia 📈.

This is an educational personal project for Web Scraping and Machine Learning. All data was scraped from the [VivaReal](https://www.vivareal.com.br) website.

## Model features:

```areas``` Total interior habitable area in ***m<sup>2</sup>***;

```bedrooms``` Total amount of bedrooms. When scraped data contained intervals (e.g. "2-4"), the mean was used, so this feature is of ***float*** type;

```bathrooms``` Total amount of bathrooms. When scraped data contained intervals (e.g. "2-4"), the mean was used, so this feature is of ***float*** type;

```parkingSpots``` Total amount of parking spots. When scraped data contained intervals (e.g. "2-4"), the mean was used, so this feature is of ***float*** type;

```type``` housing type. Can only be ***"apartment"*** or ***"house"***;

```neighborhood``` neighborhood in Salvador/Bahia in which the housing is located;

```neighborhood_area_price``` value defined by calculating:

 ***(sum of neighborhood's house prices) / (sum of neighborhood's house areas)*** if the type is ***"house"*** or
 
  ***(sum of neighborhood's apartment prices) / (sum of neighborhood's apartment areas)*** if the type is ***"apartment"***;

```prices``` housing price in ***BRL***;

## Installation and usage:

### Makefile

If you have ```make``` installed, you can use ```make <target>``` for interaction with the app.

```make init``` creates the python virtual environment and installs dependencies;

```make load_data``` runs the data Scraping/Cleaning pipeline;

```make train_xgb``` trains and pickles a XGBoost model for the API;

```make app``` runs the API locally and ```make app_dev``` runs it on development mode (auto reload).
 The server will be running on ```http://127.0.0.1:8000/``` and you can check the docs on ```http://127.0.0.1:8000/docs```.

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
