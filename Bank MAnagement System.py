class BankAccount:
    def __init__(self, account_number, customer_name, mobile_number,
                 email, account_type, branch_name, ifsc_code, initial_deposit):
        self.account_number  = account_number
        self.customer_name   = customer_name
        self.mobile_number   = mobile_number
        self.email           = email
        self.account_type    = account_type      # "Savings" / "Current"
        self.branch_name     = branch_name
        self.ifsc_code       = ifsc_code
        self.balance         = initial_deposit
        self.transaction_count = 0
        self.status          = "Active"          # "Active" / "Closed"
 
        # cumulative counters (for transaction summary)
        self.total_deposits    = initial_deposit
        self.total_withdrawals = 0
 
    def display(self):
        print("-" * 55)
        print(f"  Account Number  : {self.account_number}")
        print(f"  Customer Name   : {self.customer_name}")
        print(f"  Mobile Number   : {self.mobile_number}")
        print(f"  Email Address   : {self.email}")
        print(f"  Account Type    : {self.account_type}")
        print(f"  Branch Name     : {self.branch_name}")
        print(f"  IFSC Code       : {self.ifsc_code}")
        print(f"  Balance         : ₹{self.balance:,.2f}")
        print(f"  Transactions    : {self.transaction_count}")
        print(f"  Status          : {self.status}")
        print("-" * 55)
 
 
# ── global storage ──────────────────────────────────────
accounts = {}   # account_number -> BankAccount
 
 
# ── helpers ─────────────────────────────────────────────
def separator():
    print("=" * 55)
 
def get_account(acc_no):
    """Return account or None."""
    return accounts.get(acc_no)
 
def require_active(acc):
    """Return True if account is Active, else print error."""
    if acc.status == "Closed":
        print("  ✖  This account is CLOSED. Transaction not allowed.")
        return False
    return True
 
 
# ── menu operations ─────────────────────────────────────
 
def create_account():
    separator()
    print("         CREATE NEW ACCOUNT")
    separator()
    acc_no = input("  Account Number  : ").strip()
    if acc_no in accounts:
        print("  ✖  Account Number already exists!")
        return
 
    name   = input("  Customer Name   : ").strip()
    mobile = input("  Mobile Number   : ").strip()
    email  = input("  Email Address   : ").strip()
 
    print("  Account Type — 1. Savings   2. Current")
    choice = input("  Choose (1/2)    : ").strip()
    acc_type = "Savings" if choice == "1" else "Current"
 
    branch = input("  Branch Name     : ").strip()
    ifsc   = input("  IFSC Code       : ").strip()
 
    try:
        deposit = float(input("  Initial Deposit : ₹"))
    except ValueError:
        print("  ✖  Invalid amount.")
        return
 
    if deposit < 1000:
        print("  ✖  Initial deposit must be ≥ ₹1000.")
        return
 
    accounts[acc_no] = BankAccount(acc_no, name, mobile, email,
                                   acc_type, branch, ifsc, deposit)
    print(f"\n  ✔  Account created successfully! (Balance: ₹{deposit:,.2f})")
 
 
def view_all_accounts():
    separator()
    print("           ALL ACCOUNTS")
    separator()
    if not accounts:
        print("  No accounts found.")
        return
    for acc in accounts.values():
        acc.display()
 
 
def search_account():
    separator()
    print("           SEARCH ACCOUNT")
    separator()
    acc_no = input("  Enter Account Number : ").strip()
    acc = get_account(acc_no)
    if acc:
        acc.display()
    else:
        print("  ✖  Account not found.")
 
 
def deposit_money():
    separator()
    print("           DEPOSIT MONEY")
    separator()
    acc_no = input("  Account Number : ").strip()
    acc = get_account(acc_no)
    if not acc:
        print("  ✖  Account not found.")
        return
    if not require_active(acc):
        return
 
    try:
        amount = float(input("  Deposit Amount : ₹"))
    except ValueError:
        print("  ✖  Invalid amount.")
        return
 
    if amount <= 0:
        print("  ✖  Amount must be greater than 0.")
        return
 
    acc.balance          += amount
    acc.total_deposits   += amount
    acc.transaction_count += 1
    print(f"  ✔  ₹{amount:,.2f} deposited. New Balance: ₹{acc.balance:,.2f}")
 
 
