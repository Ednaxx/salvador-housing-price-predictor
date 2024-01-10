from bs4 import BeautifulSoup

def scrape_data(data):
    parsed_data = {
        "addresses": [],
        "titles": [],
        "areas": [],
        "bedrooms": [],
        "bathrooms": [],
        "parkingSpots": [],
        "prices": []
    }

    soup = BeautifulSoup(data, "html.parser")
    
    cards = soup.find_all('div', attrs={"data-type": "property"})
    
    for card in cards:
        try:
            address = card.find('span', class_="property-card__address").text
        except:
            address = ""
        
        try:
            title = card.find('span', class_="property-card__title").text
        except:
            title = ""

        try:
            area = card.find('span', class_="property-card__detail-area").text
        except:
            area = ""

        try:
            bedrooms = card.find('li', class_="property-card__detail-room").find('span', class_="property-card__detail-value").text
        except:
            bedrooms = ""

        try:
            bathrooms = card.find('li', class_="property-card__detail-bathroom").find('span', class_="property-card__detail-value").text
        except:
            bathrooms = ""

        try:
            parkingSpots = card.find('li', class_="property-card__detail-garage").find('span', class_="property-card__detail-value").text
        except:
            parkingSpots = ""

        try:
            prices = card.find('div', class_="property-card__price").find('p').text
        except:
            prices = ""
        
        parsed_data["addresses"].append(address)
        parsed_data["titles"].append(title)
        parsed_data["areas"].append(area)
        parsed_data["bedrooms"].append(bedrooms)
        parsed_data["bathrooms"].append(bathrooms)
        parsed_data["parkingSpots"].append(parkingSpots)
        parsed_data["prices"].append(prices)

    return parsed_data