# api-request-
#intermeadiate app for nvd api
1. Open a terminal 
2. Create a virtual environment:
***python3 -m venv cve-env***
3. Activate the virtual environment:
***source cve-env/bin/activate***
4. Installing Dependencies
***pip install fastapi uvicorn requests***
5. Locate the main.py
6. Running the FastAPI Application
***uvicorn main:app --reload --host 0.0.0.0 --port 8000***
7. Testing the API
Swagger UI ***http://127.0.0.1:8000/docs***
8. Make request with a example of CVE-1999-0095
***http://127.0.0.1:8000/CVE?cveId=CVE-1999-0095***
