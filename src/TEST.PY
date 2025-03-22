from tkinter import *
# from tkinter import Tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO
import urllib.parse

import requests


class Request:
    def __init__(self, method, args):
        self.args = args
        self.method = method

inc = 0
def fetch_information(title, poster, date, rating):
    global inc
    inc += 1
    text[f'a{inc}'].config(text=title)

    if check_var.get():
        text2[f'a2{inc}'].config(text=date)
    else:
        text2[f'a2{inc}'].config(text="")

    if check_var2.get():
        text3[f'a32{inc}'].config(text=rating)
    else:
        text3[f'a32{inc}'].config(text="")

    response = requests.get(poster)
    imag_data = response.content
    img = (Image.open(BytesIO(imag_data)))
    resized_image = img.resize((140, 200))
    photo2 = ImageTk.PhotoImage(resized_image)
    image[f'b{inc}'].config(image=photo2)
    image[f'b{inc}'].image = photo2



def search():
    global inc
    inc = 0
    # print(Search.get())
    request = Request('GET', {'search': Search.get()})
    if request.method == 'GET':
        search = urllib.parse.quote(request.args.get('search', ''))
        url = f"https://www.googleapis.com/books/v1/volumes?q={search}&maxResults=5"
        response = requests.get(url)
        # print(response.json())

        if response.status_code == 200: 
            data = response.json()
            for item in data.get('items', []):
                volume_info = item.get('volumeInfo', {})
                title = volume_info.get('title', 'N/A')
                publisher = volume_info.get('publisher', 'N/A')
                published_date = volume_info.get('publishedDate', 'N/A')
                author = volume_info.get('authors', ['N/A'])
                rating = volume_info.get('averageRating', ['N/A'])
                image_links = volume_info.get('imageLinks', {})
                image = image_links.get('thumbnail') if 'thumbnail' in image_links else 'N/A'

                print(title)
                print(publisher)
                print(published_date)
                print(author)
                print(rating)
                print(image) 

                print(inc)
                print('----------')

                fetch_information(title, image, published_date, rating)

                if check_var.get() or check_var2.get():
                    frame21.place(x=160, y=600)
                    frame22.place(x=360, y=600)
                    frame23.place(x=560, y=600)
                    frame24.place(x=760, y=600)
                    frame25.place(x=960, y=600)
                else:
                    frame21.place_forget()
                    frame22.place_forget()
                    frame23.place_forget()
                    frame24.place_forget()
                    frame25.place_forget()
        else:
            print("Failed to fetch data from Google Books API.")
            messagebox.showinfo("info", "Failed to fetch data from Google Books API.")


def showMenu(event):
    #Display the menu at the mouse position
    menu.post(event.x_root, event.y_root)

############################################################

root = Tk()
root.title("Book Recommendation System")
root.geometry("1250x600")
root.config(bg="#111119")

# root.resizable(False, False)
####################

#icon
icon_image = PhotoImage(file="images/icon.png")
root.iconphoto(False, icon_image)

#background image
heading_image=PhotoImage(file="images/background.png")
Label(root, image=heading_image, bg="#111119").place(x=-2, y=-2)

#logo
logo_image=PhotoImage(file="images/logo.png")
Label(root, image=logo_image, bg="#0099ff").place(x=300, y=80)

#heading
heading=Label(root, text="BOOK RECOMMENDATOIN SYSTEM", font=("Lato", 30, "bold"), fg='white', bg="#0099ff")
heading.place(x=410, y=90)

#search Background image
search_box = PhotoImage(file="images/Rectangle_2.png")
Label(root, image=search_box, bg="#0099ff").place(x=300, y=155)

#entry box / search section
Search = StringVar()
search_entry=Entry(root, textvariable= Search, width=20, font=("Lato", 25), bg='white', fg='black', bd=0)
search_entry.place(x=415, y=172)

#Search button
recommend_button_image = PhotoImage(file='images/Search.png')
recommend_button = Button(root, image=recommend_button_image, bg='#0099ff', bd=0, activebackground='#252532', cursor='hand2', command=search)
recommend_button.place(x=860, y=169)

################################################


############################################################

menu = Menu(root, tearoff=0)

check_var = BooleanVar()
menu.add_checkbutton(label="Publish Date", variable=check_var, command=lambda: print(f"check option is {'checked Publish Date' if check_var.get() else 'unchecked'}"))

check_var2 = BooleanVar()
menu.add_checkbutton(label="Ratting", variable=check_var2, command=lambda: print(f"check option is {'checked Ratting' if check_var2.get() else 'unchecked'}"))

