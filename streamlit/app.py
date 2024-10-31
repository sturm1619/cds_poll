import streamlit as st
from collections import namedtuple
from datetime import date
import requests

MAJOR_OPTIONS: list[str] = [
    "CS - Computational Data Science",
    "CS - Pure Computer Science",
    "CS - Secure Computing",
    "CS - Full-Stack Web Development",
    "CS - Computer Networking",
    "CS - Education",
    "CS - Other",
    "MATH - Mathematics",
    "MATH - Statistics",
    "BIO - Biology",
    "BIO - Bioinformatics",
    "BIO - Zoology",
    "BIO - Botany"
    "BIO - Biology Education",
    "Project Management",
    "Finance",
    "Other"
]

SEMESTERS: list[str] = [str(value) for value in range(0,9)] + ["9+"]

st.session_state.form = {}
animation = st.balloons if date.month not in (1,2,11,12) else st.snow

def submit_answers():
    # submission = requests.post()
    st.json(st.session_state.form)
    status_code = "201"
    if status_code == "200":
        animation()
        st.toast("Thanks for your time!")
        st.success("Your answer was submitted!")
    else:
        st.toast("Oh-oh! Something went wrong...")
        st.error("Oh-oh! Something went wrong...")

if __name__ == "__main__":
    st.title("UVU Data Science Club Survey")

    with st.form("student_form"):
        st.header("Some generic stuff about you :smile:", divider="green")

        st.session_state.form["name"] = st.text_input("Your name: ", value="")
        st.session_state.form["major"] = st.selectbox(
            "Your major",
            options=MAJOR_OPTIONS,
            placeholder="Choose your major"
        )

        st.session_state.form["semester"] = st.select_slider(
            "Number of semesters:",
            options = SEMESTERS,
            value = "1"
        )

        st.header(
            "Now, tell us about you :joy:",
            divider="green"
        )


        st.session_state.form["network"] = st.toggle(
            "I want to network with businesses/I'm looking for job"
        )

        st.session_state.form["theory"] = st.toggle(
            "I want to learn more about Data Science"
        )

        st.session_state.form["social"] = st.toggle(
            "I want to meet other students interested in Data Science"
        )

        submit = st.form_submit_button(
            "Submit your answers",
            type = "primary",
            use_container_width = True
        )

        if submit:
            submit_answers()



    # - I want an internship, or network with people in the industry
    # - I want to learn more about Data Science related topics
    # - I want to meet more students
