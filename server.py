from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import socket
import threading
import time
timeout = 20
timeout_start = time.time()
root = Tk()
root.title("Server")
root.geometry('600x600')
def start_thread(target):
    thread = threading.Thread(target=target)
    thread.daemon = True
    thread.start()

  
HOST = '127.0.0.1' 
PORT = 65432
connection_established = False 

conn,addr = None,None
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT)) 
s.listen(1)

def receive_data():
    
    while True:
        data = conn.recv(1024).decode()
        print('decoded is ',data)
        if data == 'button':
            labels.config(text="My Turn or X's Turn") 
            b1.config(text='O')
            for w in New.winfo_children():
                w.configure(state="normal")
            b1.config(state="disabled")
            
            
            
        elif data == 'button2' :    
            labels.config(text="My Turn or X's Turn") 
            b2.config(text='O')
            for w in New.winfo_children():
                w.configure(state="normal")
            b2.config(state="disabled")
            
            
        elif data == 'button3' :  
            labels.config(text="My Turn or X's Turn")   
            b3.config(text='O')
            for w in New.winfo_children():
                w.configure(state="normal")
            b3.config(state="disabled")
            
            
        elif data == 'button4' :    
            labels.config(text="My Turn or X's Turn") 
            b4.config(text='O')
            for w in New.winfo_children():
                w.configure(state="normal")
            b4.config(state="disabled")
            
              
        elif data == 'button5' :    
            labels.config(text="My Turn or X's Turn") 
            b5.config(text='O')
            for w in New.winfo_children():
                w.configure(state="normal")
            b5.config(state="disabled")
            
            
        elif data == 'button6' :    
            labels.config(text="My Turn or X's Turn") 
            b6.config(text='O')
            for w in New.winfo_children():
                w.configure(state="normal")
            b6.config(state="disabled")
            
               
        elif data == 'button7' :    
           labels.config(text="My Turn or X's Turn") 
           b7.config(text='O')
           for w in New.winfo_children():
                w.configure(state="normal")
           b7.config(state="disabled")
           
           
        elif data == 'button8' :
            labels.config(text="My Turn or X's Turn")     
            b8.config(text='O')
            for w in New.winfo_children():
                w.configure(state="normal")
            b8.config(state="disabled")
              
              
        elif data == 'button9' :    
            labels.config(text="My Turn or X's Turn") 
            b9.config(text='O')
            for w in New.winfo_children():
                w.configure(state="normal")
            b9.config(state="disabled")
            
            

def wait_for_connection():
    global connection_established,conn,addr
    conn,addr = s.accept()
    print('connected')
    connection_established = True 
    receive_data()


start_thread(wait_for_connection)   

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection

image = Image.open('C:\\Users\\jainh\\Downloads\\Tic-tac-toe1.png')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)

root.after(5000, lambda: root.destroy()) # Destroy the widget after 30 seconds
root.mainloop()

New = Tk()
New.title('Server')
New.iconbitmap('C:/Users/jainh/Downloads/Tic-tac-toe1.png')

clicked = 'X'


