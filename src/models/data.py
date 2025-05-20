# Node save 1 movie
class Movie:
    def __init__(self, title=None, publishedDate=None, averageRating=None, url=None):
        self.title = title
        self.publishedDate = publishedDate
        self.averageRating = averageRating
        self.url = url
        self.next = None  # Con trỏ đến node tiếp theo


# List of movies that have singly linked list
class Movies:
    def __init__(self):
        self.head = None  # Điểm bắt đầu của danh sách liên kết

    # Thêm một bộ phim vào cuối danh sách liên kết
    def append(self, title, publishedDate, averageRating, url):
        new_movie = Movie(title, publishedDate, averageRating, url)
        if not self.head:
            self.head = new_movie  # Nếu danh sách rỗng, gán head là node mới
        else:
            current = self.head
            while current.next:
                current = current.next  # Duyệt đến node cuối cùng
            current.next = new_movie  # Gán node mới vào cuối danh sách

    # Hiển thị danh sách phim
    def display(self):
        current = self.head
        while current:
            print(f"Title: {current.title}, Date: {current.publishedDate}, Rating: {current.averageRating}, URL: {current.url}")
            current = current.next

    # Tìm kiếm phim theo tiêu đề
    def search(self, title):
        current = self.head
        while current:
            if current.title == title:
                return current
            current = current.next
        return None  # Không tìm thấy phim

    # Xóa một phim theo tiêu đề
    def delete(self, title):
        current = self.head
        prev = None
        while current:
            if current.title == title:
                if prev:
                    prev.next = current.next  # Bỏ qua node cần xóa
                else:
                    self.head = current.next  # Nếu là node đầu tiên, cập nhật head
                return True  # Xóa thành công
            prev = current
            current = current.next
        return False  # Không tìm thấy phim để xóa


if __name__ == "__main__":
    movies = Movies()
    
    movies.append("Inception", "2010", 8.8, "https://example.com/inception.jpg")
    movies.append("Interstellar", "2014", 8.6, "https://example.com/interstellar.jpg")
    movies.append("The Matrix", "1999", 8.7, "https://example.com/matrix.jpg")
    
    print("📌 Danh sách phim:")
    movies.display()
    
    print("\n🔍 Tìm phim 'Interstellar':")
    found_movie = movies.search("Interstellar")
    if found_movie:
        print(f"✅ Tìm thấy: {found_movie.title}, Rating: {found_movie.averageRating}")
    else:
        print("❌ Không tìm thấy phim!")

    print("\n🗑️ Xóa phim 'The Matrix':")
    if movies.delete("The Matrix"):
        print("✅ Đã xóa thành công!")
    else:
        print("❌ Không tìm thấy phim để xóa!")

    print("\n📌 Danh sách phim sau khi xóa:")
    movies.display()
