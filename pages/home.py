def show():
    import streamlit as st
    st.title("🌿 MindGarden")
    st.subheader("Your private space to reflect, heal, and grow.")
    st.image("assets/garden-bg.jpg", use_column_width=True)
    st.markdown("""
    Every thought you write helps your inner garden bloom.

    🔐 Your entries are private  
    🧠 Powered by explainable AI  
    💬 Suggestions from care, not algorithms

    Use the sidebar to get started.
    """)