# setting button
Setting_image = PhotoImage(file='images/setting.png')
setting = Button(root, image=Setting_image, bd=0, cursor='hand2', activebackground='#0099ff', bg='#0099ff')
setting.place(x=1050, y=175)

setting.bind('<Button-1>', showMenu)

# logout button
logout_image=PhotoImage(file='images/logout.png')
Button(root,  image=logout_image, bg='#0099ff', cursor='hand2', command=lambda: root.destroy()).place(x=1150, y=20)

################################

# #first frame
frame1 = Frame(root, width=150, height=240, bg='white')
frame2 = Frame(root, width=150, height=240, bg='white')
frame3 = Frame(root, width=150, height=240, bg='white')
frame4 = Frame(root, width=150, height=240, bg='white')
frame5 = Frame(root, width=150, height=240, bg='white')
frame1.place(x=160, y=350)
frame2.place(x=360, y=350)
frame3.place(x=560, y=350)
frame4.place(x=760, y=350)
frame5.place(x=960, y=350)

# book text
# text = {'a1':Label(frame1, text="Book Title", font=("arial",10), fg='green')}
# # Định nghĩa Label với cấu hình font đúng
text = {
    'a1': Label(frame1, text="Book Title", font=("arial", 10), fg='green'),
    'a2': Label(frame2, text="Book Title", font=("arial", 10), fg='green'),
    'a3': Label(frame3, text="Book Title", font=("arial", 10), fg='green'),
    'a4': Label(frame4, text="Book Title", font=("arial", 10), fg='green'),
    'a5': Label(frame5, text="Book Title", font=("arial", 10), fg='green')
}
# Hiển thị Label
text['a1'].place(x=10, y=4)
text['a2'].place(x=10, y=4)
text['a3'].place(x=10, y=4)
text['a4'].place(x=10, y=4)
text['a5'].place(x=10, y=4)
# text['a1'].pack()

#Poster / Image of Book
image = {
    'b1':Label(frame1),
    'b2':Label(frame2),
    'b3':Label(frame3),
    'b4':Label(frame4),
    'b5':Label(frame5)
}
image['b1'].place(x=3, y=30)
image['b2'].place(x=3, y=30)
image['b3'].place(x=3, y=30)
image['b4'].place(x=3, y=30)
image['b5'].place(x=3, y=30)

#frame second
frame21 = Frame(root, width=150, height=240, bg='#e6e6e6')
frame22 = Frame(root, width=150, height=240, bg='#e6e6e6')
frame23 = Frame(root, width=150, height=240, bg='#e6e6e6')
frame24 = Frame(root, width=150, height=240, bg='#e6e6e6')
frame25 = Frame(root, width=150, height=240, bg='#e6e6e6')
# frame21.place(x=160, y=600)
# frame22.place(x=360, y=600)
# frame23.place(x=560, y=600)
# frame24.place(x=760, y=600)
# frame25.place(x=960, y=600)

#published date
text2 = {
    'a21': Label(frame21, text="Date", font=("arial", 10), fg='red', bg='#e6e6e6'),
    'a22': Label(frame22, text="Date", font=("arial", 10), fg='red', bg='#e6e6e6'),
    'a23': Label(frame23, text="Date", font=("arial", 10), fg='red', bg='#e6e6e6'),
    'a24': Label(frame24, text="Date", font=("arial", 10), fg='red', bg='#e6e6e6'),
    'a25': Label(frame25, text="Date", font=("arial", 10), fg='red', bg='#e6e6e6')
}
text2['a21'].place(x=10, y=4)
text2['a22'].place(x=10, y=4)
text2['a23'].place(x=10, y=4)
text2['a24'].place(x=10, y=4)
text2['a25'].place(x=10, y=4)

# Ratting
text3 = {
    'a321': Label(frame21, text="Ratting", font=("arial", 10), fg='red', bg='#e6e6e6'),
    'a322': Label(frame22, text="Ratting", font=("arial", 10), fg='red', bg='#e6e6e6'),
    'a323': Label(frame23, text="Ratting", font=("arial", 10), fg='red', bg='#e6e6e6'),
    'a324': Label(frame24, text="Ratting", font=("arial", 10), fg='red', bg='#e6e6e6'),
    'a325': Label(frame25, text="Ratting", font=("arial", 10), fg='red', bg='#e6e6e6')
}
text3['a321'].place(x=20, y=30)
text3['a322'].place(x=20, y=30)
text3['a323'].place(x=20, y=30)
text3['a324'].place(x=20, y=30)
text3['a325'].place(x=20, y=30)



####################
root.mainloop()