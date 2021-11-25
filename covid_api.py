import requests

def covid_data(city,city2,init_date,final_date):

     url='https://api.rootnet.in/covid19-in/stats/history'

     data=requests.get(url).json()
     # current data of a city
     if city2 is None  and init_date is None and final_date is None:

          lastOriginUpdate=data["lastOriginUpdate"]
          #print(lastOriginUpdate)
          current_date=lastOriginUpdate[0:lastOriginUpdate.find('T')]
          #print(current_date)
          data=data['data']
          

          region=[]
          for day in data:
               if current_date ==day['day']:
                    region=day['regional']
                    #print(region)

          for state in region:
               if state['loc']==city:
                    return state['totalConfirmed']
                    

            
            
       
        # current total of two cities/states ex. Delhi and Maharashtra   
     elif  city is not None and city2 is not None and init_date is None and final_date is None:

          lastOriginUpdate=data["lastOriginUpdate"]
          current_date=lastOriginUpdate[0:lastOriginUpdate.find('T')]
          data=data['data']
          region=[]
          for day in data:
               if current_date ==day['day']:
                    region=day['regional']
          total=0
          for state in region:
               if state['loc']==city or state['loc']==city2:
                    print(state['loc'],state['totalConfirmed'])
                    total+= state['totalConfirmed']

          return total

       # for city and city2 current data
     elif city is None and city2 is None and init_date is not None and final_date is not None:

          data=data['data']
          data_init=0
          data_final=0
          for date in data:
               if init_date ==date['day']:
                     data_init=date['summary']["total"]
               elif final_date==date['day']:
                     data_final=date['summary']['total']

          return data_final-data_init


            
       
            

     

# def covid_data_by_date():
# 	return 1




# def covid_data_by_city(city):
# 	return 1







