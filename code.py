import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import AIMessage, HumanMessage
from langchain.memory import ConversationBufferMemory

# 🎓 AI Data Science Tutor - Your interactive learning assistant!
st.title("🤖 AI Conversational Data Science Tutor 📊")
st.subheader("📚 Learn Data Science interactively with AI - Ask about ML, AI, Python & more!")

# Set your Google API key
API_KEY = "your-google-api-key-here"

# Initialize AI model with LangChain
chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=API_KEY)
memory = ConversationBufferMemory()

# Function to check if the question is related to Data Science
def is_data_science_related(question):
    ds_keywords = [
        "data science", "machine learning", "deep learning", "AI", "artificial intelligence",
        "statistics", "python", "pandas", "numpy", "matplotlib", "seaborn", "EDA",
        "feature engineering", "model training", "regression", "classification",
        "clustering", "NLP", "computer vision", "data preprocessing", "feature selection",
        "supervised learning", "unsupervised learning", "reinforcement learning"
    ]
    return any(keyword.lower() in question.lower() for keyword in ds_keywords)

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    emoji = "🧑‍💻" if role == "user" else "🤖"
    st.chat_message(role).write(f"{emoji} {msg.content}")

# Handle user input
user_input = st.chat_input("💡 Ask me anything about Data Science!")
if user_input:
    if is_data_science_related(user_input):
        # Save user message
        st.session_state.messages.append(HumanMessage(content=user_input))
        
        # Get AI response
        response = chat_model.invoke(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))
        
        # Display chat
        st.chat_message("user").write(f"🧑‍💻 {user_input}")
        st.chat_message("assistant").write(f"🤖 {response.content}")
    else:
        st.chat_message("assistant").write("🚫 I can only assist with Data Science topics! Try asking about Machine Learning, AI, Python, or related subjects. 📊")
