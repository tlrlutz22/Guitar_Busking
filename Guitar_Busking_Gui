from tkinter import *
import tkinter.font as tkfont
from tkinter import ttk
from PIL import ImageTk, Image
import math
import song_database


root = Tk()
root.title('Library')
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()

root.geometry("%dx%d" % (width, height))

main_frame = Frame(root, bg="#dcdcdc")
main_frame.pack(fill = BOTH, expand=1)

## Payment Frame
payment_frame = LabelFrame(main_frame, borderwidth=0, bg="#dcdcdc")
# payment_frame.grid(row=0, column=0, sticky='nw', rowspan=len(song_database.song_info)+2)
payment_frame.grid(row=0, column=0, sticky='nw', rowspan=100)

# Objects
venmo_QR = ImageTk.PhotoImage(Image.open(r'C:\Users\Tyler\Desktop\Gui_images/Venmo QR.PNG').resize((400, 525)))
cashapp_QR = ImageTk.PhotoImage(Image.open(r'C:\Users\Tyler\Desktop\Gui_images/Cashapp QR.PNG').resize((400, 525)))

# Labels
# Title = Label(frame_payment, text= 'Venmo for song requests', font="bold")
QR_img1 = Label(payment_frame, image=venmo_QR, borderwidth=0)
QR_img2 = Label(payment_frame, image=cashapp_QR, borderwidth=0)


# Grid
num_span = math.ceil(len(song_database.song_info)/2)
QR_img1.grid(row=0, column=0)
QR_img2.grid(row=1, column=0, sticky='news')


## Title Frame
title_frame = LabelFrame(main_frame, borderwidth=0, bg="#dcdcdc")
title_frame.grid(row=0, column=1, sticky='ns')

# Labels
root.option_add('*Font', 'ArialRoundedMTBold 30')
Title = Label(title_frame, text='Venmo for song requests!', bg="#dcdcdc", borderwidth=0)

# Grid
Title.grid(row=0, column=0, padx=580)

## Subtitles Frame
subtitles_frame = LabelFrame(main_frame, borderwidth=0, bg="#dcdcdc")
subtitles_frame.grid(row=1, column=1, sticky='nw')

# Labels
root.option_add('*Font', 'Verdana 22')
art_title = Label(subtitles_frame, text='Art', bg="#dcdcdc")
artist_title = Label(subtitles_frame, text='Artist', bg="#dcdcdc", padx=200)
song_title = Label(subtitles_frame, text='Song', bg="#dcdcdc", padx=400)

# Grid
art_title.grid(row=0, column=0)
artist_title.grid(row=0, column=1)
song_title.grid(row=0, column=2)


## Music Library Frame
frame_music = Frame(main_frame, borderwidth=0, bg="#dcdcdc")
frame_music.grid(row=2, column=1, sticky='news')

#scrollbar
my_canvas = Canvas(master=frame_music, borderwidth=0, bg="#dcdcdc")
my_canvas.grid(row=0, column=0, sticky='news', ipadx=555, ipady=345)

my_scrollbar = ttk.Scrollbar(frame_music, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.grid(row=0, column=1, sticky='nes')

my_canvas.configure(yscrollcommand=my_scrollbar.set, borderwidth=0)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

second_frame = Frame(my_canvas, borderwidth=0, bg="#dcdcdc")

my_canvas.create_window((0,0), window=second_frame, anchor="nw")

# Image objects
album_art = [ImageTk.PhotoImage(Image.open(song_database.song_info[i][0]).resize((90,90)))
             for i in range(len(song_database.song_info))]

# Labels
root.option_add('*Font', 'Arial 14')
album_art_labeling = [Label(second_frame, borderwidth=0, image=album_art[i]
                      ) for i in range(len(song_database.song_info))]
artist_name_labeling = [Label(second_frame, text=song_database.song_info[i][1],
                        width="20",height="3", bg="#dcdcdc", padx=100) 
                        for i in range(len(song_database.song_info))]
song_name_labeling = [Label(second_frame, text=song_database.song_info[i][2],
                    width="20",height="3", bg="#dcdcdc", padx=340) 
                      for i in range(len(song_database.song_info))]
                        

for i in range(len(song_database.song_info)):
    album_art_labeling[i].grid(row=i,column=0, sticky='nsew')
    artist_name_labeling[i].grid(row=i,column=1, sticky='nsew')
    song_name_labeling[i].grid(row=i,column=2, sticky='nsew')


root.mainloop()
