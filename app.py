import streamlit as st

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = None
if 'role' not in st.session_state:
    st.session_state.role = None

# Sidebar navigation (only if logged in)
if st.session_state.logged_in:
    st.sidebar.title(f"🌼 Welcome, {st.session_state.username}")
    page = st.sidebar.radio("Navigate", [
        "Home",
        "Write Journal",
        "Wellness Insights",
        "How It Works",
        "Crisis Support",
        "Admin Dashboard" if st.session_state.role == "admin" else None
    ])
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.session_state.role = None
        st.rerun()
else:
    page = "Home"

# Import pages
if page == "Home":
    from pages.home import show
elif page == "Write Journal":
    from pages.journal_entry import show
elif page == "Wellness Insights":
    from pages.wellness_insights import show
elif page == "How It Works":
    from pages.how_it_works import show
elif page == "Crisis Support":
    from pages.crisis_support import show
elif page == "Admin Dashboard":
    from pages.admin import show

# Show login if not logged in
if not st.session_state.logged_in:
    from pages.login import show
