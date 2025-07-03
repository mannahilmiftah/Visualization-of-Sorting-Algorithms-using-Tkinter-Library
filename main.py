from tkinter import *
from tkinter import ttk
import random
from countSort import count_sort
from insertionSort import insertion
from bubbleSort import bubble
from bucketSort import bucket
from heapSort import heap
from mergeSort import mergeSort
from quickSort import quick
from radixSort import radix
from book_algo1 import modified_quick
from book_algo2 import modified_count

class Sorting:
    def __init__(self):
        # Creating an instance of tkinter frame which helps to create the root window and manages all other components of tkinter
        self.root = Tk()

        # Title for the window created
        self.root.title("Sorting Visualizer")

        # Window size
        self.width = 1200
        self.height = 700
        self.posr = int(self.root.winfo_screenwidth()/2 - self.width/2)
        self.posd = int(self.root.winfo_screenheight()/2 - self.height/2)
        self.root.geometry("%dx%d+%d+%d" % (self.width, self.height, self.posr, self.posd))

        # To change the size of tkinter root window (optional)
        #self.root.resizable(0,0)

        # Background color of window
        self.root.config(bg="Black")

        # Binding function is used to deal with the events. Here when escape is pressed program will exit
        self.root.bind("<Escape>", self.quit)
        
        # VARIABLES
        # StringVar() helps to manage the value of widgets. We can take user input by creating an instance of it
        self.current_algo = StringVar()

        # To store the array to be sorted
        self.data = []
        
        # TITLE
        # The relief style here refers to certain 3-D effects
        main_title = Label(self.root,text='Sorting Visualizer',bd=10,relief=RIDGE,font=('Arial',20,'bold'),bg='Grey',fg='white')
        # Organizing/positioning the label widget
        main_title.pack(side=TOP,fill=X)
        
        # Creating Frames
        # Frame is for organizing tkinter widgets inside
        
        main_frame = Frame(self.root,bd=6,relief=RIDGE,bg='Grey')
        # Placing frame in two dimensional grid
        main_frame.place(x=875,y=70,width=300,height=575)

        # Sliding Frame
        slide_option_frame = Frame(main_frame,bd=6,relief=RIDGE,bg='Grey')
        slide_option_frame.place(x=5,y=60,width=280,height=330)

        # Creating Button Frame
        Button_Frame = Frame(main_frame,bd=4,relief=RIDGE,bg='Grey')
        Button_Frame.place(x=5,y=400,width=280,height=145)
        
        # Canvas
        # Canvas is used to draw in a window (bar graph)
        self.canvas = Canvas(self.root,bd=6,relief=RIDGE,bg='Grey')
        self.canvas.place(x=20,y=70,width=830,height=575)
        
        # Defining Labels
        # This label option is inside frame widget
        label_Algo = Label(main_frame,text="ALGORITHM",bg='Grey',fg="white",font=('Arial',12,'bold'))
        label_Algo.place(x=10,y=20,width=125)

        # Creating Quit option
        self.label_quit = Label(self.root,text="Press Escape to Quit",bg="Grey",fg="white",font=('Arial',15,'bold'),bd=5,relief=RIDGE)
        self.label_quit.pack(side=BOTTOM,fill=X)
        
        # Creating Algorithm Menu
        # Combobox is a combination of entry and dropdown menu. Entry widget is used to accept a single line text-string from a user
        self.menu = ttk.Combobox(main_frame, textvariable=self.current_algo,values=["Bubble Sort","Insertion Sort","Merge Sort","Quick Sort","Heap Sort","Radix Sort","Bucket Sort","Count Sort","Modified QuickSort","Modified CountSort"],state='readonly') 
        self.menu.place(x=130,y=20,width=125)
        
        # Scale widget provides a graphical slider object that allows you to select values from a specific scale
        # Grid is for arranging labels
        # Speed bar
        self.speed = Scale(slide_option_frame,activebackground="orange",relief=RIDGE,from_=0,to=1.0,length=250,digits=2,resolution=0.1,orient=HORIZONTAL,label="Delay in seconds") 
        self.speed.grid(row=0,column=0,padx=8,pady=11)
        
        # Size of Array
        self.array_size = Scale(slide_option_frame,activebackground="orange",relief=RIDGE,from_=5,to=1000,length=250,resolution=1,orient=HORIZONTAL,label="Size of Array (5-100)") 
        self.array_size.grid(row=1,column=0,padx=8,pady=11) 
        
        # Minimum value
        self.min_val = Scale(slide_option_frame,activebackground="orange",relief=RIDGE,from_=0,to=8,length=250,resolution=1,orient=HORIZONTAL,label="Minimum Value (0-8)") 
        self.min_val.grid(row=2, column=0, padx=8, pady=11) 
        
        # Maximum value
        self.max_val = Scale(slide_option_frame,activebackground="orange",relief=RIDGE,from_=1,to=200,length=250,resolution=1,orient=HORIZONTAL,label="Maximum Value (1-200)") 
        self.max_val.grid(row=3, column=0, padx=8, pady=11)

        #CREATING BUTTONS
        # Start button
        start_button = Button(Button_Frame,text="Start Sorting",bg="White",width=33,command=self.start_sort)
        start_button.grid(row=0,column=0,padx=15,pady=8)
        
        # Generate buttons
        self.generate_numbers()
        start_button = Button(Button_Frame,text="Generate Array",bg="White",width=33,command=self.generate_numbers)
        start_button.grid(row=1,column=0,padx=15,pady=12)

        self.numbers_bucket()
        start_button = Button(Button_Frame,text="Generate Array for Bucket Sort",bg="White",width=33,command=self.numbers_bucket)
        start_button.grid(row=2,column=0,padx=15,pady=13)
        
        # Mainloop
        self.root.mainloop() 
        
    # Quit program
    def quit(self, event):
        self.root.quit()
        
    # Generating random array
    def generate_numbers(self):
        min = int(self.min_val.get())
        max = int(self.max_val.get()) 
        size = int(self.array_size.get())
        self.data = []
        file = open("random.txt","w")
        for _ in range(size):
            self.data.append(random.randrange(min, max+1))
            line = str(self.data[_])
            file.write(line)
            file.write(",")
        file.close()
        self.drawData(self.data, ['Purple' for x in range(len(self.data))])
    
    # Generating random array for bucket sort between 0 & 1
    def numbers_bucket(self):
        min_v = 0
        max_v = 1
        size = int(self.array_size.get())
        self.data = []
        file = open("random.txt","w")
        for _ in range(size):
            self.data.append(round(random.uniform(min_v,max_v),2))
            line = str(self.data[_])
            file.write(line)
            file.write(",")
        file.close()
        self.drawData(self.data, ['Purple' for x in range(len(self.data))])
        
    # Draw bar graph
    def drawData(self,data,colourlist):
        self.canvas.delete("all")
        can_height = 575
        can_width = 800
        x_width = can_width/(len(self.data)+1)
        offset = 15
        spacing = 10
        # To set the size of bar
        bar_size = [i/max(self.data) for i in self.data]
        for i, height in enumerate(bar_size):
            # top left corner
            x0 = i*x_width + offset + spacing
            y0 = can_height - height*500
            # bottom right corner 
            x1 = ((i+1)*x_width) + offset 
            y1 = can_height
            # data bars are generated as Red colored vertical rectangles
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=colourlist[i])
            # It is used to display one or more text lines on canvas
            self.canvas.create_text(x0+2, y0, anchor=SE, text=str(self.data[i])) 
        self.root.update_idletasks() 
        
    # Select & Start sorting
    def start_sort(self):
        if self.menu.get() == "Insertion Sort":
            insertion(self.data, self.drawData, self.speed.get())
        elif self.menu.get() == "Merge Sort":
            mergeSort(self.data, self.drawData, self.speed.get(),0,self.array_size.get()-1)
        elif self.menu.get() == "Quick Sort":
            quick(self.data, self.drawData, self.speed.get(),0,self.array_size.get()-1)
        elif self.menu.get() == "Radix Sort":
            radix(self.data, self.drawData, self.speed.get())
        elif self.menu.get() == "Heap Sort":
            heap(self.data, self.drawData, self.speed.get()) 
        elif self.menu.get() == "Bucket Sort":
            bucket(self.data, self.drawData, self.speed.get())
        elif self.menu.get() == "Bubble Sort":
            bubble(self.data, self.drawData, self.speed.get())
        elif self.menu.get() == "Count Sort":
            count_sort(self.data, self.drawData, self.speed.get())
        elif self.menu.get() == "Modified QuickSort":
            modified_quick(self.data, self.drawData, self.speed.get(),0,self.array_size.get()-1)
        elif self.menu.get() == "Modified CountSort":
            modified_count(self.data, self.drawData, self.speed.get())
    
if __name__ == '__main__':
    obj = Sorting()