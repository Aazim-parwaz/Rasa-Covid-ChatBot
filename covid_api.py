import requests

def covid_data(city):

     url='https://api.rootnet.in/covid19-in/stats/history'

     data=requests.get(url).json()

     region=data["data"][len(data['data'])-1]["regional"]
     
     for stateObj in region:
          if stateObj["loc"]==city:
              print(city)
              return stateObj["totalConfirmed"]

     

# def covid_data_by_date():
# 	return 1




# def covid_data_by_city(city):
# 	return 1


print(covid_data("Jammu and Kashmir"))




