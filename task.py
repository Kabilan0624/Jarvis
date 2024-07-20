
import requests

def temp_room(room):
    result = " Temp = 20,Humadity= 70"
    return result

def temp_city(city):
    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q":"53.1,-0.13"}

    headers = {
	    "X-RapidAPI-Key": "c32615b66cmsh4f1642869fcc6cbp11ddc9jsn5a9290a4ba18",
	    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())
    d1=response.json()
    print(d1)
    d2=d1.get("current_observation")
    hum=d1.get('atmosphere').get('humidity')
    temp=d1.get('condtion').get('temperature')
    temp=round((temp-32)*5/9,2)
    return(f"Humidity:{hum}, Temp in c :{temp}")

definitions = [{"name":"temp_city",
                "description":"find weather,temperature of city",
                "parameters":{"type":"object",
                              "properties":{
                                  "city":{
                                      "type":"string","description":"city to find weather"}}}}]


definitions = [{"name":"temp_room",
                "description":"find weather,temperature of room or my home",
                "parameters":{"type":"object",
                              "properties":{
                                  "room":{
                                      "type":"string","description":"room to find weather"}}}}]


if __name__ == "__main__":
    print(temp_city("Delhi"))
