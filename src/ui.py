from tkinter import *
from tkinter import messagebox
from utils import create_rounded_rectangle
from book_management import BookDataManagement
# from book_management import UIDataManagement
import requests
from PIL import Image, ImageTk
from io import BytesIO
import urllib.parse
import time
from utils import create_book_display




class BookRecommendationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Recommendation System")
        self.root.config(bg="#111119")

        # Căn giữa cửa sổ
        self.center_window(1250, 680)

        self.inc = 0
        self.check_var_date = BooleanVar()
        self.check_var_rating = BooleanVar()

        self.create_ui()


    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_position = (screen_width - width) // 2
        y_position = (screen_height - height) // 2
        self.root.geometry(f"{width}x{height}+{x_position}+{y_position}")


    def create_ui(self):
        icon_image = PhotoImage(file="images/icon.png")
        self.root.iconphoto(False, icon_image)

        # Tạo Canvas
        canvas = Canvas(self.root, width=1250, height=225, bg="white", highlightthickness=0)
        canvas.place(x=0, y=0)
        create_rounded_rectangle(canvas, 10, 10, 1240, 215, radius=20, fill="#FF6666", outline="")

        # Logo
        logo_image = PhotoImage(file="images/logo.png")
        Label(self.root, image=logo_image, bg="#FF6666").place(x=100, y=80)
        self.root.logo_image = logo_image

        # Tiêu đề chính
        heading = Label(self.root, text="BOOK RECOMMENDATION SYSTEM", font=("Lato", 30, "bold"), fg='white', bg="#FF6666")
        heading.place(x=280, y=50)

        # Thanh tìm kiếm
        search_box_image = PhotoImage(file="images/Rectangle_2.png")
        Label(self.root, image=search_box_image, bg="#FF6666").place(x=294, y=120)
        self.root.search_box_image = search_box_image

        self.search_var = StringVar()
        search_entry = Entry(self.root, textvariable=self.search_var, width=20, font=("Lato", 25), bg='white', fg='black', bd=0)
        search_entry.place(x=415, y=138)

        recommend_button_image = PhotoImage(file="images/Search.png")
        recommend_button = Button(self.root, image=recommend_button_image, bg="#FF6666", bd=0, cursor='hand2', command=self.search_books)
        recommend_button.place(x=860, y=134)
        self.root.recommend_button_image = recommend_button_image

        # Nút cài đặt
        setting_image = PhotoImage(file="images/setting.png")
        setting_button = Button(self.root, image=setting_image, bd=0, cursor='hand2', bg="#FF6666")
        setting_button.place(x=1050, y=135)
        self.root.setting_image = setting_image

        setting_menu = Menu(self.root, tearoff=0)
        setting_menu.add_checkbutton(label="Publish Date", variable=self.check_var_date)
        setting_menu.add_checkbutton(label="Rating", variable=self.check_var_rating)
        setting_button.bind('<Button-1>', lambda event: setting_menu.post(event.x_root, event.y_root))

        # Nút đăng xuất
        logout_image = PhotoImage(file="images/logout.png")
        Button(self.root, image=logout_image, bg="#FF6666", cursor='hand2', command=self.root.destroy).place(x=1150, y=20)
        self.root.logout_image = logout_image

        # Nút quản lý dữ liệu
        Button(self.root, text="Data", font=("Lato", 15, "bold"), bg="#FF6666", fg="white", command=self.open_data_management).place(x=300, y=230)

        # Gọi hàm để tạo giao diện hiển thị sách với bo góc
        self.frames, self.text_labels, self.image_labels = create_book_display(self.root)


    def open_data_management(self):
        BookDataManagement(self.root)

    
    def fetch_information(self, title, poster, date, rating):
            """
            Cập nhật thông tin sách vào giao diện hiển thị.
            Parameters:
            - title (str): Tiêu đề sách
            - poster (str): URL ảnh bìa sách
            - date (str): Ngày xuất bản
            - rating (str): Đánh giá trung bình
            """

            # Kiểm tra nếu đã hiển thị đủ số lượng sách cho phép
            if self.inc >= len(self.frames):
                return

            # Lấy label để hiển thị tiêu đề và ảnh sách
            text_label = self.text_labels[self.inc]
            image_label = self.image_labels[self.inc]

            # Cập nhật tiêu đề sách
            text_label.config(text=title)

            # Nếu tùy chọn "Hiển thị ngày xuất bản" được bật, thêm thông tin ngày vào tiêu đề
            if self.check_var_date.get():
                text_label.config(text=f"{title}\nDate: {date}")

            # Nếu tùy chọn "Hiển thị đánh giá" được bật, thêm thông tin đánh giá vào tiêu đề
            if self.check_var_rating.get():
                text_label.config(text=f"{title}\nRating: {rating}")

            # Nếu có ảnh bìa hợp lệ, tải và hiển thị ảnh
            if poster != 'N/A':
                response = requests.get(poster)  # Gửi yêu cầu tải ảnh từ URL
                img_data = response.content  # Lấy dữ liệu ảnh
                img = Image.open(BytesIO(img_data))  # Đọc ảnh từ dữ liệu tải về
                resized_image = img.resize((120, 160))  # Thay đổi kích thước ảnh phù hợp
                photo = ImageTk.PhotoImage(resized_image)  # Chuyển đổi thành ảnh hiển thị trên Tkinter
                
                # Cập nhật ảnh vào label hiển thị
                image_label.config(image=photo)
                image_label.image = photo  # Lưu tham chiếu để tránh bị xóa bộ nhớ

            # Tăng biến đếm để cập nhật thông tin cho sách tiếp theo
            self.inc += 1


    def search_books(self):
        """Tìm kiếm sách từ Google Books API và hiển thị kết quả."""
        start_time = time.time()

        self.inc = 0  # Reset bộ đếm hiển thị sách
        search_query = self.search_var.get().strip()

        if not search_query:
            messagebox.showinfo("Thông báo", "Vui lòng nhập từ khóa tìm kiếm!")
            return

        search_query_encoded = urllib.parse.quote(search_query)
        url = f"https://www.googleapis.com/books/v1/volumes?q={search_query_encoded}&maxResults=5"

        try:
            response = requests.get(url, timeout=10)  # Thêm timeout để tránh treo
            response.raise_for_status()  # Kiểm tra lỗi HTTP (4xx, 5xx)

            data = response.json()

            if "items" not in data:
                messagebox.showinfo("Không tìm thấy", "Không có kết quả phù hợp.")
                return

            # Lặp qua từng sách trong kết quả
            for item in data["items"]:
                volume_info = item.get("volumeInfo", {})
                title = volume_info.get("title", "N/A")
                published_date = volume_info.get("publishedDate", "N/A")
                rating = volume_info.get("averageRating", "N/A")
                poster = volume_info.get("imageLinks", {}).get("thumbnail", "N/A")

                self.fetch_information(title, poster, published_date, rating)

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Lỗi", f"Lỗi khi lấy dữ liệu từ API: {e}")

        end_time = time.time()
        print(f"⏳ Thời gian gọi API: {end_time - start_time:.2f} giây")
        print(f"📚 Số sách hiển thị: {self.inc}")