import streamlit as st
from streamlit_extras import add_vertical_space as avs
import os
from dotenv import load_dotenv
import google.generativeai as genai
import PyPDF2
from PIL import Image

load_dotenv()

# set page config
st.set_page_config(
    page_title="CareerCraft",
    page_icon="📃",
    layout="wide",
)
st.title("📃 CareerCraft")
st.write(1.1)

# # Display a message with a LinkedIn profile link
# st.write("Developed by [Jitendra-Kumar](https://www.linkedin.com/in/jitendra-ky)")


avs.add_vertical_space(4)

key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key)


model = genai.GenerativeModel('gemini-2.5-flash')

def get_gemini_response(prompt):
    st.write("Generating response...")
    response = model.generate_content(prompt)
    st.write("Response generated!")
    return response.text

def input_pdf_text(uploaded_file):
    try:
        # Create a PDF reader object from the uploaded file
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        
        # Initialize a variable to store the text content
        text = ""
        
        # Iterate through all the pages and extract the text
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        
        return text
    except Exception as e:
        return f"An error occurred while reading the PDF: {e}"

def analyse_resume(resume_txt, job_description):
    prompt = open('prompt.md', 'r').read()
    prompt = prompt.replace("{{resume-8765}}", resume_txt)
    prompt = prompt.replace("{{job_description_58945}}", job_description)
    
    return get_gemini_response(prompt)




# ATS tracking application
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("<h1 style='text-align: center;'>Embark on Your Career Adventure</h1>", unsafe_allow_html=True)
    jd = st.text_area("Paste the Job Description")
    uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")
    submit = st.button("Submit")

    if submit:
        if uploaded_file is not None and jd.strip():
            text = input_pdf_text(uploaded_file)
            if "error" not in text.lower():
                with st.spinner("Analyzing your resume..."):
                    response = analyse_resume(text, jd)
                st.markdown("### Analysis Results")
                st.markdown(response)
            else:
                st.error(text)
        elif uploaded_file is None:
            st.error("Please upload your resume")
        elif not jd.strip():
            st.error("Please paste the job description")

with col2:
    st.image('https://cdn.dribbble.com/userupload/12500996/file/original-b458fe398a6d7f4e9999ce66ec856ff9.gif', use_column_width=True)

avs.add_vertical_space(10)







# Here is the introduction
col1, col2 = st.columns([3, 3])
with col1:
    st.header("🤵 Navigate the Job Market with Confidence!")
    st.markdown("""
        <p style='text-align: justify; font-size: 18px;'>
        Introducing <strong>CareerCraft</strong>, an <em>ATS-Optimized Resume Analyzer</em>—your ultimate solution 
        for optimizing job applications and accelerating career growth. Our innovative platform leverages advanced 
        ATS technology to provide job seekers with valuable insights into their resumes' compatibility with job 
        descriptions. From resume optimization and skill enhancement to career progression guidance, 
        <strong>CareerCraft</strong> empowers users to stand out in today's competitive job market. 
        Streamline your job application process, enhance your skills, and navigate your career path with confidence. 
        Join <strong>CareerCraft</strong> today and unlock new opportunities for professional success!
        </p>
        """, unsafe_allow_html=True)

# with col2:
#     # Embed YouTube video
#     st.video("https://youtu.be/-C5RDNQNT1c?si=bFBaWwzr0Be7fCnd")

# avs.add_vertical_space(10)








# Here are the offerings
col1, col2 = st.columns([3, 2])
with col1:
    st.header("🌟 Wind Energy Offerings 🌟")
    st.markdown("<p style='font-size: 18px;'>🔍 <strong>ATS Optimization</strong></p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px;'>📄 <strong>Resume Analysis</strong></p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px;'>🎯 <strong>Tailored Profile Enhancement</strong></p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px;'>📈 <strong>Skill Enhancement Guidance</strong></p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px;'>🚀 <strong>Streamlined Application Process</strong></p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px;'>💡 <strong>Personalized Recommendations</strong></p>", unsafe_allow_html=True)
with col2:
    img1 = Image.open("images/Job-Employment-PNG-Image.png")
    st.image(img1, use_column_width=True)








# FAQ section
faqs = """
Question: How does CareerCraft analyze resumes and job descriptions?
Answer: CareerCraft leverages advanced AI algorithms, powered by Google Gemini, to thoroughly examine your resume and the provided job description. It identifies crucial keywords, evaluates the alignment of your qualifications with the job requirements, and assesses the overall compatibility between the two. This process ensures your resume is optimized for Applicant Tracking Systems (ATS) and increases your chances of securing an interview.

Question: Can CareerCraft suggest improvements for my resume?
Answer: Absolutely! CareerCraft provides personalized, actionable recommendations to enhance your resume. It identifies missing keywords that are critical to the job description, suggests ways to better align your experience and skills with the job role, and offers advice on how to optimize your resume for maximum impact.

Question: Is CareerCraft suitable for both entry-level and experienced professionals?
Answer: Yes, CareerCraft is designed to assist job seekers at all career stages. Whether you're just starting out or are a seasoned professional, CareerCraft offers tailored insights and guidance to refine your resume, highlight your strengths, and position you as a strong candidate for the roles you’re targeting.

Question: How does CareerCraft ensure my resume is ATS-friendly?
Answer: CareerCraft analyzes your resume with ATS optimization in mind. It checks for the presence of industry-specific keywords, assesses formatting to ensure it is compatible with ATS systems, and suggests improvements to enhance readability and keyword density, helping your resume pass through automated filters and reach human recruiters.

Question: What makes CareerCraft different from other resume analysis tools?
Answer: CareerCraft stands out due to its integration with Google Gemini’s advanced AI capabilities, offering not just keyword analysis but also comprehensive resume optimization tailored to your specific job goals.

"""
que, ans = [], []
for line in faqs.split("\n"):
    if line.startswith("Question:"):
        que.append(line)
    elif line.startswith("Answer:"):
        ans.append(line)

st.markdown("<h1 style='text-align: center;'>FAQs</h1>", unsafe_allow_html=True)
for i in range(len(que)):
    st.write(f"### {que[i]}")
    st.write(f'''{ans[i]}''')
    '''---'''
    avs.add_vertical_space(1)