def checkwin():
    global winner
    winner = False
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg='green')
        b2.config(bg='green')
        b3.config(bg='green')
        winner = True
        for w in New.winfo_children():
            w.configure(state="disabled")
        messagebox.showinfo("Winner","Congo!!!!!!!X Wins!!!!!!!!")
    
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg='green')
        b5.config(bg='green')
        b6.config(bg='green')
        winner = True
        for w in New.winfo_children():
            w.configure(state="disabled")
            
        messagebox.showinfo("Winner","Congo!!!!!!!X Wins!!!!!!!!")  
            
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg='green')
        b8.config(bg='green')
        b9.config(bg='green')
        winner = True
        for w in New.winfo_children():
            w.configure(state="disabled")
            
        messagebox.showinfo("Winner","Congo!!!!!!!X Wins!!!!!!!!")
            
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg='green')
        b4.config(bg='green')
        b7.config(bg='green')
        winner = True
        for w in New.winfo_children():
            w.configure(state="disabled")
            
        messagebox.showinfo("Winner","Congo!!!!!!!X Wins!!!!!!!!")
            
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg='green')
        b5.config(bg='green')
        b8.config(bg='green')
        winner = True
        for w in New.winfo_children():
            w.configure(state="disabled")
            
        messagebox.showinfo("Winner","Congo!!!!!!!X Wins!!!!!!!!") 
                                   
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg='green')
        b6.config(bg='green')
        b9.config(bg='green')
        winner = True
        messagebox.showinfo("Winner","Congo!!!!!!!X Wins!!!!!!!!")
        for w in New.winfo_children():
            w.configure(state="disabled")
            
        messagebox.showinfo("Winner","Congo!!!!!!!X Wins!!!!!!!!")
            
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg='green')
        b5.config(bg='green')
        b9.config(bg='green')
        winner = True
        for w in New.winfo_children():
            w.configure(state="disabled")
            
        messagebox.showinfo("Winner","Congo!!!!!!!X Wins!!!!!!!!")
            
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg='green')
        b5.config(bg='green')
        b7.config(bg='green')
        winner = True
        for w in New.winfo_children():
            w.configure(state="disabled")
            
        messagebox.showinfo("Winner","Congo!!!!!!!X Wins!!!!!!!!")        
            
          ###################################
            
  
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg='green')
        b2.config(bg='green')
        b3.config(bg='green')
        winner = True
        for w in New.winfo_children():
            w.configure(state="disabled")
            
        messagebox.showinfo("Winner","Congo!!!!!!!O Wins!!!!!!!!")
    
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg='green')
        b5.config(bg='green')
        b6.config(bg='green')
        winner = True
        for w in New.winfo_children():
            w.configure(state="disabled")
            
        messagebox.showinfo("Winner","Congo!!!!!!!O Wins!!!!!!!!")  
            
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg='green')
        b8.config(bg='green')
        b9.config(bg='green')
        winner = True
        for w in New.winfo_children():
            w.configure(state="disabled")
            
        messagebox.showinfo("Winner","Congo!!!!!!!O Wins!!!!!!!!")
            
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg='green')
        b4.config(bg='green')
        b7.config(bg='green')
        winner = True
        for w in New.winfo_children():
            w.configure(state="disabled")
            
        messagebox.showinfo("Winner","Congo!!!!!!!O Wins!!!!!!!!")
            
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg='green')
        b5.config(bg='green')
        b8.config(bg='green')
        winner = True
        for w in New.winfo_children():
            w.configure(state="disabled")
            
        messagebox.showinfo("Winner","Congo!!!!!!!O Wins!!!!!!!!") 
                                   
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg='green')
        b6.config(bg='green')
        b9.config(bg='green')
        winner = True
        for w in New.winfo_children():
            w.configure(state="disabled")
            
        messagebox.showinfo("Winner","Congo!!!!!!!O Wins!!!!!!!!")
            
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg='green')
        b5.config(bg='green')
        b9.config(bg='green')
        winner = True
        for w in New.winfo_children():
            w.configure(state="disabled")
            
        messagebox.showinfo("Winner","Congo!!!!!!!O Wins!!!!!!!!")
        

    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg='green')
        b5.config(bg='green')
        b7.config(bg='green')
        winner = True
        for w in New.winfo_children():
            w.configure(state="disabled")
            
        messagebox.showinfo("Winner","Congo!!!!!!!O Wins!!!!!!!!")
    

        
            
            
def b_click(b):
    
    to_send = str(b)
    
    to_send = to_send.replace('.', '')
    to_send = str(to_send.replace('!', ''))
    print(to_send)
    global clicked
    if b["text"] == '' :
        labels.config(text="O's Turn")
        b.configure(state=DISABLED)
        b['text'] = 'X'
        
        checkwin()
        
        if connection_established == True:
            send_data = to_send.encode()
            conn.send(send_data)
            for w in New.winfo_children():
                w.configure(state="disabled")
            
            
            
        
           
   
             
            
               
 
b1 = Button(New, text='',font=('Verdana',20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b1))
b1.grid(row=0,column=0)
b2 = Button(New, text='',font=('Verdana',20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b2))
b2.grid(row=0,column=1)
b3 = Button(New, text='',font=('Verdana',20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b3))
b3.grid(row=0,column=2)

b4 = Button(New, text='',font=('Verdana',20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b4))
b4.grid(row=1,column=0)
b5 = Button(New, text='',font=('Verdana',20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b5))
b5.grid(row=1,column=1)
b6 = Button(New, text='',font=('Verdana',20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b6))
b6.grid(row=1,column=2)

b7 = Button(New, text='',font=('Verdana',20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b7))
b7.grid(row=2,column=0)
b8 = Button(New, text='',font=('Verdana',20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b8))
b8.grid(row=2,column=1)
b9 = Button(New, text='',font=('Verdana',20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b9))
b9.grid(row=2,column=2)
labels = Label(New, fg="white",bg="black", pady=1,text="My Turn or X's Turn",height=2,justify="center")
labels.grid(row=3,column=0)
def check_for_player():
    while time.time() < timeout_start + timeout:
        if connection_established == False:
            labels.config(text="Waiting for  2 Players")
            
            
        elif connection_established == True:
            labels.config(text="My Turn or X's Turn")
            break
        
            
                
start_thread(check_for_player) 

                
            

    

#menu = Menu(New)
#New.config(menu=menu)
#options = Menu(menu,tearoff=False)


New.mainloop()
