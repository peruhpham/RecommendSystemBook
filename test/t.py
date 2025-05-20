# import tkinter as tk
# from tkinter import ttk

# class MainApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Main Frame Example")
#         self.root.geometry("1000x600")  # Kích thước cửa sổ chính

#         # Frame chính bên phải
#         main_frame = ttk.Frame(self.root, width=700, height=500, relief="solid", borderwidth=1)
#         main_frame.place(x=250, y=50)  # Đặt frame chính ở giữa

#         # Frame bên trái
#         self.create_left_frame()

#     def create_left_frame(self):
#         left_frame = ttk.LabelFrame(self.root, text="Quản lý dữ liệu", width=200, height=300)
#         left_frame.place(x=20, y=300)  # Đặt tại tọa độ (20, 300)

#         # Các thành phần trong frame bên trái
#         name_entry = ttk.Entry(left_frame)
#         name_entry.insert(0, "Name book")
#         name_entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

#         author_spinbox = ttk.Spinbox(left_frame, from_=1, to=100)
#         author_spinbox.insert(0, "Author")
#         author_spinbox.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

#         combo_list = ["*****", "****", "***", "**", "*"]
#         status_combobox = ttk.Combobox(left_frame, values=combo_list)
#         status_combobox.current(0)
#         status_combobox.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

#         employed_var = tk.BooleanVar()
#         checkbutton = ttk.Checkbutton(left_frame, text="Employed", variable=employed_var)
#         checkbutton.grid(row=3, column=0, padx=5, pady=5, sticky="w")

#         insert_button = ttk.Button(left_frame, text="Thêm")
#         insert_button.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

#         delete_button = ttk.Button(left_frame, text="Xóa")
#         delete_button.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

#         export_button = ttk.Button(left_frame, text="Xuất Excel")
#         export_button.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = MainApp(root)
#     root.mainloop()


import csv

def load_books_and_ratings(books_file, ratings_file):
    """
    Đọc dữ liệu từ Books.csv và Ratings.csv, sau đó in thông tin ISBN, Title, và Rating.
    """
    try:
        # Tải dữ liệu Ratings.csv vào dictionary
        ratings = {}
        with open(ratings_file, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # Bỏ qua dòng tiêu đề
            for row in reader:
                isbn = row[0].strip()
                rating = row[1].strip()
                ratings[isbn] = rating

        # Đọc dữ liệu từ Books.csv và in thông tin
        print(f"{'ISBN':<15} {'Title':<30} {'Rating':<10}")
        print("-" * 60)
        with open(books_file, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # Bỏ qua dòng tiêu đề
            count = 0
            for row in reader:
                count += 1
                if count > 100:
                    print("Đã dừng lại sau 100 bản ghi.")
                    break
                # Giả sử cột ISBN là cột đầu tiên và Title là cột thứ hai
                isbn = row[0].strip()
                title = row[1].strip()
                rating = ratings.get(isbn, "N/A")  # Lấy Rating từ dictionary, nếu không có thì "N/A"
                print(f"{isbn:<15} {title:<150} {rating:<10}")
    except Exception as e:
        print(f"❌ Lỗi khi xử lý dữ liệu: {e}")

if __name__ == "__main__":
    # Đường dẫn đến tệp CSV
    books_file = "D:\\dataBookRecommend\\Books.csv"  # Thay bằng đường dẫn tệp của bạn
    ratings_file = "D:\\dataBookRecommend\\Ratings.csv"  # Thay bằng đường dẫn tệp của bạn

    # Gọi hàm để in thông tin
    load_books_and_ratings(books_file, ratings_file)