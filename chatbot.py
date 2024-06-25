import streamlit as st
import requests
import json

# Streamlit app title
st.title("Education Domain Chatbot with Chain of Thought Prompt")

# Input text box for user query
user_input = st.text_input("You:", "")

# Initialize conversation history
if "history" not in st.session_state:
    st.session_state.history = []

# Function to clear conversation history
def clear_conversation():
    st.session_state.history = []

# Add Clear Conversation button
if st.button("Clear Conversation"):
    clear_conversation()

# Education-specific context with Chain of Thought pattern
domain_context = (
    "You are a knowledgeable assistant specializing in education. "
    "You can provide information about courses, study tips, career guidance, exam preparation, and educational trends. "
    "If the user asks a question outside the education domain, answer briefly but remind them to ask education-specific questions. "
    "Break down your response into a step-by-step process to answer complex queries. "
    "Here is the user's query:"
)

# Function to get response from local LLM
def get_llm_response(query):
    try:
        url = "http://localhost:11434/api/generate"
        prompt = f"{domain_context}\n\nUser: {query}\nAssistant:"
        
        payload = {
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            raw_response_text = response.text
            # st.write("Debug: Raw Server Response", raw_response_text)  # Print the raw response for debugging
            
            try:
                # Attempt to parse the JSON response
                response_data = json.loads(raw_response_text)
                # st.write("Debug: Parsed JSON Response", response_data)  # Print the parsed JSON for further inspection
                
                # Adjust based on actual response structure
                if "response" in response_data:
                    return response_data["response"]
                else:
                    return "Error: Unexpected response structure."
            except json.JSONDecodeError as e:
                return f"JSON Decode Error: {str(e)}"

        else:
            return f"Error: Unable to get response from the LLM. Status code: {response.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"

# Process user input and get LLM response
if user_input:
    bot_response = get_llm_response(user_input)
    st.session_state.history.append({"user": user_input, "bot": bot_response})

# Display conversation history
for chat in st.session_state.history:
    st.write(f"**You**: {chat['user']}")
    st.write(f"**Bot**: {chat['bot']}")
    st.write("---")
