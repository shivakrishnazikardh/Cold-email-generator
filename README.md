
# 📧 AutoPitcher — Cold Email Generator for Job Opportunities

**AutoPitcher** is a Streamlit-based application that automates the creation of personalized cold emails tailored for job opportunities extracted from career pages. Leveraging web scraping, natural language processing, and large language models, this tool helps business development professionals pitch services effectively and efficiently.

---

## 🚀 Features

* **URL-based Job Data Extraction:**
  Load and clean job descriptions directly from career webpage URLs.

* **Automated Job Postings Extraction:**
  Extract structured job details (role, experience, skills, description) using advanced language models.

* **Portfolio Integration:**
  Query your personal portfolio based on required skills to showcase relevant tools and projects dynamically.

* **Personalized Cold Email Generation:**
  Generate professional, targeted cold emails pitching your company’s solutions tailored to each job posting.

* **Interactive Streamlit Interface:**
  User-friendly web UI to input URLs and display generated emails instantly.

---

## 🛠️ Tech Stack

* **Python** for backend logic
* **Streamlit** for frontend UI
* **Langchain Groq LLM** for natural language processing and generation
* **ChromaDB** for vector storage and similarity search in portfolio data
* **Pandas** for portfolio data management
* **Regex** for text cleaning and preprocessing

---

## 📂 Project Structure

* `app.py` — Main Streamlit application
* `chains.py` — Logic for interacting with the language model (job extraction & email generation)
* `portfolio.py` — Portfolio management and vector similarity queries
* `utils.py` — Text cleaning and preprocessing utilities

---

## 🔧 Getting Started

1. **Clone the repo:**

   ```bash
   git clone https://github.com/yourusername/autopitcher.git
   cd autopitcher
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Setup environment variables:**
   Create a `.env` file with your Groq API key:

   ```
   API_KEY_Groq=your_api_key_here
   ```

4. **Run the app:**

   ```bash
   streamlit run app.py
   ```

---

## ⚙️ How It Works

1. Enter a career page URL in the Streamlit app.
2. The app scrapes and cleans the page content.
3. The language model extracts job postings from the text in JSON format.
4. The portfolio is queried based on the skills required for each job.
5. Personalized cold emails are generated showcasing your company’s relevant tools and capabilities.
6. Emails are displayed interactively for review and use.

---

## 📈 Use Cases

* Business development executives looking to automate cold outreach.
* Job seekers or recruiters wanting to craft tailored communications.
* Teams aiming to showcase portfolios dynamically based on client needs.

---

## 🤝 Contributing

Contributions and suggestions are welcome! Feel free to fork, open issues, or submit pull requests.

