import streamlit as st

# Sample user data
users = {
    "1234": {"name": "John Doe", "balance": 5000.0, "transactions": []},
    "5678": {"name": "Jane Smith", "balance": 3000.0, "transactions": []},
    "admin": {"name": "Admin", "balance": 0.0, "transactions": []}  # Admin account
}

# Session state initialization
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "current_user" not in st.session_state:
    st.session_state.current_user = None

# Helper function to record transactions
def record_transaction(user, transaction):
    users[user]["transactions"].append(transaction)
    if len(users[user]["transactions"]) > 5:  # Limit to last 5 transactions
        users[user]["transactions"].pop(0)

# Login
if not st.session_state.authenticated:
    st.title("💳 Welcome to the Enhanced ATM Simulator")
    pin = st.text_input("Enter your PIN", type="password")
    if st.button("Login"):
        if pin in users:
            st.session_state.authenticated = True
            st.session_state.current_user = pin
            st.success(f"Welcome, {users[pin]['name']}!")
        else:
            st.error("Invalid PIN. Please try again.")
else:
    # Main menu
    current_user = st.session_state.current_user
    st.title(f"🏦 Welcome, {users[current_user]['name']}")
    
    if current_user == "admin":
        st.subheader("⚙️ Admin Panel")
        st.write("Manage user accounts here.")
        new_pin = st.text_input("Add a new user PIN:")
        if st.button("Add User"):
            if new_pin and new_pin not in users:
                users[new_pin] = {"name": "New User", "balance": 0.0, "transactions": []}
                st.success(f"User with PIN {new_pin} added successfully!")
            else:
                st.error("Invalid or duplicate PIN.")
        st.write("Current Users:")
        for pin, data in users.items():
            if pin != "admin":
                st.write(f"🔑 PIN: {pin}, Name: {data['name']}, Balance: ${data['balance']}")
    else:
        choice = st.radio("Select an option:", 
                          ["Check Balance", "Deposit Money", "Withdraw Money", 
                           "View Transactions", "Change PIN", "Logout"])
        
        if choice == "Check Balance":
            st.write(f"💰 Your current balance is: **${users[current_user]['balance']:.2f}**")
        
        elif choice == "Deposit Money":
            deposit_amount = st.number_input("Enter the amount to deposit:", min_value=0.0, step=0.01)
            if st.button("Deposit"):
                if deposit_amount > 0:
                    users[current_user]['balance'] += deposit_amount
                    record_transaction(current_user, f"Deposited ${deposit_amount:.2f}")
                    st.success(f"${deposit_amount:.2f} deposited successfully!")
                else:
                    st.error("Please enter a valid amount.")
        
        elif choice == "Withdraw Money":
            withdraw_amount = st.number_input("Enter the amount to withdraw:", min_value=0.0, step=0.01)
            if st.button("Withdraw"):
                if 0 < withdraw_amount <= users[current_user]['balance']:
                    users[current_user]['balance'] -= withdraw_amount
                    record_transaction(current_user, f"Withdrew ${withdraw_amount:.2f}")
                    st.success(f"${withdraw_amount:.2f} withdrawn successfully!")
                elif withdraw_amount > users[current_user]['balance']:
                    st.error("Insufficient funds!")
                else:
                    st.error("Please enter a valid amount.")
        
        elif choice == "View Transactions":
            st.write("📜 Transaction History:")
            transactions = users[current_user]["transactions"]
            if transactions:
                for i, transaction in enumerate(transactions, 1):
                    st.write(f"{i}. {transaction}")
            else:
                st.write("No transactions yet.")
        
        elif choice == "Change PIN":
            new_pin = st.text_input("Enter a new PIN:", type="password")
            if st.button("Change PIN"):
                if new_pin and new_pin != current_user:
                    users[new_pin] = users.pop(current_user)
                    st.session_state.current_user = new_pin
                    st.success("PIN changed successfully!")
                else:
                    st.error("Invalid or duplicate PIN.")
        
        elif choice == "Logout":
            st.session_state.authenticated = False
            st.session_state.current_user = None
            st.success("Logged out successfully!")
            
# Footer
st.caption("Enhanced ATM Simulator | Made with 💻 in Python")
