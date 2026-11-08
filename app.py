from time import sleep

import streamlit as st


def stream_no():
    for char in "No...":
        sleep(0.06)
        yield char


def verify_solutions():
    names = [st.secrets["name1"], st.secrets["name2"]]
    numbers = [st.secrets["numbers1"], st.secrets["numbers2"]]
    for name, nums in zip(names, numbers):
        concat = name + "".join(st.secrets["answers"])
        answer = "".join(concat[n-1] for n in nums)
        if answer != st.secrets["final"]:
            raise ValueError

st.set_page_config(page_title="Ross's Small Puzzle")

if "verified" not in st.session_state:
    verify_solutions()
    st.session_state.verified = True

if "current_level" not in st.session_state:
    st.session_state.current_level = 0
level = st.session_state.current_level

if "numbers" not in st.session_state:
    st.session_state.numbers = []

if level == 0:
    st.title("Level 0")
    attempt = st.text_input(st.secrets["questions"][level]).strip().lower()
    if attempt == st.secrets["name1"]:
        st.session_state.numbers = st.secrets["numbers1"]
    elif attempt == st.secrets["name2"]:
        st.session_state.numbers = st.secrets["numbers2"]
    elif attempt:
        st.write_stream(stream_no)
    if st.session_state.numbers:
        st.session_state.current_level += 1
        st.rerun()

elif level < len(st.secrets["questions"]):
    st.title(f"Level {level}")
    attempt = st.text_input(st.secrets["questions"][level]).strip().lower()
    if (attempt == st.secrets["answers"][level - 1]):
        st.session_state.current_level += 1
        st.rerun()
    elif attempt:
        st.write_stream(stream_no)

else:
    st.title(f"Final level")
    st.write(f"Do you remember your previous answers?")
    st.write(", ".join(str(x) for x in st.session_state.numbers) + ".")
    attempt = st.text_input("Final answer?").replace(" ", "").lower()
    if attempt == st.secrets["final"]:
        st.write("OK!")
    elif attempt:
        st.write_stream(stream_no)