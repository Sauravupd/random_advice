import tkinter as tk
import requests
HEIGHT = 700
WIDTH = 500
root=tk.Tk()
def get_advice():
    response=requests.get('https://api.adviceslip.com/advice')
    advice_json=response.json()
    advice= (advice_json['slip']['advice'])
    label['text']=advice
canvas=tk.Canvas(root,height=HEIGHT,width=700)
canvas.pack()
background_image=tk.PhotoImage(file='./Image/07.PNG')
background_label=tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

frame1=tk.Frame(root,bg='#668bcc',bd=2)
frame1.place(relx=0.15,rely=0.1,relwidth=0.7,relheight=0.05)
button=tk.Button(frame1,text="Generate Advice",bg="white",fg="black",font=10,bd=2,command=lambda:get_advice())
button.place(relx=0.1,rely=0.22,relwidth=0.8,relheight=0.6)
# entry1=tk.Entry(frame1,bg="white",text="this is an entry",font=10)
# entry1.place(relx=0.01,rely=0.1,relwidth=0.7,relheight=0.8)
frame2=tk.Frame(root,bg='#668bcc',bd=2)
frame2.place(relx=0.15,rely=0.2,relwidth=0.7,relheight=0.6)
label=tk.Label(frame2,bg="white",text="",justify='center',wraplength=100)
label.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.9)
root.mainloop()