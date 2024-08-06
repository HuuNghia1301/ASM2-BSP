import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Đường dẫn đến tệp CSV
sale_file_path = "C:/Users/ASUS/Desktop/py/ASM1-PowerBI-main/Sale-Table.csv"
product_detail_file_path = "C:/Users/ASUS/Desktop/py/ASM1-PowerBI-main/Product_detail_table.csv"

# Đọc dữ liệu từ file CSV
try:
    sale_df = pd.read_csv(sale_file_path)
    product_detail_df = pd.read_csv(product_detail_file_path)
    print("CSV files read successfully.")
except Exception as e:
    print(f"Error reading CSV file: {e}")
    exit()

# Kiểm tra các cột trong bảng dữ liệu
print("Sale Data Columns:")
print(sale_df.columns)
print("Product Detail Data Columns:")
print(product_detail_df.columns)

# Kiểm tra các mẫu dữ liệu
print("Sale Data Sample:")
print(sale_df.head())
print("Product Detail Data Sample:")
print(product_detail_df.head())

# Hợp nhất hai bảng dữ liệu dựa trên cột 'ProductID' nếu cần
if 'ProductID' in sale_df.columns and 'ProductID' in product_detail_df.columns:
    merged_df = pd.merge(sale_df, product_detail_df, on='ProductID')
else:
    merged_df = sale_df  # Nếu không có ProductID, sử dụng sale_df trực tiếp

print("Merged Data Sample:")
print(merged_df.head())

# Chọn các cột tính năng và biến mục tiêu (cập nhật với các cột phù hợp từ dữ liệu hợp nhất)
# Thay 'Quantity' và 'Discount' bằng các cột tính năng thực tế trong dữ liệu của bạn
X = merged_df[['Quantity', 'Discount']]  # Các cột tính năng
y = merged_df['TotalAmount']  # Biến mục tiêu

# Kiểm tra sự hiện diện và tính hợp lệ của các cột
print("Features Sample:")
print(X.head())
print("Target Sample:")
print(y.head())

# Mô tả dữ liệu
print("Data Description:")
print(merged_df.describe())

# Chuyển đổi SaleDate thành định dạng datetime
merged_df['SaleDate'] = pd.to_datetime(merged_df['SaleDate'])

# Thêm cột ngày và tháng để phân tích
merged_df['Date'] = merged_df['SaleDate'].dt.date

# Chuẩn hóa dữ liệu
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test, date_train, date_test = train_test_split(
    X_scaled, y, merged_df['Date'], test_size=0.2, random_state=0
)

# Tạo đối tượng hồi quy tuyến tính và huấn luyện mô hình
model = LinearRegression()
model.fit(X_train, y_train)

# Dự đoán doanh số bán hàng
y_pred = model.predict(X_test)

# Đánh giá mô hình
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

# Tạo DataFrame kết quả dự đoán cho ngày bán hàng
results_df = pd.DataFrame({
    'Date': date_test,
    'Actual': y_test,
    'Predicted': y_pred
})

# Nhóm theo ngày và tính tổng doanh số thực tế và dự đoán cho mỗi ngày
daily_results = results_df.groupby('Date').agg({'Actual': 'sum', 'Predicted': 'sum'}).reset_index()

# Vẽ biểu đồ so sánh giữa doanh số thực tế và dự đoán theo ngày bán hàng
plt.figure(figsize=(12, 6))
plt.plot(daily_results['Date'], daily_results['Actual'], marker='o', color='blue', label='Doanh số thực tế')
plt.plot(daily_results['Date'], daily_results['Predicted'], marker='o', color='green', linestyle='--', label='Dự đoán')
plt.xlabel('Ngày bán hàng')
plt.ylabel('Tổng doanh số')
plt.title('So sánh giữa doanh số thực tế và dự đoán theo ngày bán hàng')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
