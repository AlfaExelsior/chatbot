
# Exelsior's Chatbot

This project is an AI-powered chatbot built using **Python**, **Streamlit**, and **OpenAI's GPT-3.5 model**. The chatbot can interact with users, respond to their questions, and offer assistance on a variety of topics.

## Features

- Real-time interaction with users
- Integration with OpenAI's Chat API (GPT-3.5-turbo)
- Secure environment variable management using `python-dotenv`
- Deployed using Streamlit

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/exelsior-chatbot.git
cd exelsior-chatbot
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Windows, use `.env\Scriptsctivate`
```

### 3. Install the Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up the OpenAI API Key
- Create a `.env` file in the root directory and add the following line, replacing `your-openai-api-key` with your actual key:
```
OPENAI_API_KEY=your-openai-api-key
```

### 5. Run the App
```bash
streamlit run chatbot.py
```

The chatbot will launch in your browser, and you can start interacting with it!

## Project Structure
```
chatbot_app/
│
├── chatbot.py           # Main Python file for the Streamlit app
├── requirements.txt     # Dependencies list
├── .env                 # Environment variables file (not shared publicly)
├── .gitignore           # Ensures .env is not committed to version control
```

## Dependencies

- **Streamlit**: For building and deploying the web app
- **OpenAI**: For using the GPT-3.5 language model
- **Python-Dotenv**: To manage environment variables securely

## License

This project is licensed under the MIT License.

---

### Enjoy chatting with Exelsior's Chatbot!
