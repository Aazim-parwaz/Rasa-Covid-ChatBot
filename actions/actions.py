# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# load some libraries
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from covid_api import covid_data


class Covid(Action):

    def name(self) -> Text:
        return "action_covid"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # get the current slot values from rasa
        city = tracker.get_slot('city')
        city2= tracker.get_slot('city2')
        init_date= tracker.get_slot('init_date')
        final_date= tracker.get_slot('final_date')
        response="Sorry, got no idea - but I hope pandemic is near to an end! stay home stay safe till then!. "
        # confirmed or non-confirmed
        covid_cases_type = tracker.get_slot('covid_cases_type')
       

        # set values for empty slots
        # if covid_cases_type is None:
        #     covid_cases_type = -1
        # current data of a city
        if city2 is None  and init_date is None and final_date is None:
            
            totalConfirmed=covid_data(city,city2,init_date,final_date) 
            #answers to the query
            if totalConfirmed is not None:
                response="Total Confirmed cases in {} is {}. ".format(city,totalConfirmed) 
       
        # current total of two cities/states ex. Delhi and Maharashtra   
        elif city is not None and city2 is not None and init_date is None and final_date is None::

            totalConfirmed=covid_data(city,city2,init_date,final_date)
            #answers to the query
            if totalConfirmed is not None:
                 response="Total Confirmed cases of {} and {} altogether is {}".format(city,city2,totalConfirmed)

        # for cases between date to date2
        elif city is None and city2 is None and init_date is not None and final_date is not None:

            totalConfirmed=covid_data(city,city2,init_date,final_date)
            #answers to the query
            if totalConfirmed is not None:
                response="Confirmed case count from {} to {} is {}".format(init_date,final_date,totalConfirmed)
       
            

        
            
        # send the response back to rasa
        dispatcher.utter_message(response)