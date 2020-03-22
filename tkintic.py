import tkinter as tk
import tkinter.messagebox
import tkinter.font as font
i=True
f=0
ans=0

def fun(button):
    global f,i,ans
    if(button['text']==' ' and i==True):
        button['text']='x'
        button['fg']='blue'        
        i=False
    else:
        if(button['text']==' ' and i==False):
            button['text']='o'
            button['fg']='red'
            i=True
            
    if(f>3):
        if((b1['text']=='x' and b2['text']=='x' and b3['text']=='x') or(b4['text']=='x' and b6['text']=='x' and b5['text']=='x') or(b6['text']=='x' and b7['text']=='x' and b8['text']=='x') or(b1['text']=='x' and b4['text']=='x' and b7['text']=='x') or (b2['text']=='x' and b5['text']=='x' and b8['text']=='x') or (b3['text']=='x' and b6['text']=='x' and b9['text']=='x') or(b1['text']=='x' and b5['text']=='x' and b9['text']=='x') or (b3['text']=='x' and b5['text']=='x' and b7['text']=='x' )):
            ans=tkinter.messagebox.askyesno(title="Match done",message="Player x won the match\nWant to play again?")
            if(ans==1):
                b1['text'],b2['text'],b3['text'],b4['text'],b5['text'],b6['text'],b7['text'],b8['text'],b9['text']=' ',' ',' ',' ',' ',' ',' ',' ',' '
            else:
                wn.destroy()
        else:
            if((b1['text']=='o' and b2['text']=='o' and b3['text']=='o') or(b4['text']=='o' and b6['text']=='o' and b5['text']=='o') or(b6['text']=='o' and b7['text']=='o' and b8['text']=='o') or(b1['text']=='o' and b4['text']=='o' and b7['text']=='o') or (b2['text']=='o' and b5['text']=='o' and b8['text']=='o') or (b3['text']=='o' and b6['text']=='o' and b9['text']=='o') or(b1['text']=='o' and b5['text']=='o' and b9['text']=='o') or (b3['text']=='o' and b5['text']=='o' and b7['text']=='o' )):
                ans=tkinter.messagebox.askyesno(title="Match done",message="Player o won the match\nWant to play again?")
                if(ans):
                    b1['text'],b2['text'],b3['text'],b4['text'],b5['text'],b6['text'],b7['text'],b8['text'],b9['text']=' ',' ',' ',' ',' ',' ',' ',' ',' '    
                else:
                    wn.destroy()
    if(ans==0):
        f+=1
    else:
        f=0
        ans=0
    
    
wn=tk.Tk()
p1=tk.StringVar()
p2=tk.StringVar()
wn.configure(bg="lightpink")
button=tk.StringVar()
ff = font.Font(family='Helvetica', size=20, weight='bold')

l1=tk.Label(text="Player 1: X",font=ff,fg="blue",bg="lightpink")
l1.grid(row=0,columnspan=2)

l2=tk.Label(text="Player 2: O",font=ff,fg="red",bg="lightpink")
l2.grid(row=1,columnspan=2)

b1=tk.Button(text=' ',command=lambda:fun(b1),font=("calibria",55),width=3,padx=0,pady=0,bg='yellow')
b1.grid(row=2,column=0)

b2=tk.Button(text=' ',command=lambda:fun(b2),font=("calibria",55),width=3,padx=0,pady=0,bg='yellow')
b2.grid(row=2,column=1)

b3=tk.Button(text=' ',command=lambda:fun(b3),font=("calibria",55),width=3,padx=0,pady=0,bg='yellow')
b3.grid(row=2,column=2)

b4=tk.Button(text=' ',command=lambda:fun(b4),font=("calibria",55),width=3,padx=0,pady=0,bg='yellow')
b4.grid(row=3,column=0)

b5=tk.Button(text=' ',command=lambda:fun(b5),font=("calibria",55),width=3,padx=0,pady=0,bg='yellow')
b5.grid(row=3,column=1)

b6=tk.Button(text=' ',command=lambda:fun(b6),font=("calibria",55),width=3,padx=0,pady=0,bg='yellow')
b6.grid(row=3,column=2)

b7=tk.Button(text=' ',command=lambda:fun(b7),font=("calibria",55),width=3,padx=0,pady=0,bg='yellow')
b7.grid(row=4,column=0)

b8=tk.Button(text=' ',command=lambda:fun(b8),font=("calibria",55),width=3,padx=0,pady=0,bg='yellow')
b8.grid(row=4,column=1)

b9=tk.Button(text=' ',command=lambda:fun(b9),font=("calibria",55),width=3,padx=0,pady=0,bg='yellow')
b9.grid(row=4,column=2)


    
wn.mainloop()
