import streamlit as st
import requests
import time
from scrape1 import scrape_website, extract_body_content, clean_body_content, split_dom_content
from parse import parse_with_ollama

st.set_page_config(page_title="AI Web Scraper", page_icon="🌍", layout="wide")

st.title("🌐 AI Web Scraper")
st.write("Enter a website URL and get its cleaned text content. Perfect for quick insights!")

if "dom_content" not in st.session_state:
    st.session_state["dom_content"] = None

url = st.text_input("🔗 Enter Website URL:", placeholder="https://example.com")


if st.button("🚀 Start Scraping"):
    if not url.strip():
        st.warning("⚠️ Please enter a valid URL before scraping.")
    else:
        with st.spinner("🔄 Scraping in progress... Please wait"):
            try:
                start_time = time.time() 
                response = requests.post("http://127.0.0.1:8000/scrape", json={"url": url})

                if response.status_code == 200:
                    data = response.json()
                    execution_time = round(time.time() - start_time, 2) 

                    st.session_state["dom_content"] = data["cleaned_content"]

                    # Success Message
                    st.success(f"✅ Scraping completed in {execution_time} seconds!")

                    with st.expander("📜 View Cleaned Content", expanded=True):
                        st.text_area("📝 Cleaned Text Content:", data["cleaned_content"], height=300)

                    with st.expander("📄 View Content Chunks"):
                        for i, chunk in enumerate(data["content_chunks"], 1):
                            st.text_area(f"Chunk {i}:", chunk, height=100)

                    with st.expander("🛠 Raw HTML (for debugging)"):
                        st.code(data["raw_html"], language="html")

                else:
                    st.error(f"❌ Failed to scrape the website. Error Code: {response.status_code}")

            except requests.exceptions.ConnectionError:
                st.error("⚠️ Unable to connect to the scraping server. Ensure FastAPI is running.")
            except requests.exceptions.Timeout:
                st.error("⏳ The request took too long. Try again later.")
            except Exception as e:
                st.error(f"❌ An unexpected error occurred: {str(e)}")

if st.session_state["dom_content"]:
    st.subheader("🛠 Parse Scraped Content")
    parse_description = st.text_area("Describe what you want to parse:", placeholder="Example: Extract all product details")

    if st.button("🔍 Parse Content"):
        if parse_description.strip():
            with st.spinner("⏳ Parsing content..."):

                dom_chunks = split_dom_content(st.session_state["dom_content"])
                result = parse_with_ollama(dom_chunks, parse_description)
                st.write(result)
                st.success("✅ Parsing completed!")
        else:
            st.warning("⚠️ Please enter a description for parsing.")

# Footer
st.markdown("---")
st.caption("🔍 Built with Streamlit & FastAPI | Developed by Jay 💡")
