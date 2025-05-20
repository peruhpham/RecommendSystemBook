import requests
import urllib.parse


class Request:
    def __init__(self, method, args):
        self.args = args
        self.method = method


    def search_books(self):
        search_query = urllib.parse.quote(self.search_var.get())
        url = f"https://www.googleapis.com/books/v1/volumes?q={search_query}&maxResults=5"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            print(data)  # Xử lý dữ liệu sách ở đây
        else:
            messagebox.showinfo("Error", "Failed to fetch data from Google Books API.")
