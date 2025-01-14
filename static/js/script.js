document.getElementById('send-btn').addEventListener('click', sendMessage);

function sendMessage() {
    const userInput = document.getElementById('user-input').value.trim();
    if (userInput === "") return;

    // Display the user's message in the chat box
    displayMessage(userInput, 'user');

    // Show thinking animation and overlay while waiting for the bot's response
    const thinkingOverlay = document.getElementById('thinking-overlay');
    thinkingOverlay.style.display = 'flex'; // Show overlay

    // Send the user's input to the backend (Flask)
    fetch('/chatbot/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: userInput })
    })
    .then(response => response.json())
    .then(data => {
        // Hide thinking animation and display bot response
        thinkingOverlay.style.display = 'none'; // Hide overlay
        if (data.answer) {
            displayMessage(data.answer, 'bot');
        } else {
            displayMessage('Sorry, I could not process your request.', 'bot');
        }
    })
    .catch(error => {
        // Hide thinking animation and display error message
        thinkingOverlay.style.display = 'none'; // Hide overlay
        console.error('Error:', error);
        displayMessage('An error occurred. Please try again later.', 'bot');
    });

    // Clear the input field after sending the message
    document.getElementById('user-input').value = "";
}

// Function to display messages (user and bot) in the chat box
// Function to display messages (user and bot) in the chat box
// Function to display messages (user and bot) in the chat box
function displayMessage(message, sender) {
    const chatBox = document.getElementById('chat-box');
    const messageDiv = document.createElement('div');

    // Set appropriate classes for styling user and bot messages
    if (sender === 'user') {
        messageDiv.classList.add('user-message', 'bg-blue-100', 'text-right', 'p-2', 'rounded-lg', 'mb-2');
    } else {
        messageDiv.classList.add('bot-message', 'bg-gray-100', 'p-2', 'rounded-lg', 'mb-2');
    }

    // Step 1: Handle code blocks (surrounded by triple backticks)
    if (message.includes('```')) {
        message = message.replace(/```([\s\S]+?)```/g, '<pre class="bg-black text-white p-4 rounded-lg">$1</pre>');
    }

    // Step 2: Format lists (bullet points or numbered)
    // Convert lists into <ul> or <ol> based on the message
    message = message.replace(/^[\*\-\+] (.*)/gm, '<li>$1</li>');  // Convert list items into <li> elements
    message = message.split('\n').map(item => item.trim()).join('');
    if (message.includes('<li>')) {
        message = '<ul class="list-disc pl-6">' + message + '</ul>';  // Wrap list items with <ul> and style with padding
    }

    // Step 3: Convert URLs into clickable links
    message = message.replace(/(https?:\/\/[^\s]+)/g, '<a href="$1" target="_blank" class="text-blue-500">Link</a>');

    // Step 4: Apply bold only to specific sections like numbered steps or headings
    message = message.replace(/(\d+\.)/g, '<br/><br/><strong>$1</strong>'); // Make numbered steps bold
    message = message.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');  // Bold specific content using **text**

    // Step 5: Apply italics for emphasis using *text*
    message = message.replace(/\*(.*?)\*/g, '<i>$1</i>');  // Italics text using *text*

    // Step 6: Add paragraph breaks for better readability
    message = message.replace(/\n/g, '<p></p>');

    // Inject the processed message as HTML content
    messageDiv.innerHTML = message;

    // Append the formatted message to the chat box
    chatBox.appendChild(messageDiv);

    // Automatically scroll the chat box to the bottom so the new message is visible
    chatBox.scrollTop = chatBox.scrollHeight;
}



// Allow pressing Enter to send a message
document.getElementById('user-input').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});
