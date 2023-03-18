import tkinter
from tkinter import *
import wolframalpha
import wikipedia
from transformers import pipeline
from transformers import BertTokenizer,BertForQuestionAnswering




def chatbot() :
    
    try :
        #Try deeplearning model to Extract data from Context
        question = query_input.get()
        l1["text"] = "QUESTION :- " + question
        print(question)
        print(context)
        QA(question = question, context = context)
        answer = QA(question = question, context = context)["answer"]
        accuracy = QA(question = question, context = context)["score"]
        res = "result"
        
        #messagebox.showinfo(res,answer+"\nAccuracy:- "+accuracy)
        
    except : 
        #Try wikipedia for answer
        answer =  wikipedia.summary(query,sentences = 5)
        
        
    finally : 
        #If No answer is Found
        print("Sorry, I am unable to find the answer for you :(")
        
        
    
        
 

        
    
   