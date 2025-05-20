import time
import csv


class BookNode:
    """
    Một nút trong danh sách liên kết, lưu trữ thông tin về một cuốn sách.
    """
    def __init__(self, isbn, title, author, year, publisher, img_s, img_m, img_l):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher
        self.img_s = img_s
        self.img_m = img_m
        self.img_l = img_l
        self.next = None  # Con trỏ đến nút tiếp theo


class BookLinkedList:
    """
    Danh sách liên kết để lưu trữ thông tin sách.
    """
    def __init__(self):
        self.head = None  # Nút đầu tiên trong danh sách
        self.tail = None  # Nút cuối cùng trong danh sách

    def append(self, isbn, title, author, year, publisher, img_s, img_m, img_l):
        """
        Thêm một cuốn sách vào cuối danh sách liên kết.
        """
        new_node = BookNode(isbn, title, author, year, publisher, img_s, img_m, img_l)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def display_all_books(self):
        """
        Hiển thị tất cả thông tin sách trong danh sách liên kết.
        """
        current = self.head
        if not current:
            print("❌ Danh sách sách trống!")
            return

        print("\n📚 Tất cả thông tin về sách:")
        while current:
            print(f"ISBN: {current.isbn}, Title: {current.title}, Author: {current.author}, "
                  f"Year: {current.year}, Publisher: {current.publisher}, "
                  f"Image-S: {current.img_s}, Image-M: {current.img_m}, Image-L: {current.img_l}")
            current = current.next

    def count_books(self):
        """
        Đếm số lượng sách trong danh sách liên kết.
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        print(f"\n📚 Tổng số lượng sách: {count}")
        return count

    # def search_books_by_title(self, title):
    #     """
    #     Tìm kiếm sách theo tiêu đề.
    #     """
    #     current = self.head
    #     found = False
    #     print(f"\n🔍 Kết quả tìm kiếm cho tiêu đề chứa: '{title}'")
    #     while current:
    #         if title.lower() in current.title.lower():
    #             print(f"ISBN: {current.isbn}, Title: {current.title}, Author: {current.author}, "
    #                   f"Year: {current.year}, Publisher: {current.publisher}")
    #             found = True
    #         current = current.next
    #     if not found:
    #         print(f"❌ Không tìm thấy sách với tiêu đề chứa: '{title}'")
    def search_books_by_title(self, title):
        """
        Tìm kiếm sách theo tiêu đề và hiển thị kết quả dưới dạng bảng, 
        căn chỉnh độ rộng của từng cột dựa trên dữ liệu dài nhất.
        """
        if not title or not isinstance(title, str):
            print("❌ Tiêu đề tìm kiếm không hợp lệ. Vui lòng nhập một chuỗi không rỗng.")
            return

        current = self.head
        results = []

        # Khởi tạo độ rộng tối thiểu của các cột (bao gồm tiêu đề cột)
        max_lengths = {
            "STT": len("STT"),
            "Title": len("Title"),
            "Author": len("Author"),
            "Year": len("Year"),
            "Publisher": len("Publisher")
        }

        # Thu thập kết quả và tính toán chiều dài dữ liệu lớn nhất trong mỗi cột
        while current:
            if title.lower() in current.title.lower():
                results.append({
                    "STT": len(results) + 1,
                    "Title": current.title,
                    "Author": current.author,
                    "Year": str(current.year),
                    "Publisher": current.publisher
                })
                max_lengths["Title"] = max(max_lengths["Title"], len(current.title))
                max_lengths["Author"] = max(max_lengths["Author"], len(current.author))
                max_lengths["Year"] = max(max_lengths["Year"], len(str(current.year)))
                max_lengths["Publisher"] = max(max_lengths["Publisher"], len(current.publisher))
            current = current.next

        # Hiển thị kết quả
        if results:
            # Tạo dòng ngang phân cách với độ dài tổng của tất cả các cột
            total_width = sum(max_lengths.values()) + len(max_lengths) * 3 + 1
            print(f"\n       Danh sách sách chứa: '{title}'       ")
            print("=" * total_width)

            # In tiêu đề cột với chiều rộng đã căn chỉnh
            print(f"{'STT':<{max_lengths['STT']}}   "
                f"{'Title':<{max_lengths['Title']}}   "
                f"{'Author':<{max_lengths['Author']}}   "
                f"{'Year':<{max_lengths['Year']}}   "
                f"{'Publisher':<{max_lengths['Publisher']}}")
            print("-" * total_width)

            # In từng dòng dữ liệu
            for book in results:
                print(f"{book['STT']:<{max_lengths['STT']}}   "
                    f"{book['Title']:<{max_lengths['Title']}}   "
                    f"{book['Author']:<{max_lengths['Author']}}   "
                    f"{book['Year']:<{max_lengths['Year']}}   "
                    f"{book['Publisher']:<{max_lengths['Publisher']}}")
            print("=" * total_width)
            print(f"✅ Tổng số sách tìm thấy: {len(results)}")
        else:
            print(f"❌ Không tìm thấy sách với tiêu đề chứa: '{title}'")




def load_data_to_linked_list(file_path):
    """
    Đọc dữ liệu từ tệp CSV và thêm vào danh sách liên kết.
    """
    print(f"📥 Đang tải dữ liệu từ tệp: {file_path}")
    book_list = BookLinkedList()
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # Bỏ qua dòng tiêu đề
            for fields in reader:
                isbn = fields[0]
                title = fields[1]
                author = fields[2]
                year = fields[3]
                publisher = fields[4]
                img_s = fields[5]
                img_m = fields[6]
                img_l = fields[7]
                book_list.append(isbn, title, author, year, publisher, img_s, img_m, img_l)
        print("✅ Dữ liệu đã được tải vào danh sách liên kết!")
    except Exception as e:
        print(f"❌ Lỗi khi đọc tệp: {e}")
    return book_list


if __name__ == "__main__":
    # Đường dẫn đến tệp CSV
    file_path = "D:\\dataBookRecommend\\Books.csv"  # Thay bằng đường dẫn tệp của bạn

    # Tải dữ liệu vào danh sách liên kết
    start_time = time.time()
    book_list = load_data_to_linked_list(file_path)
    end_time = time.time()
    print(f"⏱️ Thời gian tải dữ liệu: {end_time - start_time:.2f} giây")

    # Hiển thị tất cả thông tin sách
    # book_list.display_all_books()

    # Đếm số lượng sách
    book_list.count_books()

    # Tìm kiếm sách theo tiêu đề
    search_title = input("\n🔍 Nhập tiêu đề sách cần tìm: ")
    book_list.search_books_by_title(search_title)