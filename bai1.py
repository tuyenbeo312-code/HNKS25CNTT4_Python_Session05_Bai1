      
branch_count = int(input("Nhập số lượng chi nhánh: "))
month_count = 3

# Danh sách lưu doanh thu
revenues = []

# Nhập dữ liệu
for branch in range(1, branch_count + 1):
    branch_data = []

    for month in range(1, month_count + 1):
        revenue = int(input(f"Nhập doanh thu Chi nhánh {branch}, tháng {month}: "))
        branch_data.append(revenue)

    revenues.append(branch_data)

# In báo cáo sau khi nhập xong
print("\n----- Kết quả -----")

for branch in range(branch_count):
    for month in range(month_count):
        print(
            f"Chi nhánh {branch + 1}, tháng {month + 1}: "
            f"{revenues[branch][month]} triệu đồng"
              
# Phân tích lỗi:
# Code cũ bị sai vì duyệt theo tháng trước,
# nên báo cáo không gom theo từng chi nhánh.

# Đúng nghiệp vụ:
# - Vòng lặp ngoài: duyệt chi nhánh
# - Vòng lặp trong: duyệt tháng
