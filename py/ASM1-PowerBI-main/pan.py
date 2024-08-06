import pandas as pd

def check_csv_errors(file_path, error_log_path):
    errors = []
    
    try:
        # Đọc dữ liệu từ file CSV vào DataFrame
        df = pd.read_csv(file_path, engine='python')
    except pd.errors.ParserError as e:
        errors.append(f"Đã gặp lỗi khi đọc file {file_path}: {e}")
        # Ghi thông báo lỗi vào file log và không xử lý tiếp
        with open(error_log_path, 'w', encoding='utf-8') as log_file:
            for error in errors:
                log_file.write(error + '\n')
        return

    # Số lượng cột dự kiến từ header
    expected_fields = len(df.columns)
    
    # Danh sách lưu các lỗi
    def fill_errors(row, index):
        filled_row = row.copy()
        if len(row) != expected_fields:
            errors.append(f"Lỗi ở dòng {index + 2}: Số lượng trường không khớp. Cần {expected_fields} trường, có {len(row)} trường.")
            # Điền 'Lỗi' vào các ô thiếu
            for i in range(len(row)):
                if pd.isnull(row[i]) or row[i] == '':
                    filled_row[i] = 'Lỗi'
            # Thêm thông tin về lỗi vào danh sách
            if len(row) < expected_fields:
                errors.append(f"Lỗi ở dòng {index + 2}: Thiếu cột(s) tại các chỉ số: {list(range(len(row), expected_fields))}.")
        return filled_row

    # Duyệt qua các dòng và kiểm tra lỗi
    fixed_rows = [fill_errors(df.iloc[i], i) for i in range(len(df))]
    fixed_df = pd.DataFrame(fixed_rows, columns=df.columns)
    
    # Ghi thông tin lỗi vào file log
    if errors:
        with open(error_log_path, 'w', encoding='utf-8') as log_file:
            for error in errors:
                log_file.write(error + '\n')
    else:
        with open(error_log_path, 'w', encoding='utf-8') as log_file:
            log_file.write("Không tìm thấy lỗi\n")
    
    print(f"Lỗi đã được ghi vào {error_log_path}")

# Danh sách các file cần kiểm tra
files = [
    "C:/Users/ASUS/Desktop/py/ASM1-PowerBI-main/Market_Trend_Table.csv",
    "C:/Users/ASUS/Desktop/py/ASM1-PowerBI-main/ProductGroupTable.csv",
    "C:/Users/ASUS/Desktop/py/ASM1-PowerBI-main/Product_detail_table.csv",
    "C:/Users/ASUS/Desktop/py/ASM1-PowerBI-main/Sale-Table.csv",
    "C:/Users/ASUS/Desktop/py/ASM1-PowerBI-main/Website_Access_Category_Table.csv",
    "C:/Users/ASUS/Desktop/py/ASM1-PowerBI-main/customer_table.csv",
]

for file in files:
    error_log_file = file.replace('.csv', '_errors.log')  # Tạo tên file log
    check_csv_errors(file, error_log_file)
