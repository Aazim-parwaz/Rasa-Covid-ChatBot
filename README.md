# COVID-19 Chatbot with Rasa 2.0: open source conversational AI(currently migrating to Rasa 3.x)

## Table of Contents
1. [introduction](#introduction)
2. [COVID-19 data](#COVID-19_data)
3. [Conversational flow](#Conversation_Flow)
4. [Implementation](#Implementation)
5. [Installation](#Installation)
6. [References](#References)
## introduction
<a name="introduction"></a>

As natural language processing (NLP) technology and chatbot systems over the past few years have evolved quickly, also the usefulness of chatbots has increased. The motivation of chatbots is productivity; they have an instant access to information they refer to and are efficient in assisting users. (Brandtzaeg, 2017, *Why people use chatbots*. COVID-19 chatbot is an excellent use case example for the technology.

The content of a chatbot consists of the personality, conversation flows and the information it can deliver to the user. Personality is created by interactions and responses and by acting differently in different situations. These responses should be designed so that it maximises the engagement between the bot and the user (Katz, 2019, *The Ultimate Guide to chatbot personality*, Chatbots Magazine). The COVID-19 chatbot described here aims to use these principles, however due to the efforts required, in a rather minimalistic way leaving plenty of room for future improvements. e.g. in the area of how to handle chitchat.

## COVID-19 data
<a name="COVID-19_data"></a>
The COVID-19 data format chosen here is defined by (https://api.rootnet.in/covid19-in/stats/history), which provides COVID-19 data freely for developers. 

## Conversation Flow
<a name="Conversation_Flow"></a>
The conversation is initiated by the end-user. A greeting or a goodbye should reset any prior assumptions or knowledge collected by the bot during previous interactions. When time or COVID-19 detail are not contained in the query, the bot shall report the current and generic COVID-19 conditions. When the city is not provided in the query, the bot shall request for it. Any further specifics in the query should be answered in more detail if information is available. 




## Demonstration:<br>
 ### Sample Demonstration Images:<br>
 Chatbot's Intro Interface:<br>
<img src="https://user-images.githubusercontent.com/59523836/209435980-fd31fa24-82d5-4235-8dbc-96c034a0625d.png"></img><br>
 Chatbot's Chat Interface:<br>
<img src="https://user-images.githubusercontent.com/59523836/209436003-8f377aaf-f502-444b-9706-eda27508cc9f.png"></img><br>
 Chatbot's Tracker Interface:<br>
<img src="https://user-images.githubusercontent.com/59523836/209436020-a88e9660-59cc-40b9-a607-4d84367de6e6.png"></img><br>
Deployed Chatbot's Telegram interface:<br>
<img src="https://user-images.githubusercontent.com/59523836/209436030-9b391ae9-08e3-464c-acac-890b5efe3bae.png"></img><br>

 <br><br>
 
 
 
 
 
 ### Sample Demonstration Videos:<br>
 #### Working Of Chatbot In Local Server:<br>
 <img src="https://user-images.githubusercontent.com/59523836/209436111-7492f454-f90d-4ead-8102-b9a66b26ce09.webm"></img>
 
  #### Working Of Chatbot In Deployable Server:<br>
 <img src="https://user-images.githubusercontent.com/59523836/209436093-0a6fd620-c734-4864-aef9-f2fdd1cd1e4f.webm"></img>
<br>



## Implementation
<a name="Implementation"></a>
All components are defined to support the conversation flow . The end-user intents here are: **who_are_you, covid_in_city, covid_in_two_city, covid_in_period, covid_without_city, greet, goodbye, affirm, deny, mood_great, mood_unhappy, bot_challenge, how_are_you, capabilities**
In Rasa, the slots can be used for passing information to and back between Rasa and external actions. Three slots are required: **city,city2, init_date,final_date**.

The responses where the personality is also largely created are: **utter_greet, utter_goodbye, utter_ask city** (triggers city_form), **utter_iamabot, utter_capabilities, utter_im_well so on**. This also includes the external action, **action_covid**, which fetches the COVID-19 data, parses it and generates the COVID-19 response sentence.

External actions are user defined functions written in python. Only one action, **action_covid**, is required. It is split in two separate functionalities here: **actions.py** which receives slots: **city,city2,init_date and final_date** from Rasa. It then queries the COVID-19 data for specific city from **covid_api.py** where a function **covid_data(city,city2,init_data,final_data)** is defined. The function returns the COVID-19 data(totalcases) after getting filtered out from (https://api.rootnet.in/covid19-in/stats/history) onecall json format to **action_covid**, which then forms a response sentense to be passed back to Rasa.

The user intents, stories and rules are used for training the NLP model. These intent examples cover tens of different ways of asking questions, and explaining to the model how to find the values for the three slots and what is the intent the user has. The stories contain the conversation flows and rules that will stop any conversation and force a different path. 


## Installation
<a name="Installation"></a> 
Installation assumes existing installation of miniconda or anaconda. 
https://www.anaconda.com/

### pip3 & Rasa

Below are the simple steps for creating a virtual environment, install pip3 and Rasa Open Source 2.0.

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

There are additional actions that need to be started before starting the bot evaluation. These are in ```actions.py``` and ```covid_api.py``` files. To do so, run below commands on two different terminals: 

```
rasa run actions
```

Start the discussion with rasabot:

```
rasa shell
```



## References
<a name="References"></a>
    - Rasa. (n.d.). Rasa: Open source conversational AI. URL: https://rasa.com
    
    
