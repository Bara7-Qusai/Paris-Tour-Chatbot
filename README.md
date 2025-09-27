
# ParisTourChatbot 🌟

A conversational AI chatbot that provides tourist information about Paris using **OpenAI GPT-4o-mini**.

---

## Features

- Answers questions about famous landmarks such as:
  - Eiffel Tower
  - Louvre Museum
  - Arc de Triomphe
- Provides must-see artworks at the Louvre.
- Maintains conversation context across multiple questions.
- Interactive web interface built with **Streamlit** for real-time Q&A.

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/ParisTourChatbot.git
````

2. **Navigate to the project folder**

```bash
cd ParisTourChatbot
```

3. **Install required packages**

```bash
pip install -r requirements.txt
```

4. **Set your OpenAI API key**

```bash
export OPENAI_API_KEY="your_api_key_here"   # macOS/Linux
setx OPENAI_API_KEY "your_api_key_here"     # Windows PowerShell
```

---

## Usage

### 1️⃣ Run the automatic question script

```bash
python app.py
```

* Sends predefined questions to the chatbot and prints responses.

### 2️⃣ Run the interactive Streamlit app

```bash
streamlit run streamlit_app.py
```

* Opens a web interface where users can type questions about Paris landmarks and get instant answers.

---

## Project Structure

```
ParisTourChatbot/
├── app.py                # Script with predefined questions
├── streamlit_app.py      # Interactive web app using Streamlit
├── requirements.txt      # Required Python packages
├── README.md             # Project documentation
└── .gitignore            # Ignore cache and environment files
```
