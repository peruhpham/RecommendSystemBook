from tkinter import Canvas, Frame, Label, Scrollbar



def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
    """Vẽ hình chữ nhật bo góc"""
    points = [
        x1 + radius, y1,
        x2 - radius, y1,
        x2, y1,  
        x2, y1 + radius,
        x2, y2 - radius,
        x2, y2,  
        x2 - radius, y2,
        x1 + radius, y2,
        x1, y2,  
        x1, y2 - radius,
        x1, y1 + radius,
        x1, y1
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)


def create_book_display(root):
    """
    Tạo giao diện hiển thị sách với viền bo tròn.

    Parameters:
    - root: Cửa sổ hoặc Frame chính để hiển thị các khung sách.

    Returns:
    - frames (list): Danh sách các Frame chứa nội dung sách.
    - text_labels (dict): Dictionary chứa Label hiển thị tiêu đề sách.
    - image_labels (dict): Dictionary chứa Label hiển thị ảnh bìa sách.
    """

    # Danh sách chứa các thành phần giao diện
    frames = []  # Lưu Frame chứa nội dung sách
    text_labels = {}  # Lưu Label tiêu đề sách
    image_labels = {}  # Lưu Label hiển thị ảnh bìa

    # Tạo khung hiển thị sách theo từng vị trí
    for i, x in enumerate(range(30, 1100 + 1, 150)):  # Khoảng cách giữa các khung là 200px
        # 1️⃣ Tạo Frame để chứa nội dung sách
        frame = Frame(root, width=130, height=210, bg="#FFFF99", highlightbackground="#FFFF00", highlightthickness=1)
        frame.place(x=x, y=180)  # Đặt vị trí khung sách

        # Thêm Frame vào danh sách để quản lý sau này
        frames.append(frame)

        # 2️⃣ Tạo Label hiển thị tiêu đề sách
        text_labels[i] = Label(
            frame,
            text="Book Title",
            font=("Arial", 7, "normal"),
            fg="blue",  # Thay đổi màu chữ ở đây (ví dụ: "blue")
            bg="#FFFF99",
            wraplength=120,
            justify="center"
        )
        text_labels[i].place(x=5, y=5, width=120, height=30)  # Đặt vị trí tiêu đề

        # 3️⃣ Tạo Label hiển thị ảnh bìa sách
        image_labels[i] = Label(
            frame, 
            bg="white", 
            relief="solid", 
            borderwidth=1)
        image_labels[i].place(x=5, y=40, width=120, height=160)  # Đặt vị trí hiển thị ảnh bìa

    # Trả về các danh sách để sử dụng trong chương trình chính
    return frames, text_labels, image_labels


