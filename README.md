
# AWS Lambda with Pandas

## Local Development

1. Create a virtual environment:

   python3 -m venv venv
2. Activate the virtual environment:

   - For Windows:
     venv\Scripts\activate.bat
   - For Mac/Linux:
     source venv/bin/activate
3. Install the required dependencies:

   pip install -r requirements.txt
4. Start the local API using AWS SAM:

   sam local start-api
