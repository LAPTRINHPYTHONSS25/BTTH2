class BankAccount:
    # Class attributes
    bank_name = "Vietcombank"
    transaction_fee = 2000

    def __init__(self, account_number, account_name):
        self.account_number = account_number
        self.account_name = account_name
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        if not value or value.strip() == "":
            print("Tên tài khoản không được để trống")
        else:
            self._account_name = value.strip().upper()

    @staticmethod
    def validate_account_number(account_number):
        return account_number.isdigit() and len(account_number) == 10

    @classmethod
    def update_transaction_fee(cls, new_fee):
        if new_fee < 0:
            print("Phí giao dịch không được âm")
            return False
        cls.transaction_fee = new_fee
        return True

    def deposit(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return
        self.__balance += amount
        print(f"Nạp tiền thành công: +{amount:,} VND")

    def withdraw(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return
        total_deduction = amount + self.transaction_fee
        if self.__balance < total_deduction:
            print("Giao dịch thất bại. Số dư không đủ để thanh toán số tiền và phí giao dịch")
        else:
            self.__balance -= total_deduction
            print(f"Rút tiền thành công: -{amount:,} VND")
            print(f"Phí giao dịch: {self.transaction_fee:,} VND")

    def display_info(self):
        print(f"Ngân hàng: {self.bank_name}")
        print(f"Số tài khoản: {self.account_number}")
        print(f"Tên chủ tài khoản: {self.account_name}")
        print(f"Số dư hiện tại: {self.balance:,} VND")
        print(f"Phí giao dịch: {self.transaction_fee:,} VND")

# --- Hệ thống Menu ---
def run_system():
    current_account = None
    
    while True:
        print("\n===== VIETCOMBANK DIGIBANK SIMULATOR =====")
        print("1. Mở tài khoản mới\n2. Xem thông tin tài khoản\n3. Giao dịch Nạp / Rút tiền\n4. Cập nhật Tên chủ tài khoản\n5. Đổi phí giao dịch hệ thống\n6. Thoát chương trình")
        choice = input("Chọn chức năng (1-6): ")

        if choice == '1':
            acc_num = input("Nhập số tài khoản 10 chữ số: ")
            if BankAccount.validate_account_number(acc_num):
                name = input("Nhập tên chủ tài khoản: ")
                current_account = BankAccount(acc_num, name)
                print("Mở tài khoản thành công!")
            else:
                print("Số tài khoản không hợp lệ! Số tài khoản phải gồm đúng 10 chữ số.")

        elif choice in ['2', '3', '4']:
            if current_account is None:
                print("Hệ thống chưa có thông tin tài khoản. Vui lòng mở tài khoản ở Chức năng 1 trước.")
            else:
                if choice == '2':
                    current_account.display_info()
                elif choice == '3':
                    trans_type = input("1. Nạp tiền\n2. Rút tiền\nChọn loại giao dịch (1-2): ")
                    amount = int(input("Nhập số tiền giao dịch: "))
                    if trans_type == '1': current_account.deposit(amount)
                    elif trans_type == '2': current_account.withdraw(amount)
                    print(f"Số dư mới: {current_account.balance:,} VND")
                elif choice == '4':
                    new_name = input("Nhập tên mới: ")
                    current_account.account_name = new_name
                    print(f"Cập nhật thành công. Tên mới: {current_account.account_name}")

        elif choice == '5':
            print(f"Phí giao dịch hiện tại: {BankAccount.transaction_fee:,} VND")
            new_fee = int(input("Nhập phí giao dịch mới: "))
            if BankAccount.update_transaction_fee(new_fee):
                print(f"Đã cập nhật phí giao dịch toàn hệ thống thành {new_fee:,} VND")

        elif choice == '6':
            print("Cảm ơn bạn đã sử dụng Vietcombank Digibank!")
            break

run_system()