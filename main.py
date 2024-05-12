import streamlit as st
from models import Ceterficate

md = Ceterficate()

st.title("Certificate Generator")
University_name = ["Yale University", "Duke University", "University of Michigan", "Google", "Coursera"]
univ_name = st.sidebar.selectbox("Select University", University_name)
student_name = st.sidebar.text_input("NAME")
date = st.sidebar.text_input("DATE")
course = st.sidebar.text_input("ENTER COURSE NAME")

isClicked = st.sidebar.button("Generate")
if isClicked:
    md.institute_selected(univ_name)
    md.Course(course)
    md.Name(student_name)
    md.Professor(univ_name)
    md.Date(date)
    md.BasicImages()
    md.BasicText()

    md.ShowImage()
