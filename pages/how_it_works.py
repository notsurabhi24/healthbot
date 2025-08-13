def show():
    import streamlit as st

    st.title("🔍 How MindGarden Thinks")

    st.markdown("""
    Welcome to the brain of **MindGarden**! We use two classic AI reasoning techniques to understand your emotions — all with **zero black boxes**.
    """)

    tab1, tab2 = st.tabs(["🧠 Forward Chaining", "🎯 Backward Chaining"])

    with tab1:
        st.header("Forward Chaining: From Data to Insight")
        st.write("**Data-driven reasoning** — starts with what you tell us.")

        st.markdown("""
        ### Example:
        - You write: *"I'm anxious and can't sleep."*
        - **Facts extracted:** `anxious`, `racing thoughts`
        - **Rule:** `IF anxious AND racing thoughts → suggest_breathing`
        - **Action:** You get a breathing exercise.

        This runs automatically — like a therapist noticing patterns.
        """)

        st.code("""
        Facts: [anxious, racing thoughts]
        Rule: anxious + racing thoughts → suggest_breathing
        Conclusion: "Try 4-7-8 breathing"
        """, language="text")

    with tab2:
        st.header("Backward Chaining: Goal-Driven Thinking")
        st.write("**Goal-first reasoning** — works backward to check evidence.")

        st.markdown("""
        ### Example:
        - **Goal:** "Should I talk to a counselor?"
        - **Rule:** `IF sad AND no_energy AND hopeless → suggest_therapy`
        - AI checks your entries for these signs.

        Only if evidence matches → it suggests therapy.

        Efficient. Focused. Safe.
        """)

        st.info("No machine learning. No data leaks. Just logic and care.")
