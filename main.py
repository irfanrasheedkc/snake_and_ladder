#Main file

from tkinter import *

#Tkinter window
root=Tk()
root.title('Snake and Ladder')
root.geometry(f'800x800')
root.resizable(False,False)

#set window color
root.configure(bg='white')

#Title icon
photo = PhotoImage(file = "icon.png")
root.iconphoto(False, photo)
# Add a frame to set the size of the window
frame= Frame(root, relief= 'sunken')
frame.pack(fill= BOTH, expand= True, padx= 10, pady=0)
frame.configure(bg='white')

canvas = Canvas(height=800 , width=900)

y1=3
y2=78

count = 0

list = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91,
         81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
         80, 79, 78, 77, 76, 75, 74, 73, 72, 71,
         61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
         60, 59, 58, 57, 56, 55, 54, 53, 52, 51,
         41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
         40, 39, 38, 37, 36, 35, 34, 33, 32, 31,
         21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
         20, 19, 18, 17, 16, 15, 14, 13, 12, 11,
         1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list)
for i in range(10):
    x1 = 3
    x2 = 78
    # if (i % 2 == 0):
    #     count = count + 10
    for j in range(10):
            if((i+j)%2==0):
                fill="red"
            else:
                fill="white"
            canvas.create_rectangle(x1,y1,x2,y2 ,outline ="black",fill =fill,width = 2 )
            canvas.create_text(x1+37, y1+37, text=list[count], fill="black", font=('Helvetica 15 bold'))
            count = count+1
            x1 = x1+75
            x2 = x2+75
    y1 = y1+75
    y2 = y2+75
canvas.pack(padx = 10, pady = 10)

root.mainloop()