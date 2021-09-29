import tkinter as tk
from tkinter import ttk, Entry
from PIL import Image, ImageTk

LARGEFONT = ("Verdana", 35)

players = 3
player_names = ["Rebecca", "Charlotte", "Tonko", "Tobias"]


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        container = tk.Frame(self, )
        container.grid()

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2, Page3, Page4):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="", font=LARGEFONT)
        label.grid(row=0, column=1, padx=10, pady=10)

        label = ttk.Label(self, text="Start Kenneth Kasse", font=LARGEFONT)
        label.place(relx=.5, rely=0.05, anchor="c")

        button1 = ttk.Button(self, text="Start Game",
                             command=lambda: controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=2, padx=10, pady=10)

        meme = Image.open('work.jpg')
        meme = ImageTk.PhotoImage(meme)
        meme_lbl = tk.Label(self, image=meme)
        meme_lbl.image = meme
        meme_lbl.grid(row=2, column=2, padx=10, pady=10)


# second window frame page1
class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="", font=LARGEFONT)
        label.grid(row=0, column=1, padx=10, pady=10)

        label = ttk.Label(self, text="Venter på start", font=LARGEFONT)
        label.place(relx=.5, rely=0.05, anchor="c")

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Return to start",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place
        # by using grid
        button1.place(relx=.5, rely=0.15, anchor="c")

        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text="Start Game",
                             command=lambda: controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.place(relx=.5, rely=0.22, anchor="c")

        meme = Image.open('progmeme.png')
        meme = ImageTk.PhotoImage(meme)
        meme_lbl = tk.Label(self, image=meme)
        meme_lbl.image = meme
        meme_lbl.place(relx=.5, rely=0.7, anchor="c")


# third window frame page2


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="", font=LARGEFONT)
        label.grid(row=0, column=1, padx=10, pady=10)

        label = ttk.Label(self, text="Write a funny haha meme", font=LARGEFONT)
        label.place(relx=.5, rely=0.05, anchor="c")

        meme = Image.open('work.jpg')
        w, h = meme.size
        if w > h:
            scale = w / h
            w = int(500)
            h = int(w / scale)
        elif w < h:
            scale = h / w
            h = int(450)
            w = int(h / scale)
        meme = meme.resize((w, h))
        meme = ImageTk.PhotoImage(meme)
        meme_lbl = tk.Label(self, image=meme)
        meme_lbl.image = meme
        meme_lbl.grid(row=1, column=1, padx=10, pady=10)

        # Text box to write funny haha meme
        entry1: Entry = tk.Entry(self)
        entry1.grid(row=2, column=1, padx=10, pady=10)
        entry1.get()

        # button to show frame 2 with text
        # layout2
        # button1 = ttk.Button(self, text="Page 1",
        # command=lambda: controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        #  button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Submit",
                             command=lambda: controller.show_frame(Page3))

        # putting the button in its place by
        # using grid
        button2.grid(row=3, column=1, padx=10, pady=10)


class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        # putting the grid in its place by using
        # grid
        label = ttk.Label(self, text="", font=LARGEFONT)
        label.grid(row=0, column=1, padx=10, pady=10)

        label = ttk.Label(self, text="---Voting Time---", font=LARGEFONT)
        label.place(relx=.5, rely=0.05, anchor="c")

        for x in range(players):

            meme = Image.open('andreas.png')
            w, h = meme.size
            if w > h:
                scale = w / h
                w = int(500)
                h = int(w / scale)
                meme = meme.resize((w, h))
                meme = ImageTk.PhotoImage(meme)
                meme_lbl = tk.Label(self, image=meme)
                meme_lbl.image = meme
                if int(x / 2) == 0:
                    meme_lbl.grid(row=int(x / 2 + 1), column=x % 2 + 1, padx=10, pady=10)
                if int(x / 2) == 1:
                    meme_lbl.grid(row=int(x / 2 + 2), column=x % 2 + 1, padx=10, pady=10)

                button1 = ttk.Button(self, text="Yass this queen",
                                     command=lambda: controller.show_frame(Page4))
                if int(x/2) == 0:
                    button1.grid(row=int(x / 2 + 2), column=x % 2 + 1, padx=10, pady=10)
                if int(x/2) == 1:
                    button1.grid(row=int(x / 2 + 4), column=x % 2 + 1, padx=10, pady=10)
            elif w < h:
                scale = h / w
                h = int(450)
                w = int(h / scale)
                meme = meme.resize((w, h))
                meme = ImageTk.PhotoImage(meme)
                meme_lbl = tk.Label(self, image=meme)
                meme_lbl.image = meme
                meme_lbl.grid(row=1, column=x, padx=10, pady=10)

                button1 = ttk.Button(self, text="Yass this queen",
                                     command=lambda: controller.show_frame(Page4))
                button1.grid(row=2, column=x, padx=10, pady=10)




class Page4(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="---SCORE---", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=1, padx=10, pady=10)

        for x in range(players):
            label = ttk.Label(self, text=x + 1, font=LARGEFONT)

            # putting the grid in its place by using
            # grid
            label.grid(row=x + 1, column=0, padx=10, pady=10)

            label = ttk.Label(self, text=player_names[x], font=LARGEFONT)

            # putting the grid in its place by using
            # grid
            label.grid(row=x + 1, column=1, padx=10, pady=10)

        button1 = ttk.Button(self, text="m'ka' goodnight",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button1.grid(row=players + 2, column=1, padx=10, pady=10)


# Driver Code
app = tkinterApp()
app.mainloop()
