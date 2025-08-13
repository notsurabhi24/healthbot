def show():
    import streamlit as st
    import pandas as pd
    from datetime import datetime
    import os

    st.title("🌼 Write in Your MindGarden")

    mood = st.selectbox("How are you feeling?", [
        "😊 Happy", "😐 Neutral", "😔 Sad", "😰 Anxious", "😡 Angry", "😴 Tired"
    ])
    entry = st.text_area("Share your thoughts...", height=200)

    if st.button("🌱 Save Entry"):
        if not entry.strip():
            st.error("Please write something before saving.")
        else:
            # Ensure data dir exists
            if not os.path.exists("data"):
                os.makedirs("data")

            # Save entry
            data = pd.DataFrame([{
                "user": st.session_state.username,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "mood": mood,
                "entry": entry
            }])
            data.to_csv("data/entries.csv", mode='a', header=not os.path.exists("data/entries.csv"), index=False)
            st.success("Your thoughts are saved. The garden grows 🌷")
            st.balloons()
