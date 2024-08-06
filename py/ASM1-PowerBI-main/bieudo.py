import pandas as pd
import matplotlib.pyplot as plt

# Đường dẫn đến tệp CSV
customer_file_path = 'C:/Users/ASUS/Desktop/py/ASM1-PowerBI-main/customer_table.csv'
website_access_file_path = 'C:/Users/ASUS/Desktop/py/ASM1-PowerBI-main/Website_Access_Category_Table.csv'
product_file_path = 'C:/Users/ASUS/Desktop/py/ASM1-PowerBI-main/Product_detail_table.csv'
product_group_file_path = 'C:/Users/ASUS/Desktop/py/ASM1-PowerBI-main/ProductGroupTable.csv'

# Đọc dữ liệu từ file CSV
try:
    customer_df = pd.read_csv(customer_file_path)
    website_access_df = pd.read_csv(website_access_file_path, on_bad_lines='skip')  # Bỏ qua các dòng lỗi
    product_df = pd.read_csv(product_file_path)
    product_group_df = pd.read_csv(product_group_file_path, on_bad_lines='skip')  # Bỏ qua các dòng lỗi
    print("CSV files read successfully.")
except Exception as e:
    print(f"Error reading CSV files: {e}")

# Kiểm tra các cột trong bảng dữ liệu
print("Customer Table Columns:", customer_df.columns)
print("Website Access Category Table Columns:", website_access_df.columns)
print("Product Table Columns:", product_df.columns)
print("Product Group Table Columns:", product_group_df.columns)

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

# Biểu đồ phân phối theo mức độ thành viên cho từng thành phố
try:
    if 'City' in customer_df.columns and 'MembershipLevel' in customer_df.columns:
        membership_city_df = customer_df.groupby(['City', 'MembershipLevel']).size().unstack().fillna(0)
        membership_city_df.plot(kind='bar', stacked=True, figsize=(14, 8), colormap='viridis')

        plt.title('Phân phối mức độ thành viên cho từng thành phố')
        plt.xlabel('Thành phố')
        plt.ylabel('Số lượng')
        plt.legend(title='Mức độ thành viên')
        plt.grid(axis='y')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    else:
        print("Columns 'City' and/or 'MembershipLevel' are missing in customer_df.")
except Exception as e:
    print(f"Error plotting membership level distribution by city: {e}")

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

# Kết hợp dữ liệu sản phẩm với nhóm sản phẩm
try:
    print("Product Group Table Columns:", product_group_df.columns)
    if 'ProductGroupID' in product_df.columns and 'ProductGroupID' in product_group_df.columns:
        # In mẫu dữ liệu để kiểm tra các giá trị hợp nhất
        print("Product Data Sample:")
        print(product_df.head())
        print("Product Group Data Sample:")
        print(product_group_df.head())

        # Đổi tên cột để hợp nhất
        product_group_df.rename(columns={'GroupID': 'ProductGroupID', 'GroupName': 'ProductGroup'}, inplace=True)
        merged_product_df = pd.merge(product_df, product_group_df, on='ProductGroupID')
        print("Merged Product Data Sample:")
        print(merged_product_df.head())

        # Kiểm tra sự tồn tại của cột 'ProductGroup' và 'Price'
        if 'ProductGroup' in merged_product_df.columns and 'Price' in merged_product_df.columns:
            # Biểu đồ phân phối sản phẩm theo giá và nhóm sản phẩm
            plt.figure(figsize=(12, 6))
            product_group_price = merged_product_df.groupby('ProductGroup')['Price'].mean()
            product_group_price.plot(kind='bar', figsize=(14, 8), color='skyblue')

            plt.title('Phân phối giá trung bình theo nhóm sản phẩm')
            plt.xlabel('Nhóm sản phẩm')
            plt.ylabel('Giá trung bình')
            plt.grid(axis='y')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()
        else:
            print("Columns 'ProductGroup' and/or 'Price' are missing in merged_product_df.")
    else:
        print("Columns 'ProductGroupID' are missing in product_df and/or product_group_df.")
except Exception as e:
    print(f"Error merging product data and plotting distribution: {e}")
