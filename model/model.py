# model/test.py
import cohere
import requests
import json
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Cohere API key from environment variable
cohere_client = cohere.Client(os.getenv("COHERE_API_KEY"))

# Load the list of named websites and keywords from JSON file
with open("websites_named.json", "r") as file:
    websites = json.load(file)["websites"]

# Function to scrape website content
def scrape_website(name, url):
    """
    Scrapes content from a given website's URL.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        content = " ".join([para.get_text() for para in paragraphs])
        return f"Content from {name}:\n{content}\n"
    except requests.RequestException as e:
        print(f"Error scraping {name} ({url}): {e}")
        return f"Error retrieving content from {name}.\n"

# Check if the query is relevant to the website's keywords
def is_relevant(query, keywords):
    """
    Determines if the query is relevant based on the website's keywords.
    """
    return any(keyword.lower() in query.lower() for keyword in keywords)

# Function to determine response length based on user query
def get_response_length_based_on_user_query(user_query):
    """
    Determines the response length based on the word count of the user query.
    """
    if not user_query or not user_query.strip():
        raise ValueError("User query cannot be empty or blank.")

    word_count = len(user_query.split())

    # Define thresholds and response lengths as constants
    SHORT_THRESHOLD = 10
    MODERATE_THRESHOLD = 30
    SHORT_RESPONSE = 500
    MODERATE_RESPONSE = 1000
    LONG_RESPONSE = 1500

    if word_count <= SHORT_THRESHOLD:
        return SHORT_RESPONSE
    elif SHORT_THRESHOLD < word_count <= MODERATE_THRESHOLD:
        return MODERATE_RESPONSE
    else:
        return LONG_RESPONSE

# Generate an answer based on relevant website content
def answer_question_from_named_websites(user_query, websites):
    """
    Answers the user's query using content scraped from relevant websites.
    """
    combined_content = ""

    # Scrape and combine content from relevant websites
    for name, data in websites.items():
        url = data["url"]
        keywords = data["keywords"]

        if is_relevant(user_query, keywords):
            print(f"Scraping: {name} - {url}")
            website_content = scrape_website(name, url)
            combined_content += website_content + "\n"
        else:
            print(f"Skipping {name}: Query not relevant.")

    if not combined_content.strip():
        return "Sorry, I couldn't find relevant information for your query on the specified websites."

    # Construct prompt for the LLM
    prompt = f"Based on the content from the following website, please answer the question in a clear and structured manner. Break down your response into easy-to-understand points or steps, if applicable. Here is the website content:\n\n{combined_content}\n\nQuestion: {user_query}"
    
    # Determine response length
    max_tokens = get_response_length_based_on_user_query(user_query)

    # Ask Cohere model
    response = cohere_client.generate(
        model='command-r-plus-08-2024',
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.7
    )

    return response.generations[0].text.strip()
