# AI Web Scraper

A powerful web scraping solution built with FastAPI and Streamlit, featuring AI-powered content parsing capabilities.

## Overview

AI Web Scraper is an advanced web content extraction tool that combines modern web scraping techniques with artificial intelligence for efficient data processing. The application utilizes FastAPI for backend operations and Streamlit for the user interface, while incorporating Ollama for intelligent content parsing.

## Features

### Core Capabilities

- Robust web scraping using BeautifulSoup and Requests
- Intelligent content cleaning and HTML processing
- AI-powered parsing for structured data extraction
- Content chunking for optimal processing
- User-friendly interface for easy interaction

### Technical Highlights

- High-performance FastAPI backend
- Interactive Streamlit-based frontend
- Advanced content cleaning algorithms
- Integration with Ollama for AI parsing
- Scalable chunked content processing

## Technology Stack

### Backend
- FastAPI - Web framework
- BeautifulSoup4 - HTML parsing
- Requests - HTTP client
- Pydantic - Data validation

### Frontend
- Streamlit - User interface
- Streamlit Components - Enhanced UI elements

### AI Integration
- Ollama - Content parsing and analysis

### Deployment Options
- Docker containerization
- Cloud platform support (AWS, Heroku, Render)

## Project Structure

```
ai-web-scraper/
├── backend/
│   ├── scrape1.py        # Core scraping logic
│   ├── parse.py          # AI parsing implementation
│   ├── main.py          # FastAPI application
│   └── requirements.txt  # Backend dependencies
├── frontend/
│   ├── app.py           # Streamlit interface
│   └── requirements.txt  # Frontend dependencies
├── assets/              # Project assets
├── docs/               # Documentation
├── .gitignore
├── README.md
└── LICENSE
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-web-scraper.git
cd ai-web-scraper
```

2. Install backend dependencies:
```bash
cd backend
pip install -r requirements.txt
```

3. Install frontend dependencies:
```bash
cd ../frontend
pip install -r requirements.txt
```

## Usage

1. Start the FastAPI backend:
```bash
cd backend
uvicorn main:app --reload
```

2. Launch the Streamlit frontend:
```bash
cd frontend
streamlit run app.py
```

3. Access the application at `http://localhost:8501`

## API Documentation

The FastAPI backend provides comprehensive API documentation at `/docs` endpoint when running locally. This includes:

- Detailed endpoint specifications
- Request/response schemas
- Interactive API testing interface

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- FastAPI documentation and community
- Streamlit team for the excellent frontend framework
- Ollama team for AI capabilities
- Contributors and maintainers

## Contact

Project Link:
