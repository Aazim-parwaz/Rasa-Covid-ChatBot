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
        print(tracker)
        covid_cases_type = tracker.get_slot('covid_cases_type')
       

        # set values for empty slots
        if covid_cases_type is None:
            covid_cases_type = -1

        
        # list possible cities     
        possible_cities=["Jammu and Kashmir","Maharashtra","Delhi","Ladakh","Punjab"]

        # Default answer if better answer cannot be found
        response="Sorry, got no idea - but I hope pandemic is near to an end! stay home stay safe till then!. "

        # read & parse the information and generate response
        if city in possible_cities:
            
            totalConfirmed_Current=covid_data(city)

           

            # answers to queries about current weather   

            response="Total Confirmed cases in {} is {}. ".format(city,totalConfirmed_Current) 
            

        # reponse for if city is not in range of supported cities
        else:
            response = "Sorry, currently I am limited to information from Delhi, Maharashtra and Jammu and Kashmir only."

        # send the response back to rasa
        dispatcher.utter_message(response)