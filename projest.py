import streamlit as st

# Dummy data for a single account
account = {
    "pin": "1234",
    "balance": 5000.0
}

# Streamlit app
st.title("💳 Basic ATM Simulator")

# Session state to track user authentication and account balance
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "balance" not in st.session_state:
    st.session_state.balance = account["balance"]

# Login system
if not st.session_state.authenticated:
    st.subheader("🔑 Login")
    pin = st.text_input("Enter your PIN", type="password")
    if st.button("Login"):
        if pin == account["pin"]:
            st.session_state.authenticated = True
            st.success("Authentication Successful!")
        else:
            st.error("Incorrect PIN. Please try again.")
else:
    # ATM menu options
    st.subheader("🏦 ATM Menu")
    choice = st.radio(
        "Select an option:",
        ("Check Balance", "Deposit Money", "Withdraw Money", "Logout")
    )

    # Check balance
    if choice == "Check Balance":
        st.write(f"💰 Your current balance is: **${st.session_state.balance:.2f}**")

    # Deposit money
    elif choice == "Deposit Money":
        deposit_amount = st.number_input("Enter the amount to deposit:", min_value=0.0, step=0.01)
        if st.button("Deposit"):
            st.session_state.balance += deposit_amount
            st.success(f"${deposit_amount:.2f} deposited successfully!")
    
    # Withdraw money
    elif choice == "Withdraw Money":
        withdraw_amount = st.number_input("Enter the amount to withdraw:", min_value=0.0, step=0.01)
        if st.button("Withdraw"):
            if 0 < withdraw_amount <= st.session_state.balance:
                st.session_state.balance -= withdraw_amount
                st.success(f"${withdraw_amount:.2f} withdrawn successfully!")
            elif withdraw_amount > st.session_state.balance:
                st.error("Insufficient funds!")
            else:
                st.error("Invalid amount entered.")
    
    # Logout
    elif choice == "Logout":
        st.session_state.authenticated = False
        st.success("Logged out successfully!")

# Footer
st.caption("Basic ATM Simulator | Made with 💻 in Python")
