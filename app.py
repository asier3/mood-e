from asyncio import start_server
from flask import Flask, render_template, request, redirect, url_for
from main import username_clean, greeting, get_response, positive_classifier
import numpy as np
import pandas as pd
from datetime import datetime
import time
from time import strftime
from time import gmtime

app = Flask(__name__)
counter = 0
input_history = []
output_history = []
pos_score_history = []
time_history = []
username = ''

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/chat")
def chat():
    global start
    start = time.time()
    return render_template("index.html")

@app.route("/get")
def get_bot_response():

    global counter
    global input_history
    global output_history
    global pos_score_history
    global username
    global time_history

    counter += 1 
    time_history.append(str(datetime.now())[11:19])

    if counter == 1:
        userText = request.args.get('msg')
        username = username_clean(userText)
        return str(greeting(username))

    else:
        userText = request.args.get('msg')
        input_history.append(userText)
        pos_score_history.append(round(positive_classifier(userText),2))
        if positive_classifier(userText) < 0.1:
            output_history.append("I'm sorry, I have been programmed to give the best customer service but seems that I failed.")
            return str("I'm sorry, I have been programmed to give the best customer service but seems that I failed. Would you like to be attended by one of our agents? - Type 'agent' to be transferred")
        else:
            bot_response = get_response(userText)
            output_history.append(bot_response)
            return str(bot_response)

@app.route("/endpage")
def endpage():
    global end
    end = time.time()
    return render_template("endpage.html")

@app.route("/stats")
def stats():

    time_history.pop()
    customer_history_df = pd.DataFrame(np.array([time_history, input_history, output_history, pos_score_history]).T, columns=['time','customer inputs','bot response','sentiment score'])
    filename = (str(datetime.now())[:10] + '-' + str(datetime.now())[11:13] + '-' + str(datetime.now())[14:16]).replace('-','')
    customer_history_df.to_csv(f'customer_history/{filename}_{username}.csv', index=False)
    table_json = customer_history_df.to_html(index=False)
    avgpos = round(np.mean(pos_score_history), 2)
    total_time = end - start
    total_time = strftime("%H:%M:%S", gmtime(total_time))
    messages = len(input_history)
    return render_template("stats.html", table =table_json, averagepos = avgpos, time = total_time, messages = messages)



if __name__ == "__main__":
    app.run()