# (1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP
# Input/Output của các hàm chính và hàm phụ trợ:

# display_students(student_list): Nhận list → In danh sách, không return.
# validate_score(score_input): Nhận str → Trả về float nếu hợp lệ, None nếu không hợp lệ.
# find_student_by_id(student_list, student_id): Nhận list và str → Trả về index (int) hoặc -1.
# add_student(student_list): Nhận list (sửa đổi trực tiếp) → Không return.
# update_score(student_list): Nhận list (sửa đổi trực tiếp) → Không return.
# get_rank(average_score): Nhận float → Trả về str ("Giỏi", "Khá", "Trung bình", "Yếu").
# evaluate_students(student_list): Nhận list → In đánh giá, không return.
# display_menu(): In menu, return lựa chọn int.

# Lý do tách thành nhiều hàm nhỏ:

# Tránh spaghetti code (một vòng lặp while hàng trăm dòng).
# Dễ đọc, dễ bảo trì, dễ test từng chức năng.
# Tái sử dụng code (ví dụ: validate_score và find_student_by_id được dùng ở nhiều nơi).
# Tuân thủ nguyên tắc Single Responsibility (mỗi hàm chỉ làm một việc).

# HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY
students = [
    {
        "student_id": "RA001",
        "name": "Nguyễn Văn A",
        "math_score": 8.5,
        "english_score": 7.0
    },
    {
        "student_id": "RA002",
        "name": "Trần Thị B",
        "math_score": 9.0,
        "english_score": 9.5
    }
]


def display_menu():
    """Hiển thị menu chính"""
    print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY =====")
    print("1. Hiển thị danh sách học viên")
    print("2. Thêm học viên mới")
    print("3. Cập nhật điểm thi theo mã học viên")
    print("4. Đánh giá học lực của toàn bộ học viên")
    print("5. Thoát chương trình")
    print("====================================================")


def validate_score(score_input):
    """Kiểm tra điểm số hợp lệ (0-10)"""
    try:
        score = float(score_input)
        if 0 <= score <= 10:
            return score
        else:
            print("Điểm không hợp lệ, phải là số từ 0 đến 10.")
            return None
    except ValueError:
        print("Điểm không hợp lệ, phải là số từ 0 đến 10.")
        return None


def find_student_by_id(student_list, student_id):
    """Tìm học viên theo mã, trả về index hoặc -1"""
    for index, student in enumerate(student_list):
        if student["student_id"] == student_id:
            return index
    return -1


def display_students(student_list):
    """Chức năng 1: Hiển thị danh sách học viên"""
    if not student_list:
        print("Danh sách học viên hiện đang trống.")
        return
    
    print("\n--- DANH SÁCH HỌC VIÊN ---")
    for i, student in enumerate(student_list, 1):
        print(f"{i}. Mã: {student['student_id']} | Tên: {student['name']} | "
              f"Toán: {student['math_score']} | Anh: {student['english_score']}")


def add_student(student_list):
    """Chức năng 2: Thêm học viên mới"""
    print("\n--- THÊM HỌC VIÊN MỚI ---")
    
    # Nhập mã học viên
    while True:
        student_id = input("Mã Học Viên: ").strip().upper()
        if not student_id:
            print("Mã học viên không được để trống!")
            continue
        if find_student_by_id(student_list, student_id) != -1:
            print("Mã học viên đã tồn tại, vui lòng nhập mã khác!")
            continue
        break
    
    # Nhập tên
    while True:
        name = input("Tên Học Viên: ").strip()
        if not name:
            print("Tên học viên không được để trống!")
            continue
        name = name.title()  # Viết hoa chữ cái đầu mỗi từ
        break
    
    # Nhập điểm Toán
    while True:
        math_input = input("Nhập Điểm Toán: ")
        math_score = validate_score(math_input)
        if math_score is not None:
            break
    
    # Nhập điểm Anh
    while True:
        eng_input = input("Nhập Điểm Anh: ")
        english_score = validate_score(eng_input)
        if english_score is not None:
            break
    
    # Thêm vào danh sách
    new_student = {
        "student_id": student_id,
        "name": name,
        "math_score": math_score,
        "english_score": english_score
    }
    student_list.append(new_student)
    print("Thêm học viên thành công!")


def update_score(student_list):
    """Chức năng 3: Cập nhật điểm thi"""
    print("\n--- CẬP NHẬT ĐIỂM THI ---")
    student_id = input("Nhập mã học viên cần cập nhật: ").strip().upper()
    
    index = find_student_by_id(student_list, student_id)
    if index == -1:
        print(f"Không tìm thấy học viên mang mã {student_id}!")
        return
    
    print(f"Đang cập nhật cho: {student_list[index]['name']}")
    
    # Cập nhật điểm Toán
    while True:
        math_input = input("Nhập Điểm Toán mới: ")
        math_score = validate_score(math_input)
        if math_score is not None:
            break
    
    # Cập nhật điểm Anh
    while True:
        eng_input = input("Nhập Điểm Anh mới: ")
        english_score = validate_score(eng_input)
        if english_score is not None:
            break
    
    student_list[index]["math_score"] = math_score
    student_list[index]["english_score"] = english_score
    print("Cập nhật điểm thành công!")


def get_rank(average_score):
    """Hàm phụ trợ: Xếp loại học lực"""
    if average_score >= 8.0:
        return "Giỏi"
    elif average_score >= 6.5:
        return "Khá"
    elif average_score >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"


def evaluate_students(student_list):
    """Chức năng 4: Đánh giá học lực"""
    if not student_list:
        print("Danh sách học viên hiện đang trống.")
        return
    
    print("\n--- ĐÁNH GIÁ HỌC LỰC ---")
    for student in student_list:
        avg = (student["math_score"] + student["english_score"]) / 2
        rank = get_rank(avg)
        print(f"Mã: {student['student_id']} | Tên: {student['name']} | "
              f"ĐTB: {avg:.2f} | Xếp loại: {rank}")


# ===================== MAIN PROGRAM =====================
def main():
    while True:
        display_menu()
        choice = input("Nhập lựa chọn (1-5): ").strip()
        
        if choice == "1":
            display_students(students)
        elif choice == "2":
            add_student(students)
        elif choice == "3":
            update_score(students)
        elif choice == "4":
            evaluate_students(students)
        elif choice == "5":
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")


# Chạy chương trình
if __name__ == "__main__":
    main()