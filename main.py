import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text




def create_streamlit_app(chain, portfolio, clean_text):
    st.title("📧Cold Mail Generator")
    url_input = st.text_input("Enter  a URL:", value="https://careers.nike.com/software-engineer-iii-workday-payroll-remote-work-option/job/R-60875?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic")
    submit_button = st.button("Submit")

    

    if submit_button:
        @st.cache_data(show_spinner=True)
        def load_data():
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            return data
        try:
            data = load_data()
            portfolio.load_portfolio()
            jobs = chain.extract_jobs(data)
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = chain.write_mail(job, links)
                st.code(email, language = 'markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout= "wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)