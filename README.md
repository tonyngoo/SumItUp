# Sum It Up!
Sum It Up is a web application to summarize any text passage with custom prompting, leveraging Ollama

## Demo Run
Here is a demo run of Sum It Up in action.
In this demo, we're copying a chunk of a text passage about the Toronto Raptors and using Sum It Up to summarize it in fewer words.

https://github.com/user-attachments/assets/fa9080bc-1003-4915-bbdf-9099062fd94d

## Tech Stack
- Python
- Langchain
- Ollama
- FastAPI
- React
- Axios

# Instructions for Local Setup

1. Create a Python virtual environment:

   ```
    python<version> -m venv <virtual-environment-name>
   ```
2. Head to https://github.com/ollama/ollama?tab=readme-ov-file and download Ollama locally on your OS
3. Clone the master branch:

   ```
    git clone https://github.com/tonyngoo/SumItUp.git
   ```
4. Install required packages on your virtual environment:
  - First, navigate to the `requirements.txt` file in the `backend` folder

   ```
    cd backend
   ```
  - Next, install the requirements

   ```
    pip install -r requirements.txt
   ```
5. In your root directory, run uvicorn, an ASGI (Asynchronous Server Gateway Interface) server to handle FastAPI
   
   ```
     uvicorn backend.main:app --reload
   ```
7. Run the app

   ```
     npm start
   ```
9. Time to Sum It Up!
