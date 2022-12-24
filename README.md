# COVID-19 Chatbot with Rasa 2.0: open source conversational AI(currently migrating to Rasa 3.x)

## Table of Contents
1. [introduction](#introduction)
2. [COVID-19 data](#COVID-19_data)
3. [Conversational flow](#Conversation_Flow)
4. [Demonstration](#demo)
5. [Implementation](#Implementation)
6. [Installation](#Installation)
7. [References](#References)
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




## Demonstration:
<a name="demo"></a>
<br>
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
 #### Starting Of Chatbot In Local Server:<br>
 [start_shell.webm](https://user-images.githubusercontent.com/59523836/209438734-f42a78ff-b1ec-466b-a543-36f2f885f846.webm)


#### Demo Of Chatbot In Local Server:<br>
 [demo_shell_interface.webm](https://user-images.githubusercontent.com/59523836/209438786-c921d3cb-b48a-4e1b-aaf5-798119b2f324.webm)


#### Starting Chatbot In Deployable Server:<br>


[starting_deployment_env.webm](https://user-images.githubusercontent.com/59523836/209439046-56a9e5fd-9d2f-4862-8417-cb73c9c69b2d.webm)


  #### Working Of Chatbot In Deployable Server:<br>
  [telegram_demo.webm](https://user-images.githubusercontent.com/59523836/209439104-eed7b7bc-e086-488a-bae0-dfee8e84f55e.webm)

 



## Implementation
<a name="Implementation"></a>


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
    
    
