      
# code sau khi sửa

branch_count = int(input("Nhập số lượng chi nhánh: "))
month_count = 3

for branch in range(1, branch_count + 1):
    for month in range(1, month_count + 1):
        revenue = int(input(f"Nhập doanh thu Chi nhánh {branch}, tháng {month}: "))
        print(f"Chi nhánh {branch}, tháng {month}: {revenue} triệu đồng")

# Báo cáo không gom theo từng chi nhánh vì vòng lặp đang bị đảo: bạn duyệt tháng theo số chi nhánh và chi nhánh theo số tháng, 
# nên dữ liệu nhập vào không theo đúng cấu trúc nghiệp vụ.

# Theo yêu cầu gom dữ liệu theo chi nhánh: vòng lặp ngoài phải duyệt theo chi nhánh.

# Mỗi chi nhánh có nhiều tháng, nên vòng lặp trong duyệt theo tháng
