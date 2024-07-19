# Sum It Up!
Sum It Up is a web application to summarize any text passage with custom prompting, leveraging Ollama

## Demo Run
Here is a demo run of Sum It Up in action. <br>
In this demo, we're copying a chunk of a text passage about the Toronto Raptors and using Sum It Up to summarize it in fewer words.

https://github.com/user-attachments/assets/8a2478e4-c1f4-4eba-b407-a1fd34ed2f0a

## Tech Stack
- Python
- Langchain
- Llama3
- Ollama
- FastAPI
- React
- Axios

# Instructions for Local Setup

1. Create a Python virtual environment:

   ```
    python<version> -m venv <virtual-environment-name>
   ```
2. Head to https://github.com/ollama/ollama?tab=readme-ov-file and download the Ollama framework locally on your OS
3. Open up Terminal and install llama3
   ```
    ollama pull llama3
   ```
4. Clone the repository:

    ```
     git clone https://github.com/tonyngoo/SumItUp.git
    ```
5. Use specifically the master branch as the main branch was for deployment:
    ```
     git checkout master
    ```
6. Install required packages on your virtual environment:
  - First, navigate to the `requirements.txt` file in the `backend` folder

    ```
     cd backend
    ```
  - Next, install the requirements

    ```
     pip install -r requirements.txt
    ```
7. In your root directory, run uvicorn, an ASGI (Asynchronous Server Gateway Interface) server to handle FastAPI
   
    ```
     uvicorn backend.main:app --reload
    ```
8. Run the app

    ```
     npm start
    ```
9. Time to Sum It Up!
