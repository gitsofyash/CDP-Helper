# Customer Data Platform (CDP) Chatbot

This chatbot is designed to answer "how-to" questions related to four popular Customer Data Platforms (CDPs): Segment, mParticle, Lytics, and Zeotap. It extracts relevant information from the official documentation of these platforms to guide users on how to perform tasks or achieve specific outcomes within each platform.

## Core Functionalities

1. **Answer "How-to" Questions:**
   - The chatbot can respond to user queries about specific tasks or features within Segment, mParticle, Lytics, and Zeotap.
   - Example questions:
     - "How do I set up a new source in Segment?"
     - "How can I create a user profile in mParticle?"
     - "How do I build an audience segment in Lytics?"
     - "How can I integrate my data with Zeotap?"

2. **Extract Information from Documentation:**
   - The chatbot retrieves relevant information from the official documentation of the four CDPs:
     - [Segment Documentation](https://segment.com/docs/?ref=nav)
     - [mParticle Documentation](https://docs.mparticle.com/)
     - [Lytics Documentation](https://docs.lytics.com/)
     - [Zeotap Documentation](https://docs.zeotap.com/home/en-us/)

3. **Handle Variations in Questions:**
   - The chatbot can handle questions with size variations and irrelevant questions (e.g., non-CDP-related queries).

4. **Bonus Features:**
   - **Cross-CDP Comparisons:** The chatbot can provide comparisons between CDPs on specific features or functionalities.
   - **Advanced "How-to" Questions:** The chatbot handles complex use cases and configurations.

## Installation

### Prerequisites

- Python 3.x
- Flask
- A valid Cohere API Key for processing NLP tasks

### Getting the Cohere API Key

To use Cohere for NLP tasks in this project, you'll need to sign up for a Cohere account and obtain your API key.

1. Go to the [Cohere website](https://cohere.ai/).
2. Sign up for an account.
3. Once signed in, navigate to the [API page](https://cohere.ai/docs/).
4. Generate a new API key.
5. Copy the API key, which you'll use to authenticate requests to Cohere's API.

### Setting Up the Project

1. Clone the repository to your local machine:

    ```bash
    git clone <repository-url>
    ```

2. Navigate into the project directory:

    ```bash
    cd <project-directory>
    ```

3. Set up a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:
   - On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Create a `.env` file in the root directory and add your Cohere API key:

    ```bash
    COHERE_API_KEY=your-cohere-api-key-here
    ```

7. Run the Flask server:

    ```bash
    flask run
    ```

8. The chatbot will be available at `http://localhost:5000`.

## Usage

- Open the application in your browser and start interacting with the chatbot.
- Ask how-to questions related to Segment, mParticle, Lytics, or Zeotap, and the chatbot will extract and display the relevant information from the documentation.

## Contributing

Feel free to open issues and submit pull requests for any improvements or bug fixes. Contributions are always welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Cohere API](https://cohere.ai) for NLP processing.
- [Segment Documentation](https://segment.com/docs/?ref=nav).
- [mParticle Documentation](https://docs.mparticle.com/).
- [Lytics Documentation](https://docs.lytics.com/).
- [Zeotap Documentation](https://docs.zeotap.com/home/en-us/).
