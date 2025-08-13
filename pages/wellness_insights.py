def show():
    import streamlit as st
    import pandas as pd
    from rules.mood_rules import get_forward_rules, extract_facts, get_empathetic_responses
    from utils.forward_chain import forward_chain

    st.title("📊 Your Wellness Insights")

    try:
        df = pd.read_csv("data/entries.csv")
        user_entries = df[df['user'] == st.session_state.username]

        if len(user_entries) == 0:
            st.info("Write a journal entry to start seeing insights.")
        else:
            latest = user_entries.iloc[-1]
            st.write(f"**Last entry ({latest['date']}):** {latest['mood']}")

            facts = extract_facts(latest['mood'], latest['entry'])
            conclusions = forward_chain(get_forward_rules(), facts)

            st.subheader("💡 AI Suggestions")

            responses = get_empathetic_responses()
            for concl in conclusions:
                if concl in responses:
                    res = responses[concl]
                    with st.expander(res["title"]):
                        st.write(res["advice"])

    except Exception as e:
        st.error("No data yet or error loading entries.")
