import streamlit as st

st.set_page_config(page_title="Ross's Small Puzzle")

if "current_level" not in st.session_state:
    st.session_state.current_level = 0
level = st.session_state.current_level

if level < len(st.secrets["questions"]):
    st.title(f"Level {level}")
    attempt = st.text_input(st.secrets["questions"][level]).strip().lower()
    if (attempt == st.secrets["answers"][level]):
        st.session_state.current_level += 1
        st.rerun()
    elif attempt:
        st.write("No...")

else:
    st.title(f"Final level")
    st.write(f"Do you remember your previous answers?")
    st.write(", ".join(str(x) for x in st.secrets["numbers"]) + ".")
    attempt = st.text_input("Final answer?").replace(" ", "").lower()
    if attempt == st.secrets["final"]:
        st.write("OK!")
    elif attempt:
        st.write("No...")