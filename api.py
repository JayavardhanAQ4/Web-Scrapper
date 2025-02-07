from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from scrape1 import scrape_website, extract_body_content, clean_body_content, split_dom_content

app = FastAPI(
    title="AI Web Scraper API",
    description="Scrape and process website content via API",
    version="1.0.0"
)

class ScrapeRequest(BaseModel):
    url: str

@app.get("/")
def read_root():
    return {"message": "Welcome to AI Web Scraper API!"}

@app.post("/scrape")
def scrape_webpage(request: ScrapeRequest):
    html_content = scrape_website(request.url)
    if not html_content:
        raise HTTPException(status_code=500, detail="Failed to retrieve website content")

    body_content = extract_body_content(html_content)
    cleaned_content = clean_body_content(body_content)
    chunks = split_dom_content(cleaned_content, max_length=6000)

    return {
        "url": request.url,
        "raw_html": html_content, 
        "cleaned_content": cleaned_content,
        "content_chunks": chunks
    }