def withdraw_money():
    separator()
    print("           WITHDRAW MONEY")
    separator()
    acc_no = input("  Account Number     : ").strip()
    acc = get_account(acc_no)
    if not acc:
        print("  ✖  Account not found.")
        return
    if not require_active(acc):
        return
 
    try:
        amount = float(input("  Withdrawal Amount  : ₹"))
    except ValueError:
        print("  ✖  Invalid amount.")
        return
 
    if amount <= 0:
        print("  ✖  Amount must be greater than 0.")
        return
    if acc.balance - amount < 1000:
        print("  ✖  Insufficient balance (minimum ₹1000 must be maintained).")
        return
 
    acc.balance            -= amount
    acc.total_withdrawals  += amount
    acc.transaction_count  += 1
    print(f"  ✔  ₹{amount:,.2f} withdrawn. Remaining Balance: ₹{acc.balance:,.2f}")
 
 
def check_balance():
    separator()
    print("           CHECK BALANCE")
    separator()
    acc_no = input("  Account Number : ").strip()
    acc = get_account(acc_no)
    if not acc:
        print("  ✖  Account not found.")
        return
    print(f"  Account Holder : {acc.customer_name}")
    print(f"  Current Balance: ₹{acc.balance:,.2f}")
    print(f"  Status         : {acc.status}")
 
 
def transfer_money():
    separator()
    print("           TRANSFER MONEY")
    separator()
    sender_no   = input("  Sender Account Number   : ").strip()
    receiver_no = input("  Receiver Account Number : ").strip()
 
    sender   = get_account(sender_no)
    receiver = get_account(receiver_no)
 
    if not sender:
        print("  ✖  Sender account not found.")
        return
    if not receiver:
        print("  ✖  Receiver account not found.")
        return
    if not require_active(sender):
        return
    if not require_active(receiver):
        return
 
    try:
        amount = float(input("  Transfer Amount         : ₹"))
    except ValueError:
        print("  ✖  Invalid amount.")
        return
 
    if amount <= 0:
        print("  ✖  Amount must be greater than 0.")
        return
    if sender.balance - amount < 1000:
        print("  ✖  Sender has insufficient balance (minimum ₹1000 must be maintained).")
        return
 
    sender.balance            -= amount
    sender.total_withdrawals  += amount
    sender.transaction_count  += 1
 
    receiver.balance          += amount
    receiver.total_deposits   += amount
    receiver.transaction_count += 1
 
    print(f"  ✔  ₹{amount:,.2f} transferred from {sender.customer_name} → {receiver.customer_name}")
    print(f"     Sender Balance  : ₹{sender.balance:,.2f}")
    print(f"     Receiver Balance: ₹{receiver.balance:,.2f}")
 
 
def update_customer_details():
    separator()
    print("        UPDATE CUSTOMER DETAILS")
    separator()
    acc_no = input("  Account Number : ").strip()
    acc = get_account(acc_no)
    if not acc:
        print("  ✖  Account not found.")
        return
 
    print(f"  Current Name   : {acc.customer_name}")
    new_name = input("  New Name (Enter to keep): ").strip()
    if new_name:
        acc.customer_name = new_name
 
    print(f"  Current Mobile : {acc.mobile_number}")
    new_mobile = input("  New Mobile (Enter to keep): ").strip()
    if new_mobile:
        acc.mobile_number = new_mobile
 
    print(f"  Current Email  : {acc.email}")
    new_email = input("  New Email (Enter to keep): ").strip()
    if new_email:
        acc.email = new_email
 
    print("  ✔  Customer details updated successfully.")
 
 
def view_transaction_summary():
    separator()
    print("       VIEW TRANSACTION SUMMARY")
    separator()
    acc_no = input("  Account Number : ").strip()
    acc = get_account(acc_no)
    if not acc:
        print("  ✖  Account not found.")
        return
 
    print(f"  Account Holder    : {acc.customer_name}")
    print(f"  Total Deposits    : ₹{acc.total_deposits:,.2f}")
    print(f"  Total Withdrawals : ₹{acc.total_withdrawals:,.2f}")
    print(f"  Total Transactions: {acc.transaction_count}")
    print(f"  Current Balance   : ₹{acc.balance:,.2f}")
 
 
