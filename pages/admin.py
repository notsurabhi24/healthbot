def show():
    import streamlit as st
    import pandas as pd

    if st.session_state.get("role") != "admin":
        st.error("🚫 Access denied. Admins only.")
        st.stop()

    st.title("👮 Admin Dashboard")

    try:
        users_df = pd.read_csv("database/users.csv")
        st.subheader("👥 Registered Users")
        st.dataframe(users_df.drop("password", axis=1))
    except:
        st.warning("No users registered yet.")

    try:
        entries_df = pd.read_csv("data/entries.csv")
        st.subheader("📈 Mood Trends")
        st.bar_chart(entries_df['mood'].value_counts())
        st.write("Total Entries:", len(entries_df))
        st.dataframe(entries_df)
    except:
        st.info("No journal entries yet.")
