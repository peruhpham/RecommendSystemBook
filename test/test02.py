import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Dữ liệu mẫu về sách và mô tả
books_metadata = {
    'Book1': 'Khoa học viễn tưởng, không gian, phiêu lưu',
    'Book2': 'Lịch sử Việt Nam, thời kỳ cổ, chiến tranh',
    'Book3': 'Trinh thám, bí ẩn, điều tra',
    'Book4': 'Tâm lý học, con người, xã hội',
    'Book5': 'Tiểu thuyết, tình yêu, lãng mạn',
}

# Dữ liệu mẫu về đánh giá của người dùng
user_ratings = {
    'User A': {'Book1': 5, 'Book3': 4, 'Book5': 3},
    'User B': {'Book2': 4, 'Book4': 5},
    'User C': {'Book5': 5, 'Book3': 4},
    'User D': {'Book1': 3, 'Book2': 2, 'Book4': 4},
}

def content_based_filtering(user, books_metadata, user_ratings):
    # Tạo vector TF-IDF từ mô tả sách
    vectorizer = TfidfVectorizer()
    book_vectors = vectorizer.fit_transform(books_metadata.values())
    book_titles = list(books_metadata.keys())

    # Lấy các sách mà người dùng đã đánh giá
    user_books = user_ratings.get(user, {})
    user_profile = None

    # Tổng hợp vector đặc trưng của các sách đã đánh giá
    for book, rating in user_books.items():
        idx = book_titles.index(book)
        book_vector = book_vectors[idx].toarray()[0]
        weighted_vector = rating * book_vector
        user_profile = weighted_vector if user_profile is None else user_profile + weighted_vector

    # Kiểm tra hồ sơ người dùng
    if user_profile is None:
        print(f"Người dùng {user} chưa có lịch sử đánh giá. Không thể tạo gợi ý.")
        return []

    # Xử lý NaN và định dạng lại hồ sơ
    import numpy as np
    user_profile = np.nan_to_num(user_profile).reshape(1, -1)

    # Tính độ tương đồng giữa hồ sơ người dùng và các sách
    similarities = []
    for idx, book_vector in enumerate(book_vectors):
        similarity = cosine_similarity(user_profile, [book_vector.toarray()[0]])[0][0]
        similarities.append((book_titles[idx], similarity))

    # Sắp xếp sách theo độ tương đồng
    recommendations = sorted(similarities, key=lambda x: x[1], reverse=True)
    return recommendations

# Hàm hiển thị menu
def display_menu():
    print("\n----- Goodreads Simulator -----")
    print("1. Xem danh sách sách")
    print("2. Xem gợi ý sách dựa trên sở thích cá nhân")
    print("3. Tìm kiếm sách theo từ khóa")
    print("0. Thoát")

# Chương trình chính
def main():
    while True:
        display_menu()
        choice = input("\nLựa chọn của bạn: ")
        
        if choice == '1':  # Xem danh sách sách
            print("\nDanh sách sách:")
            for book, description in books_metadata.items():
                print(f"- {book}: {description}")

        elif choice == '2':  # Xem gợi ý sách
            user = input("\nNhập tên người dùng (ví dụ: User A): ")
            recommendations = content_based_filtering(user, books_metadata, user_ratings)
            print("\nGợi ý sách dựa trên sở thích:")
            for book, score in recommendations[:5]:  # Hiển thị top 5 gợi ý
                print(f"- {book} (Điểm tương đồng: {score:.2f})")

        elif choice == '3':  # Tìm kiếm sách theo từ khóa
            keyword = input("\nNhập từ khóa để tìm kiếm: ")
            results = [book for book, description in books_metadata.items() if keyword.lower() in description.lower()]
            if results:
                print("\nKết quả tìm kiếm:")
                for book in results:
                    print(f"- {book}: {books_metadata[book]}")
            else:
                print("\nKhông tìm thấy sách phù hợp với từ khóa.")

        elif choice == '0':  # Thoát chương trình
            print("\nCảm ơn bạn đã sử dụng hệ thống!")
            break

        else:
            print("\nLựa chọn không hợp lệ. Vui lòng thử lại.")

# Chạy chương trình
if __name__ == '__main__':
    main()