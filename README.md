# 🎬 AI Movie Explorer

AI Movie Explorer is an AI-powered movie exploration application built using **Streamlit, Python, OpenRouter API, PostgreSQL, and Neon PostgreSQL**.

Users can ask movie-related questions in natural language and receive intelligent movie information generated from AI and database results.

The application converts user questions into SQL queries, retrieves movie information from PostgreSQL, and generates additional movie insights such as story summaries and actor details.

---

## 🚀 Live Demo

🔗 https://ai-movie-explorer.streamlit.app

---

## 📂 GitHub Repository

🔗 https://github.com/iamGokulraja/AI-Movie-Explorer

---

# ✨ Features

* 🎥 Natural Language Movie Search
* 🤖 AI to SQL Conversion
* 🗄 PostgreSQL Database Querying
* ☁ Neon PostgreSQL Deployment
* 💻 PostgreSQL Local Development
* 📊 Interactive Streamlit Interface
* 🧠 AI Generated Movie Insights
* ⚡ Fast Query Execution

---

# 🛠 Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### Database

* PostgreSQL (Localhost)
* Neon PostgreSQL (Cloud)

### AI Models

* OpenRouter API
* Meta Llama 3

### Libraries

```text
Pandas
SQLAlchemy
OpenAI
python-dotenv
Streamlit
```

---

# 📁 Project Structure

```plaintext
AI-Movie-Explorer
│
├── app.py
├── dataset_loader.py
├── Tamil_movies_dataset.csv
├── requirements.txt
├── .env
├── README.md
```

---

# ⚙ Installation

Clone Repository

```bash
git clone https://github.com/iamGokulraja/AI-Movie-Explorer.git
```

Move into Project

```bash
cd AI-Movie-Explorer
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄 Database Setup

## Local Development (PostgreSQL)

Create PostgreSQL database locally.

Example `.env`

```env
DATABASE_CONN=postgresql://username:password@localhost:5432/database_name

API_KEY=your_openrouter_api_key
```

Load Dataset

```bash
python dataset_loader.py
```

---

## Streamlit Deployment (Neon PostgreSQL)

Create Neon PostgreSQL database.

Example Secrets

```env
DATABASE_CONN=your_neon_postgresql_connection

API_KEY=your_openrouter_api_key
```

Load Dataset

```bash
python dataset_loader.py
```

---

# ▶ Run Application

```bash
streamlit run app.py
```

---

# 🧠 How It Works

1. User enters movie-related question

2. AI converts question into PostgreSQL SQL query

3. SQL executes in PostgreSQL / Neon PostgreSQL

4. Matching movie data is retrieved

5. AI generates movie story and actor insights

6. Final results displayed in Streamlit

---

# 📸 Example Questions

```text
Show top rated Tamil movies

Movies acted by Vijay

Best action movies after 2020

Show movies with highest PeopleVote

Top Hero Rating movies
```

---

# ☁ Deployment

## GitHub

```bash
git add .
git commit -m "Initial Commit"
git push origin main
```

---

## Streamlit Community Cloud

1. Push project to GitHub

2. Open Streamlit Community Cloud

3. Connect GitHub Repository

4. Select app.py

5. Add Streamlit Secrets

```env
DATABASE_CONN=your_neon_postgresql_connection

API_KEY=your_openrouter_api_key
```

6. Deploy Application

---

# ☁ Deployment Architecture

```plaintext
Local Run
──────────────

User
 ↓
Streamlit
 ↓
OpenRouter API
 ↓
PostgreSQL (Localhost)


Cloud Deployment
────────────────

User
 ↓
Streamlit Cloud
 ↓
OpenRouter API
 ↓
Neon PostgreSQL
```

---

# 🔮 Future Improvements

* Movie Posters
* Recommendation System
* Authentication
* Voice Search
* Multi-language Support
* RAG Integration

---

# 👨‍💻 Author

**Gokul Raja**

ECE Student | Full Stack Development | AI Enthusiast

GitHub:
https://github.com/iamGokulraja

---

⭐ If you like this project, don't forget to give it a Star.
