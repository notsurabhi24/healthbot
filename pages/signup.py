def show():
    import streamlit as st
    from utils.auth import register_user
    import os

    st.title("📝 Sign Up")

    username = st.text_input("Choose a username")
    password = st.text_input("Choose a password", type="password")
    confirm = st.text_input("Confirm password", type="password")

    if st.button("Register"):
        if password != confirm:
            st.error("Passwords don't match!")
        elif len(password) < 5:
            st.error("Password too short!")
        elif not username:
            st.error("Username cannot be empty")
        else:
            success, msg = register_user(username, password)
            if success:
                st.success(msg + " You can now log in.")
            else:
                st.error(msg)
