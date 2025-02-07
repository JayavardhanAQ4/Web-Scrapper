from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

AUTH = 'brd-customer-hl_f34a5e46-zone-ai_scrapper:fxt19m118fs7'
SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'

def scrape_website(website):
    """Scrape the given website using Selenium"""
    try:
        print("Launching Chrome Browser..")
        sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, browser_name="chrome", vendor_prefix="goog")
        options = ChromeOptions()
        options.add_argument("--headless")

        with Remote(command_executor=sbr_connection, options=options) as driver:
            print('Connected! Navigating...')
            driver.get(website)
            time.sleep(10)
            
            html = driver.page_source
            return html

    except Exception as e:
        print(f"Error occurred: {e}")
        return None

def extract_body_content(html_content):
    """Extracts the body content from the HTML"""
    if not html_content:
        return "No HTML content received."

    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.find('body')
    
    return str(body_content) if body_content else "No body content found."

def clean_body_content(body_content):
    """Cleans extracted content by removing scripts and styles"""
    soup = BeautifulSoup(body_content, 'html.parser')

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
        
    cleaned_content = soup.get_text(separator='\n')
    cleaned_content = "\n".join([line.strip() for line in cleaned_content.split('\n') if line.strip()])
    
    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    """Splits DOM content into smaller chunks for processing"""
    return [dom_content[i:i+max_length] for i in range(0, len(dom_content), max_length)]
