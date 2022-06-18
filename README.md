This is the final project for the Ironhack Data Analytics Bootcamp, in which we showcase what we learned
through the course and what we are capable of.

I decided to create a chatbot that can detect sentiment on text, allowing companies and businesses
to give a better-automatized customer service. The model used to detect sentiment was a BERT model 
pre-trained to detect sentiment and fine-tuned with an IMDB database with 50,000 reviews tagged as 
positive or negative (link below). The model can detect the sentiment on a text from 0 (most negative) 
to 1 (most positive). 

The chatbot stores the history of the conversation into a separate CSV file and calculates: the conversation time, the average sentiment score of the whole conversation, and the number of messages sent by the customer. It also plots the sentiment scores against time in order to show the evolution of the mood of the customer throughout the conversation.

The chatbot has been developed in python and implemented into HTML with flask.

DEMO VIDEO: https://www.youtube.com/watch?v=WY8RsDuDVp0&t

The steps I followed to complete this project were:

1 - Create a basic chatbot and train it to answer specific queries (in this case a flight cancellation).

2 - Download a BERT pre-trained model to detect sentiment and fine-tune it with the IMDB review database.
(BERT sentiment model: https://colab.research.google.com/drive/1heHu8DA1Cp385ZQta6_T9CVnK1qOYext)
(IMDB review database: https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)

3 - Merge the chatbot and BERT model into python and create the functions that will allow storing the history of the conversation
and other stats.

4 - Create the web app with flask and HTML files to shape and style the web app.

This chatbot can be the perfect tool for companies that want to automatize their customer services without losing
the quality of the service given. The sentiment model can be trained with past data in order to make it more accurate
as well as the chatbot. In addition, all the data collected will help to get useful insights for the company, the better
you know your customers, the better you will serve them!

Check my Portfolio for more info!
https://troopl.com/asierodriguez/moode

You can also check my Linkedin
https://www.linkedin.com/in/asierodriguez/
