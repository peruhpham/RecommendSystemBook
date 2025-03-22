
from tkinter import *
from tkinter import messagebox, filedialog
from tkinter import ttk
import pandas as pd
import openpyxl

# Node chứa thông tin của một quyển sách
class Book:
    def __init__(self, title=None, author=None, year=None):
        self.title = title
        self.author = author
        self.year = year
        self.next = None  # Con trỏ đến sách tiếp theo

# Danh sách liên kết đơn để quản lý sách
class BookList:
    def __init__(self):
        self.head = None  # Điểm bắt đầu của danh sách

    def append(self, title, author, year):
        new_book = Book(title, author, year)
        if not self.head:
            self.head = new_book
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_book

    def to_list(self):
        books = []
        current = self.head
        while current:
            books.append({"Title": current.title, "Author": current.author, "Year": current.year})
            current = current.next
        return books

    def display(self, listbox):
        listbox.delete(0, END)
        current = self.head
        while current:
            listbox.insert(END, f"{current.title} - {current.author} ({current.year})")
            current = current.next

class BookDataManagement:
    def __init__(self, parent):
        self.parent = parent
        self.books = BookList()
        self.create_ui_data()

    def create_ui_data(self):
        self.ui_data_window = Toplevel(self.parent)
        self.ui_data_window.title("UI Data Management")
        self.ui_data_window.geometry("900x600")
        # Đặt icon cho cửa sổ
        try:
            self.icon_image = PhotoImage(file="images/icon.png")  # Đảm bảo đường dẫn đúng
            self.ui_data_window.iconphoto(False, self.icon_image)  # Gọi iconphoto trên Toplevel
        except Exception as e:
            print(f"Lỗi đặt icon: {e}")
        self.ui_data_window.config(bg="#F0F0F0")

        self.style = ttk.Style(self.ui_data_window)
        try:
            self.ui_data_window.tk.call("source", r"D:\Project_Recommendation_Systems\tkinter_excel_app\forest-dark.tcl")
            self.ui_data_window.tk.call("source", r"D:\Project_Recommendation_Systems\tkinter_excel_app\forest-light.tcl")
        except TclError as e:
            print(f"Lỗi tcl: {e}")

        self.style.theme_use("forest-dark")

        # Tạo nút chuyển đổi chế độ sáng/tối
        self.mode_switch = ttk.Checkbutton(
            self.ui_data_window,
            text="Chế độ sáng/tối",
            command=self.toggle_mode,
        )
        self.mode_switch.state(["!alternate"])  # Đảm bảo trạng thái mặc định
        self.mode_switch.pack(anchor="ne", padx=10, pady=10)

        # Frame chính
        frame = ttk.Frame(self.ui_data_window)
        frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        widgets_frame = ttk.LabelFrame(frame, text="Quản lý dữ liệu")
        widgets_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.name_entry = ttk.Entry(widgets_frame)
        self.name_entry.insert(0, "Name book")
        self.name_entry.bind("<FocusIn>", lambda e: self.name_entry.delete(0, 'end'))
        self.name_entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.author_spinbox = ttk.Spinbox(widgets_frame, from_=18, to=100)
        self.author_spinbox.insert(0, "Author")
        self.author_spinbox.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        self.combo_list = ["*****", "****", "***", "**", "*"]
        self.status_combobox = ttk.Combobox(widgets_frame, values=self.combo_list)
        self.status_combobox.current(0)
        self.status_combobox.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        self.employed_var = BooleanVar()
        self.checkbutton = ttk.Checkbutton(widgets_frame, text="Employed", variable=self.employed_var)
        self.checkbutton.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

        insert_button = ttk.Button(widgets_frame, text="Thêm", command=self.insert_to_treeview)
        insert_button.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

        delete_button = ttk.Button(widgets_frame, text="Xóa", command=self.delete_selected_row)
        delete_button.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

        export_button = ttk.Button(widgets_frame, text="Xuất Excel", command=self.export_to_excel)
        export_button.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")

        tree_frame = ttk.Frame(frame)
        tree_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        tree_scroll = ttk.Scrollbar(tree_frame)
        tree_scroll.pack(side="right", fill="y")

        cols = ("Name", "Author", "Rating", "Genre")
        self.treeview = ttk.Treeview(tree_frame, show="headings", columns=cols, yscrollcommand=tree_scroll.set)
        for col in cols:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, width=150)
        self.treeview.pack(fill=BOTH, expand=True)
        tree_scroll.config(command=self.treeview.yview)

    def toggle_mode(self):
        if self.mode_switch.instate(["selected"]):
            self.style.theme_use("forest-light")
        else:
            self.style.theme_use("forest-dark")

    def insert_to_treeview(self):
        name = self.name_entry.get().strip()
        author = self.author_spinbox.get().strip()
        subscription = self.status_combobox.get().strip()
        employment_status = "Yes" if self.employed_var.get() else "No"

        if not name or not author:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập tên và tuổi hợp lệ!")
            return

        self.treeview.insert("", "end", values=(name, author, subscription, employment_status))
        self.name_entry.delete(0, "end")
        self.name_entry.insert(0, "Name")
        self.author_spinbox.delete(0, "end")
        self.author_spinbox.insert(0, "Author")
        self.status_combobox.current(0)
        self.checkbutton.state(["!selected"])

    def delete_selected_row(self):
        selected_item = self.treeview.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn hàng cần xóa!")
            return
        self.treeview.delete(selected_item)

    def export_to_excel(self):
        path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
        if path:
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            sheet.title = "Data"
            cols = ("Name", "Author", "Rating", "Genres")
            sheet.append(cols)
            for child in self.treeview.get_children():
                sheet.append(self.treeview.item(child)["values"])
            workbook.save(path)
            messagebox.showinfo("Thông báo", f"Dữ liệu đã được xuất ra tệp Excel tại {path}")

