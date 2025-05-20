import pandas as pd

# Đọc dữ liệu từ tệp CSV
def load_data(file_path):
    """
    Đọc dữ liệu từ tệp CSV và trả về DataFrame.
    """
    try:
        data = pd.read_csv(file_path, encoding="utf-8")
        print(f"✅ Dữ liệu đã được tải thành công! Số lượng bản ghi: {len(data)}")
        return data
    except Exception as e:
        print(f"❌ Lỗi khi đọc tệp: {e}")
        return None

# Hiển thị thông tin cơ bản về dữ liệu
def display_data_info(data):
    """
    Hiển thị thông tin cơ bản về dữ liệu.
    """
    print("\n📊 Thông tin dữ liệu:")
    print(data.info())
    print("\n📋 Một số bản ghi đầu tiên:")
    print(data.head())

# Tìm kiếm sách theo tiêu đề
def search_books_by_title(data, title):
    """
    Tìm kiếm sách theo tiêu đề.
    """
    results = data[data["Book-Title"].str.contains(title, case=False, na=False)]
    if results.empty:
        print(f"❌ Không tìm thấy sách với tiêu đề chứa: '{title}'")
    else:
        print(f"✅ Tìm thấy {len(results)} sách với tiêu đề chứa: '{title}'")
        print(results[["ISBN", "Book-Title", "Book-Author", "Year-Of-Publication", "Publisher"]])

# Xuất dữ liệu ra tệp Excel
def export_to_excel(data, output_path):
    """
    Xuất dữ liệu ra tệp Excel.
    """
    try:
        data.to_excel(output_path, index=False, sheet_name="Books Data")
        print(f"✅ Dữ liệu đã được xuất ra tệp Excel tại: {output_path}")
    except Exception as e:
        print(f"❌ Lỗi khi xuất dữ liệu ra Excel: {e}")

# Hiển thị tất cả thông tin về sách
def display_all_books(data):
    """
    Hiển thị tất cả thông tin về sách.
    """
    print("\n📚 Tất cả thông tin về sách:")
    print(data.to_string(index=False))  # Hiển thị toàn bộ dữ liệu mà không in cột chỉ mục


# Chương trình chính
if __name__ == "__main__":
    # Đường dẫn đến tệp CSV
    file_path = "D:\dataBookRecommend\Books.csv"  # Thay bằng đường dẫn tệp của bạn

    # Tải dữ liệu
    books_data = load_data(file_path)

    if books_data is not None:
        # Hiển thị thông tin dữ liệu
        display_data_info(books_data)

        # Hiển thị tất cả thông tin về sách
        # display_all_books(books_data)

        # Tìm kiếm sách theo tiêu đề
        search_title = input("\n🔍 Nhập tiêu đề sách cần tìm: ")
        search_books_by_title(books_data, search_title)

        """# Xuất dữ liệu ra tệp Excel
        output_path = "books_output.xlsx"  # Thay bằng đường dẫn tệp Excel bạn muốn lưu
        export_to_excel(books_data, output_path)"""