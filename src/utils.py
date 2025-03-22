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
    - frames (list): Danh sách các Frame chứa thông tin sách.
    - text_labels (dict): Dictionary chứa Label hiển thị tiêu đề sách.
    - image_labels (dict): Dictionary chứa Label hiển thị ảnh bìa sách.
    """

    # Danh sách chứa các thành phần giao diện
    canvas_list = []  # Lưu Canvas để vẽ viền bo góc
    frames = []  # Lưu Frame chứa nội dung sách
    text_labels = {}  # Lưu Label tiêu đề sách
    image_labels = {}  # Lưu Label hiển thị ảnh bìa

    # Tạo khung hiển thị sách theo từng vị trí
    for i, x in enumerate(range(30, 960 + 1, 200)):  # Khoảng cách giữa các khung là 200px
        # 1️⃣ Tạo Canvas để vẽ hình chữ nhật bo góc
        # canvas = Canvas(root, width=150, height=240, bg="white", highlightthickness=0)
        # canvas.place(x=x, y=250)
        
        # Vẽ hình chữ nhật bo góc trên Canvas
        # create_rounded_rectangle(canvas, 0, 0, 150, 240, radius=20, fill="green", outline="black")

        # 2️⃣ Tạo Frame nằm trên Canvas để chứa nội dung sách
        frame = Frame(root, width=140, height=230, bg="white")
        frame.place(x=x + 5, y=255+100)  # Đặt lệch vào 5px để không bị trùng viền Canvas

        # Thêm Canvas và Frame vào danh sách để quản lý sau này
        # canvas_list.append(canvas)
        frames.append(frame)

        # 3️⃣ Tạo Label hiển thị tiêu đề sách
        text_labels[i] = Label(frame, text="Book Title", font=("arial", 10), fg="green", bg="white")
        text_labels[i].place(x=3, y=4)  # Đặt vị trí tiêu đề

        # 4️⃣ Tạo Label hiển thị ảnh bìa sách
        image_labels[i] = Label(frame, bg="white")
        image_labels[i].place(x=3, y=60)  # Đặt vị trí hiển thị ảnh

    # Trả về các danh sách để sử dụng trong chương trình chính
    return frames, text_labels, image_labels


