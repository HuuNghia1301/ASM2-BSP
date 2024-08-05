import pandas as pd
import matplotlib.pyplot as plt

# Đường dẫn đến tệp CSV
customer_file_path = 'C:/Users/ASUS/Desktop/py/ASM1-PowerBI-main/customer_table.csv'
website_access_file_path = 'C:/Users/ASUS/Desktop/py/ASM1-PowerBI-main/Website_Access_Category_Table.csv'
product_file_path = 'C:/Users/ASUS/Desktop/py/ASM1-PowerBI-main/Product_detail_table.csv'

# Đọc dữ liệu từ file CSV
try:
    customer_df = pd.read_csv(customer_file_path)
    website_access_df = pd.read_csv(website_access_file_path)
    product_df = pd.read_csv(product_file_path)
except Exception as e:
    print(f"Error reading CSV files: {e}")

# Kiểm tra các cột trong bảng dữ liệu
print("Customer Table Columns:", customer_df.columns)
print("Website Access Category Table Columns:", website_access_df.columns)
print("Product Table Columns:", product_df.columns)

# Biểu đồ phân phối theo giới tính cho từng thành phố
try:
    if 'City' in customer_df.columns and 'Gender' in customer_df.columns:
        gender_city_df = customer_df.groupby(['City', 'Gender']).size().unstack().fillna(0)
        gender_city_df.plot(kind='bar', stacked=True, figsize=(14, 8), color=['skyblue', 'salmon'])

        plt.title('Phân phối theo giới tính cho từng thành phố')
        plt.xlabel('Thành phố')
        plt.ylabel('Số lượng')
        plt.legend(title='Giới tính')
        plt.grid(axis='y')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    else:
        print("Columns 'City' and/or 'Gender' are missing in customer_df.")
except Exception as e:
    print(f"Error plotting gender distribution by city: {e}")

# Biểu đồ phân phối theo mức độ thành viên
try:
    if 'MembershipLevel' in customer_df.columns:
        plt.figure(figsize=(10, 5))
        customer_df['MembershipLevel'].value_counts().plot(kind='bar', color='salmon')
        plt.title('Phân phối theo mức độ thành viên')
        plt.xlabel('Mức độ thành viên')
        plt.ylabel('Số lượng')
        plt.grid(axis='y')
        plt.show()
    else:
        print("Column 'MembershipLevel' is missing in customer_df.")
except Exception as e:
    print(f"Error plotting membership level distribution: {e}")

# Biểu đồ phân phối theo loại trình duyệt
try:
    if 'BrowserType' in website_access_df.columns:
        website_access_df = website_access_df.dropna(subset=['BrowserType'])

        plt.figure(figsize=(8, 5))
        website_access_df['BrowserType'].value_counts().plot(kind='bar', color='teal')
        plt.title('Phân phối theo loại trình duyệt')
        plt.xlabel('Loại trình duyệt')
        plt.ylabel('Số lượng')
        plt.grid(axis='y')
        plt.show()
    else:
        print("Column 'BrowserType' is missing in website_access_df.")
except Exception as e:
    print(f"Error plotting browser type distribution: {e}")

# Biểu đồ phân phối sản phẩm
try:
    if 'ProductName' in product_df.columns:
        plt.figure(figsize=(12, 6))
        product_df['ProductName'].value_counts().plot(kind='bar', color='lightblue')
        plt.title('Phân phối sản phẩm')
        plt.xlabel('Tên sản phẩm')
        plt.ylabel('Số lượng')
        plt.grid(axis='y')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    else:
        print("Column 'ProductName' is missing in product_df.")
except Exception as e:
    print(f"Error plotting product distribution: {e}")
