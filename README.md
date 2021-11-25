# COVID-19 Chatbot with Rasa 2.0: open source conversational AI

## introduction

As natural language processing (NLP) technology and chatbot systems over the past few years have evolved quickly, also the usefulness of chatbots has increased. The motivation of chatbots is productivity; they have an instant access to information they refer to and are efficient in assisting users. (Brandtzaeg, 2017, *Why people use chatbots*). COVID-19 chatbot is an excellent use case example for the technology.

The content of a chatbot consists of the personality, conversation flows and the information it can deliver to the user. Personality is created by interactions and responses and by acting differently in different situations. These responses should be designed so that it maximises the engagement between the bot and the user (Katz, 2019, *The Ultimate Guide to chatbot personality*, Chatbots Magazine). The COVID-19 chatbot described here aims to use these principles, however due to the efforts required, in a rather minimalistic way leaving plenty of room for future improvements. e.g. in the area of how to handle chitchat.

## COVID-19 data

The COVID-19 data format chosen here is defined by (https://api.rootnet.in/covid19-in/stats/history), which provides COVID-19 data freely for developers. Delhi, Maharashtra, and Jammu and Kashmir data are prefetched for testing purposes, if API use is not wanted for some reason. 


## Conversation Flow

The conversation is initiated by the end-user. A greeting or a goodbye should reset any prior assumptions or knowledge collected by the bot during previous interactions. When time or COVID-19 detail are not contained in the query, the bot shall report the current and generic COVID-19 conditions. When the city is not provided in the query, the bot shall request for it. Any further specifics in the query should be answered in more detail if information is available. 



## Implementation

All components are defined to support the conversation flow . The end-user intents here are: **greet, goodbye, covid_in_city, covid_without_city, capabilities, how_are_you and who_are_you so on**.

In Rasa, the slots can be used for passing information to and back between Rasa and external actions. Three slots are required: **covid_cases_type, city, date**.

The responses where the personality is also largely created are: **utter_greet, utter_goodbye, utter_ask city** (triggers city_form), **utter_iamabot, utter_capabilities, utter_im_well so on**. This also includes the external action, **action_covid**, which fetches the COVID-19 data, parses it and generates the COVID-19 response sentence.

External actions are user defined functions written in python. Only one action, **action_covid**, is required. It is split in two separate functionalities here: **actions.py** which receives slots: **covid_cases_type, city & date** from Rasa. It then queries the COVID-19 data for specific city from **covid_api.py** where a function **covid_data(city)** is defined. The function returns the COVID-19 data for a specific city in (https://api.rootnet.in/covid19-in/stats/history) onecall json format to **action_covid**, which then parses it and forms a response sentense to be passed back to Rasa.

The user intents, stories and rules are used for training the NLP model. These intent examples cover tens of different ways of asking questions, and explaining to the model how to find the values for the three slots and what is the intent the user has. The stories contain the conversation flows and rules that will stop any conversation and force a different path. 


## Installation
 
Installation assumes existing installation of miniconda or anaconda. 
https://www.anaconda.com/

### pip & Rasa

Below are the simple steps for creating a virtual environment, install pip and Rasa Open Source 2.0.

```
conda create -n RasaEnv python=3.7.6 
conda activate RasaEnv
conda install -c anaconda pip3
pip3 install rasa==2.8.11  
```
In case of issue, please refer to Rasa Open Source installation pages: 
https://rasa.com/docs/rasa/installation/

### Creating and initialising a new project:

```p
mkdir rasa
cd rasa
rasa init --no-prompt
```
This will create a new directlry, under which rasa creates all necessary directories and files.

Replace all files in the rasa directory with the files in the project.

## Train the model and run the bot

Train the model with command 

```
rasa train
```

There are additional actions that need to be started before starting the bot evaluation. These are in ```actions.py``` and ```covid_api.py``` files. 

```
rasa run actions
```

Start the discussion with rasabot:

```
rasa shell
```



## References

    - Rasa. (n.d.). Rasa: Open source conversational AI. URL: https://rasa.com
    
    