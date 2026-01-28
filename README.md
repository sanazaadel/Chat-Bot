### Ollama Chat Bot 
This is a simple chat bot application built using Streamlit and Ollama's language models. The app allows users to select from various Ollama models and interact with them in a chat interface.
## Prerequisites
- Python 3.7 or higher
- An Ollama account and API access
## Installation
1. Clone the repository         
2. Navigate to the project directory:
3. Install the required dependencies:
    ```bash 
   pip install -r requirements.txt
4. Install ollama if you haven't already. Follow the instructions on the [Ollama website](https://github.com/ollama/ollama) to set it up on your local machine.
5. Make sure you have the desired Ollama models downloaded and available on your local Ollama server using the command:
    ```bash 
   ollama pull <model-name>    
    ```
## Setting up Environment Variables
1. Add PYTHONPATH to your environment variables to include the `src` directory. You can do this by adding the following line to your shell configuration file (e.g., `.bashrc`, `.zshrc`):
    ```bash 
   export PYTHONPATH=$PYTHONPATH:{pwd}   
    ```
## Running the App
1. run the Ollama server on your local machine using the command line interface
    ```bash 
   ollama serve    
    ```
1. Start the Streamlit app:
    ```bash 
   streamlit run src/main.py    
    ```     
2. Open your web browser and access the chat bot interface.
## Usage
- Select an Ollama model from the sidebar.
- Type your message in the input box and press Enter to send it.
- The bot will respond based on the selected model.
- Click "New chat" to start a new conversation.
## Customization
- You can modify the list of available models in the `src/main.py` file.
- Adjust the prompt generation logic in `src/utils.py` to change how user inputs are processed.
