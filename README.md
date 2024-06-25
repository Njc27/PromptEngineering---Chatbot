# PromptEngineering-Chatbot


# Detailed instructions to set up and to run the application:

- Installed Streamlit using the command: pip install streamlit.
- Installed necessary modules including transformers and requests.
- Started the LLaMA model by executing the command: ollama run llama3, ensuring it was running on port 11434.
- Collaborated with ChatGPT to write a Python script for a basic chatbot.
- Launched the chatbot using: streamlit run chatbot.py, with Streamlit serving as the frontend interface.
- Iterated with basic greetings and domain-specific commands to train the model.
- With guidance from ChatGPT, enhanced the chatbot to follow the "Chain of Thought" prompt pattern.
- Asked several questions related to the "Education" domain and received detailed, accurate responses.


### Setting Up LLAMA3:

#### Download and Installation
1. **Downloading LLAMA3:**
   - Accessed the GitHub link provided in the assignment to find the LLAMA3 model files.
   - Chose and downloaded the Mac version suitable for my operating system.

2. **Installation Process:**
   - Opened a terminal and executed the command **ollama run llama3** to initiate the installation.
   - The command automatically handled the setup, including any required dependencies and configurations. This process ensures that the LLAMA3 model is correctly installed and ready to be interacted with on the machine.

#### Testing and Interaction
3. **Initial Interaction:**
   - To test if LLAMA3 was functioning properly, I interacted with the model directly in the terminal. This step is crucial to verify that the model is responsive and correctly set up before automating interactions via scripts or APIs.
   - Example query I tested: "Which is the best part in the world to see a beautiful sunset?"
   - This direct interaction helped confirm that the model was operational and capable of processing natural language queries.

4. **Automated Interaction Using Curl:**
   - After confirming the model's responsiveness, I proceeded to test it through a scripted method using the `curl` command. This step is essential for integrating the model with applications that need to automate interactions.
   - Executed the following curl command:
     curl http://localhost:11434/api/chat -d "{ \"model\": \"llama3\", \"messages\": [{\"role\": \"user\", \"content\": \"which is the best place in the world to see a beutiful sunset\"}], \"stream\": false }"
    
   - This command sends a JSON-formatted request to the model's API running on localhost, allowing me to test the model's integration with web technologies and validate its response in a controlled API environment.

### Setting Up Moondream:

#### Installation and Testing
- Followed the same installation and testing procedures as for LLAMA3. Used the command '**ollama run moondream**' to install the Moondream model.

#### API Interaction Testing
- After confirming functionality, tested Moondream using a modified curl command for API interaction:
  curl http://localhost:11434/api/chat -d "{ \"model\": \"moondream\", \"messages\": [{\"role\": \"user\", \"content\": \"which are best roads for a road trip in the USA?\"}], \"stream\": false }"