def calculate_interest():
    separator()
    print("         CALCULATE INTEREST")
    separator()
    acc_no = input("  Account Number : ").strip()
    acc = get_account(acc_no)
    if not acc:
        print("  ✖  Account not found.")
        return
    if acc.account_type != "Savings":
        print("  ✖  Interest is applicable for Savings accounts only.")
        return
 
    interest = acc.balance * 4 / 100
    print(f"  Account Holder : {acc.customer_name}")
    print(f"  Balance        : ₹{acc.balance:,.2f}")
    print(f"  Interest Rate  : 4%")
    print(f"  Interest Amount: ₹{interest:,.2f}")
 
 
def close_account():
    separator()
    print("           CLOSE ACCOUNT")
    separator()
    acc_no = input("  Account Number : ").strip()
    acc = get_account(acc_no)
    if not acc:
        print("  ✖  Account not found.")
        return
    if acc.status == "Closed":
        print("  ✖  Account is already closed.")
        return
 
    acc.status = "Closed"
    print(f"  ✔  Account {acc_no} has been CLOSED.")
 
 
def reopen_account():
    separator()
    print("           REOPEN ACCOUNT")
    separator()
    acc_no = input("  Account Number : ").strip()
    acc = get_account(acc_no)
    if not acc:
        print("  ✖  Account not found.")
        return
    if acc.status == "Active":
        print("  ✖  Account is already Active.")
        return
 
    acc.status = "Active"
    print(f"  ✔  Account {acc_no} has been REOPENED and is now ACTIVE.")
 
 
def display_top_account_holder():
    separator()
    print("       TOP ACCOUNT HOLDER")
    separator()
    if not accounts:
        print("  No accounts found.")
        return
 
    top = max(accounts.values(), key=lambda a: a.balance)
    print(f"  Highest Balance Account:")
    top.display()
 
 
def display_bank_statistics():
    separator()
    print("         BANK STATISTICS")
    separator()
    if not accounts:
        print("  No accounts found.")
        return
 
    total    = len(accounts)
    active   = sum(1 for a in accounts.values() if a.status == "Active")
    closed   = total - active
    tot_bal  = sum(a.balance for a in accounts.values())
    avg_bal  = tot_bal / total if total else 0
 
    print(f"  Total Accounts  : {total}")
    print(f"  Active Accounts : {active}")
    print(f"  Closed Accounts : {closed}")
    print(f"  Total Balance   : ₹{tot_bal:,.2f}")
    print(f"  Average Balance : ₹{avg_bal:,.2f}")
 
 
# ── main menu ────────────────────────────────────────────
 
def show_menu():
    separator()
    print("       BANK MANAGEMENT SYSTEM — MENU")
    separator()
    options = [
        " 1. Create New Account",
        " 2. View All Accounts",
        " 3. Search Account",
        " 4. Deposit Money",
        " 5. Withdraw Money",
        " 6. Check Balance",
        " 7. Transfer Money",
        " 8. Update Customer Details",
        " 9. View Transaction Summary",
        "10. Calculate Interest",
        "11. Close Account",
        "12. Reopen Account",
        "13. Display Top Account Holder",
        "14. Display Bank Statistics",
        "15. Exit",
    ]
    for o in options:
        print(" ", o)
    separator()
 
def main():
    actions = {
        "1" : create_account,
        "2" : view_all_accounts,
        "3" : search_account,
        "4" : deposit_money,
        "5" : withdraw_money,
        "6" : check_balance,
        "7" : transfer_money,
        "8" : update_customer_details,
        "9" : view_transaction_summary,
        "10": calculate_interest,
        "11": close_account,
        "12": reopen_account,
        "13": display_top_account_holder,
        "14": display_bank_statistics,
    }
 
    while True:
        show_menu()
        choice = input("  Enter your choice (1-15): ").strip()
 
        if choice == "15":
            separator()
            print("  Thank you for using the Bank Management System. Goodbye!")
            separator()
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("  ✖  Invalid choice. Please enter a number between 1 and 15.")
 
        input("\n  Press Enter to continue...")
 
if __name__ == "__main__":
    main()
 

