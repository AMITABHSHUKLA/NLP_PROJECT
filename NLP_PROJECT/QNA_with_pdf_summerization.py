import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tkinter import messagebox
import wikipedia
import transformers
from transformers import pipeline
from transformers import BertTokenizer,BertForQuestionAnswering
import PyPDF2
from PyPDF2 import PdfReader



QA = pipeline("question-answering" )

def chatbot() :
    
    try :
        question = query_input.get()
        l1["text"] = "QUESTION :- " + question
        print(question)
        QA(question = question, context = context)
        answer = str(QA(question = question, context = context)["answer"])
        accuracy = str(QA(question = question, context = context)["score"])
        result = "result"
        print(answer)
        
        messagebox.showinfo(result,answer+"\n Accuracy:- "+accuracy)
        

    except : 
        answer =  wikipedia.summary(question,sentences = 5)
        wiki = "wiki"
        messagebox.showinfo(wiki,answer)
        

    finally : 
        l_a["text"] = "Answer :- " + answer
        #messagebox.showinfo("Thanks","Hope You got your answer Thank You!")

     
def pdf_to_text():
    global a_input
    global name
    file_location = filedialog.askopenfilename(title = "Select image")
    name = filedialog.asksaveasfilename()
    
    name = name.replace("/","//" )
    #print(name)
    
    page = Tk()
    page.geometry("200x300")
    page.config(bg="blue")
    page.title("page no.")
    page_label = Label(page, text = "PAGE NUMBER",bg="BLACK",fg = "white",
                       padx=10,pady=10,borderwidth=7,
                       relief = RAISED,font='Helvetica 10 bold')
    page_label.pack()
    a_input = Entry(page,width=125)
    a_input.pack(ipady=6,pady=(1,15),side = BOTTOM)
    bat = Button(page,text = "ENTER",bg="white",fg='black',padx=4,pady=4,borderwidth=6,command= txt_file)
             
    bat.pack(side = BOTTOM)
    
    page.mainloop()
    
#---------------------------------------------------------------------------
def txt_file() :
    
    pa = int(a_input.get())
    print(pa)
    
    reader = PdfReader(name)
    page = reader.pages[pa]
    a = page.extract_text()

    with open("text.txt","w") as t :
        t.write(a)
    
    with open("text.txt","r") as file :
        content = file.read()
        with open("text.txt","w") as txt :
            for line in content:
                m = line.replace(" ","")
                txt.write(m)
            

    
        
def summary():
    with open("text.txt","r") as f :
        text_pdf = f.read()
    summary_extraction = pipeline("summarization")
    summary = summary_extraction(text_pdf,max_length = 400,min_length = 200,do_sample = False)
    print(summary)
    messagebox.showinfo("Result",summary)


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


#-------------------------FRAME FOR CONTEXT-----------------------------------#
fc = Frame(root,bg="orange",borderwidth=7,relief=FLAT)
fc.pack(side=LEFT,fill = "y")
fc_label = Label(fc,text ="CONTEXT",bg = "orange", font = "Helvetica 16 bold" )
fc_label.pack(side = TOP)
f2 = LabelFrame(fc,bg= "white")
f2.pack()
l2 = Label(f2,bg="grey",fg = "black",font= "Helvetica 14 bold",wraplength= 900)
l2.pack()
btnp = Button(fc,text = "UPLOAD PDF",bg="white",fg='black',padx=4,pady=4,borderwidth=6,command = pdf_to_text)
             
btnp.pack(side = RIGHT)

#-----------------FRAME FOR QUESTION-------------------------------------------#
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
btns = Button(fq,text = "Get Summary",bg="white",fg='black',padx=4,pady=4,borderwidth=6,command = summary)
             
btns.pack(side = LEFT)

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