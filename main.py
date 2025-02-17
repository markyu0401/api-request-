import logging
from fastapi import FastAPI, Query
from fastapi.responses import RedirectResponse
import requests

# Initialize FastAPI
app = FastAPI()

# NVD API Base URL
NVD_API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

# Configure logging to see what URLs are requested
logging.basicConfig(level=logging.INFO)

@app.get("/", tags=["Status"])
def home():
    return {"message": "FastAPI is running successfully!"}

# Redirect `/cve` → `/CVE`
@app.get("/cve", include_in_schema=False)
def redirect_to_uppercase():
    return RedirectResponse(url="/CVE")

# Main API Endpoint
@app.get("/CVE", tags=["CVE Data"])
def get_cve(
    cve_id: str = Query(None, alias="cveId"),
    keyword_search: str = Query(None, alias="keywordSearch")
):
    """
    Fetch CVE details from the NVD API.
    """
    headers = {"Accept": "application/json"}

    # Convert `cveId` to uppercase before making API call
    if cve_id:
        cve_id = cve_id.upper()  # Force uppercase
        url = f"{NVD_API_URL}?cveId={cve_id}"
    elif keyword_search:
        url = f"{NVD_API_URL}?keywordSearch={keyword_search}"
    else:
        return {"error": "Please provide either a CVE ID or a keyword for search."}

    logging.info(f"Fetching data from NVD API: {url}")  # Log the request URL

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data from NVD API", "status_code": response.status_code}
