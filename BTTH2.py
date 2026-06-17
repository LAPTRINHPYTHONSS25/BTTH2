class NetflixAccount:
    # 1. Class Attributes
    platform_name = "Netflix"
    max_profiles = 5

    def __init__(self, email):
        self.email = email
        self.__password = ""
        self.__plan = "Basic"
        self.profiles = []

    # 3. Tính đóng gói (@property & setter)
    @property
    def password(self):
        # Chỉ trả về chuỗi ẩn danh
        return "********"

    @password.setter
    def password(self, value):
        if len(value) < 6:
            raise ValueError("Password is too short")
        self.__password = value

    @property
    def plan(self):
        return self.__plan

    # 4. Class Method & Static Method
    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email

    @classmethod
    def update_max_profiles(cls, new_limit):
        cls.max_profiles = new_limit

    # 5. Instance Methods
    def add_profile(self, profile_name):
        if len(self.profiles) >= NetflixAccount.max_profiles:
            print("Đã đạt giới hạn số lượng Profile trên tài khoản này.")
        else:
            self.profiles.append(profile_name)
            print(f"Đã thêm profile: {profile_name}")

    def upgrade_plan(self, new_plan):
        valid_plans = ["Basic", "Standard", "Premium"]
        if new_plan in valid_plans:
            self.__plan = new_plan
            print(f"Gói cước đã được nâng cấp lên: {new_plan}")
        else:
            print("Gói cước không hợp lệ.")

    def display_info(self):
        print(f"\n--- Thông tin tài khoản {self.platform_name} ---")
        print(f"Email: {self.email}")
        print(f"Mật khẩu: {self.password}")
        print(f"Gói cước: {self.plan}")
        print(f"Profiles: {', '.join(self.profiles) if self.profiles else 'Chưa có'}")

# --- Hệ thống Menu CLI ---
def run_netflix_manager():
    current_account = None

    while True:
        print("\n===== NETFLIX ACCOUNT MANAGER =====")
        print("1. Đăng ký tài khoản mới\n2. Xem thông tin tài khoản\n3. Thêm người xem\n4. Nâng cấp gói cước\n5. Cập nhật chính sách Netflix\n6. Thoát")
        choice = input("Chọn chức năng (1-6): ")

        if choice == '1':
            email = input("Nhập email: ")
            if NetflixAccount.validate_email(email):
                current_account = NetflixAccount(email)
                while True:
                    try:
                        pwd = input("Nhập mật khẩu (>= 6 ký tự): ")
                        current_account.password = pwd
                        print("Đăng ký thành công!")
                        break
                    except ValueError as e:
                        print(f"Lỗi: {e}. Vui lòng nhập lại.")
            else:
                print("Email không hợp lệ, vui lòng chứa ký tự '@' và '.'")

        elif choice in ['2', '3', '4']:
            if current_account is None:
                print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
            else:
                if choice == '2':
                    current_account.display_info()
                elif choice == '3':
                    name = input("Nhập tên Profile: ")
                    current_account.add_profile(name)
                elif choice == '4':
                    plan = input("Chọn gói (Basic/Standard/Premium): ")
                    current_account.upgrade_plan(plan.capitalize())

        elif choice == '5':
            new_limit = int(input("Nhập số lượng Profile tối đa mới: "))
            NetflixAccount.update_max_profiles(new_limit)
            print(f"Đã cập nhật giới hạn Profile toàn hệ thống thành {new_limit}")

        elif choice == '6':
            print("Tạm biệt!")
            break

if __name__ == "__main__":
    run_netflix_manager()