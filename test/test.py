import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.impute import SimpleImputer

# Dữ liệu mẫu: Ma trận người dùng - sách
data = {
    'User': ['A', 'B', 'C', 'D'],
    'Book1': [5, 4, None, 3],
    'Book2': [3, None, 4, None],
    'Book3': [None, 2, 5, 4],
    'Book4': [4, 5, None, 3],
}

# Chuyển dữ liệu thành DataFrame
df = pd.DataFrame(data).set_index('User')

# Xử lý thiếu dữ liệu (impute)
imputer = SimpleImputer(strategy='mean')
df_filled = pd.DataFrame(imputer.fit_transform(df), columns=df.columns, index=df.index)

# Tính độ tương đồng cosine giữa các người dùng
similarity_matrix = cosine_similarity(df_filled)
similarity_df = pd.DataFrame(similarity_matrix, index=df.index, columns=df.index)

print("Ma trận độ tương đồng giữa người dùng:")
print(similarity_df)

# Gợi ý cho người dùng cụ thể (ví dụ: User A)
target_user = 'A'
neighbors = similarity_df[target_user].sort_values(ascending=False).index[1:]  # Loại chính mình ra

# Gợi ý sách chưa được đọc dựa trên hàng xóm
recommendations = {}
for neighbor in neighbors:
    neighbor_ratings = df.loc[neighbor]
    for book, rating in neighbor_ratings.items():
        if pd.isna(df.loc[target_user, book]) and not pd.isna(rating):
            recommendations[book] = recommendations.get(book, 0) + rating * similarity_df.loc[target_user, neighbor]

# Sắp xếp sách được gợi ý
sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)

print("\nDanh sách gợi ý sách cho User A:")
for book, score in sorted_recommendations:
    print(f"{book}: Điểm gợi ý = {score:.2f}")