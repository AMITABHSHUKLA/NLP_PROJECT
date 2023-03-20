import tkinter
from tkinter import *
from tkinter import messagebox
import wikipedia
import transformers
from transformers import pipeline
from transformers import BertTokenizer,BertForQuestionAnswering


model_name = "deepset/bert-base-cased-squad2"
tokenizer_A = BertTokenizer.from_pretrained(model_name)
qa_model = BertForQuestionAnswering.from_pretrained(model_name)
QA = pipeline("question-answering" , model = qa_model, tokenizer = tokenizer_A)

def chatbot() :
    
    try :
        qes = query_input.get()
        l1["text"] = "QUESTION :- " + qes
        print(qes)
        print(context)
        QA(question = qes, context = context)
        answer = str(QA(question = qes, context = context)["answer"])
        accuracy = str(QA(question = qes, context = context)["score"])
        print(answer)
        
        result = "result"
        
        messagebox.showinfo(result,answer+"\nAccuracy:- "+accuracy)
        
    except : 
        answer =  wikipedia.summary(qes,sentences = 5)
        messagebox.showinfo("Answer",answer)
        
    finally : 
        l_a["text"] = "Answer :- " + answer


def showcontext():
    global context
    context = context_input.get()
    l2["text"] = context
    
    

root = Tk()
root.geometry("1200x600")
root.config(bg="Grey")
root.title("CHATBOT")
root_label = Label(root, text = "CHATBOT",bg="BLACK",fg = "white",
                   padx=10,pady=10,borderwidth=7,
                   relief = RAISED,font='Helvetica 10 bold')
root_label.pack()



fc = Frame(root,bg="orange",borderwidth=7,relief=FLAT)
fc.pack(side=LEFT,fill = "y")
fc_label = Label(fc,text ="CONTEXT",bg = "orange", font = "Helvetica 16 bold" )
fc_label.pack(side = TOP)
f2 = LabelFrame(fc,bg= "white")
f2.pack()
l2 = Label(f2,bg="grey",fg = "black",font= "Helvetica 14 bold",wraplength= 900)
l2.pack()

fq = Frame(root,bg="sky blue",borderwidth=7,relief=FLAT)
fq.pack(side=LEFT,fill = "y")
fq_label = Label(fq,text ="QUESTION",bg = "sky blue",fg = "black", font = "Helvetica 16 bold" )
fq_label.pack(side = TOP)
f1 = LabelFrame(fq,bg= "white")
f1.pack()
l1 = Label(f1,bg="sky blue",fg = "black",font= "Helvetica 14 bold",wraplength= 900)
l1.pack()
f_a = LabelFrame(fq,bg= "white")
f_a.pack()
l_a = Label(f_a,bg="sky blue",fg = "black",font= "Helvetica 14 bold",wraplength= 400)
l_a.pack()
#takes input
#
btn = Button(fq,text = "ENTER",bg="white",fg='black',padx=4,pady=4,borderwidth=6,command = chatbot)
             
btn.pack(side = BOTTOM)

query_input = Entry(fq,width=125)
query_input.pack(ipady=6,pady=(1,15),side = BOTTOM)
#---------------------------------------------------------------------------------#
btn2 = Button(fc,text = "ENTER",bg="white",fg='black',padx=4,pady=4,borderwidth=6,command = showcontext
             )
btn2.pack(side = BOTTOM)

context_input = Entry(fc,width=125)
context_input.pack(ipady=6,pady=(1,15),side = BOTTOM)

root.mainloop()
