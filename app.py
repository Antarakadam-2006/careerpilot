import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader
page = st.sidebar.selectbox(
    "Choose Page",
    ["Home", "Resume Analyzer", "Career Roadmap", "Interview Practice"]
)
# Paste your Gemini API key here

genai.configure(api_key="YOUR_API_KEY_HERE")
model = genai.GenerativeModel("gemini-2.5-flash")



if page == "Home":

    st.title("🚀 CareerForge AI")

    st.subheader("Your Personal AI Career Mentor")

    st.write("""
    Welcome to CareerForge AI.

    Features:
    - Resume Analysis
    - Career Roadmap
    - Interview Practice
    - Skill Development
    """)
elif page == "Resume Analyzer":

    st.title("📄 AI Resume Analyzer")

    uploaded_file = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"]
    )

    if uploaded_file is not None:

        reader = PdfReader(uploaded_file)

        resume_text = ""

        for page in reader.pages:
            text = page.extract_text()

            if text:
                resume_text += text

        st.success("Resume uploaded successfully!")

        if st.button("Analyze Resume"):

            prompt = f"""
            Analyze this resume.

            Give:
            1. ATS Score out of 100
            2. Skills Found
            3. Strengths
            4. Weaknesses
            5. Missing Skills
            6. Suggestions for Improvement
            7. 5 Interview Questions

            Resume:
            {resume_text}
            """

            response = model.generate_content(prompt)

            st.subheader("Analysis Result")
            st.write(response.text)
elif page == "Career Roadmap":

    st.title("🗺️ Career Roadmap")

    role = st.text_input(
        "Enter your dream job role"
    )

    if st.button("Generate Roadmap"):

        prompt = f"""
        Create a detailed 6-month roadmap
        for becoming a {role}.

        Include:
        1. Skills to learn
        2. Courses
        3. Projects
        4. Interview preparation

        Give month-wise plan.
        """

        response = model.generate_content(prompt)

        st.subheader("Your Career Roadmap")

        st.write(response.text)


elif page == "Interview Practice":

    st.title("🎤 Interview Practice")

    interview_role = st.text_input(
        "Enter job role for interview practice"
    )

    if st.button("Generate Interview Questions"):

        prompt = f"""
        Generate 10 interview questions for a {interview_role}.

        Include:
        - Technical Questions
        - HR Questions
        - Scenario Based Questions

        Number them properly.
        """

        response = model.generate_content(prompt)

        st.subheader("Interview Questions")

        st.write(response.text)