import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import json
import numpy as np
import re
import random_responses
import random
import tensorflow as tf
#import tensorflow_hub as hub
import tensorflow_text as text
#from IPython.display import display

dataset_name = 'imdb'
saved_model_path = './{}_bert'.format(dataset_name.replace('/', '_'))
reloaded_model = tf.saved_model.load(saved_model_path)

# BERT model (returns positiveness from 0 to 1)
def positive_classifier(input):
    # Works for a single string (sentence) input
        p_score = np.array(tf.sigmoid(reloaded_model(tf.constant([input]))))[0][0] 
        return p_score

# Load JSON data 
def load_json(file):
    with open(file) as bot_responses:
        return json.load(bot_responses)


# Store JSON data
response_data = load_json("bot.json")

# Cleaning name
def username_clean(input):
    username = input.lower()
    list_words_strip = ["i am", "i'm", "my", "name", "this", "is", "hi", "hello", "hey", "how", "are", "you", "it's", ",", ".", "?", "!"]
    for word in list_words_strip:
        username = username.replace(word, "")
    username = username.strip()
    username = username.capitalize()
    return username

# Greeting output
def greeting(input):
    return "Nice to meet you " + input + ". How can I help you today?"

# Get the response of the bot
def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []

    # Check all the responses
    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

        # Check if there are any required words
        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1

        # Amount of required words should match the required score
        if required_score == len(required_words):
            # print(required_score == len(required_words))
            # Check each word the user has typed
            for word in split_message:
                # If the word is in the response, add to the score
                if word in response["user_input"]:
                    response_score += 1

        # Add score to list
        score_list.append(response_score)
        # Debugging: Find the best phrase
        # print(response_score, response["user_input"])

    # Find the best response and return it if they're not all 0
    best_response = max(score_list)
    response_index = score_list.index(best_response)

    # Check if input is empty
    if input_string == "":
        return "Please type something so we can chat :("
    	
    # Main bot response
    if best_response != 0:
        resp_len = len(response_data[response_index]["bot_response"])
        if resp_len == 1:
            return response_data[response_index]["bot_response"][0]
        else:
            return response_data[response_index]["bot_response"][random.randint(0,(resp_len-1))]

    # If there is no good response, return a random one.
    return random_responses.random_string()

# MAIN BODY
#print("Nump·E: Hello human! This is Nump·E, your virtual assistant. Could you please tell me your name?")
#username = input("You: ")
#username = clean_name(username)
#print("Nump·E: Nice to meet you " + username + ". How can I help you today?")
#input_history = []
#pos_score_history = []

#while True:
    #user_input = input("You: ")
    #pos_score = positive_classifier(user_input)
    
    #if pos_score < 0.05:
        #print("I am so sorry that you had such a bad experience with us, please, let me contact with an agent that will have a tailored solution for you!")
    #elif pos_score > 0.85:
        #print("I am very glad that you had a great experience with us, if you have a moment please rate our app on the AppStore or Google Play! ")
    #else:
        #print("Nump·E:", get_response(user_input))
    #input_history.append(user_input)
    #pos_score_history.append(pos_score)
    
    #if user_input == 'break':
        #display(pd.DataFrame(input_history, pos_score_history).T)
        #break


    #count_variable = 0
    #userText = request.args.get('msg')
    #while True:
        #if count_variable == 0:
            #count_variable += 1
            #username = main.clean_name(userText)
            #return str("Nice to meet you " + username + ". How can I help you today?")
        #elif count_variable == 1:
            #count_variable += 1
            #return str(main.get_response(userText))
        #elif count_variable == 2:
            #return str()