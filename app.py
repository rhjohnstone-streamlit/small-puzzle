import streamlit as st

if "current_level" not in st.session_state:
    st.session_state.current_level = 0
level = st.session_state.current_level

if level < len(st.secrets["questions"]):
    st.title(f"Level {level}")
    if (st.text_input(st.secrets["questions"][level]).lower() == st.secrets["answers"][level]):
        st.session_state.current_level += 1
        st.rerun()
else:
    numbers = ", ".join(str(x) for x in st.secrets["numbers"])
    st.title(f"Final level")
    st.write(f"Do you remember your previous answers? {numbers}.")
    if st.text_input("Final answer?").replace(" ", "").lower() == st.secrets["final"]:
        st.write("OK!")