# Rule-Based Interactive Terminal Assistant / Chatbot

A Python-based interactive terminal chatbot developed as part of **Datheon Python Programming Internship – Task 4**.

The chatbot uses rule-based logic, regular expressions, keyword matching, and a JSON FAQ dataset to identify user queries and provide relevant responses.

## Project Overview

The Rule-Based Interactive Terminal Assistant is designed to simulate a basic customer-support chatbot.

It recognizes greetings, identifies user intents, answers frequently asked questions, handles multiple intents in a single message, and provides fallback responses for unrecognized queries.

The chatbot also supports exit commands such as `bye`, `exit`, and `quit`.

## Features

- **Greeting Recognition:** Responds to common greetings such as Hello, Hi, and Good Morning.
- **Intent Recognition:** Identifies user queries using predefined keywords and regular expressions.
- **FAQ Management:** Loads questions and answers dynamically from a JSON dataset.
- **Business Hours Information:** Provides business operating hours.
- **Internship Support:** Answers questions about project submission and internship requirements.
- **Certificate Information:** Provides certificate processing details.
- **Multi-Intent Recognition:** Handles multiple recognized intents in a single message.
- **Fallback Responses:** Responds appropriately when a query is not recognized.
- **Exit Commands:** Allows users to end the conversation using Bye, Exit, or Quit.
- **Error Handling:** Handles missing or invalid JSON files and interrupted sessions.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Main programming language |
| re | Regular expression and keyword matching |
| json | Loading FAQ data |
| pathlib | File path management |
| String Processing | Input normalization |
| Exception Handling | Managing runtime errors |

## Project Structure

```text
Task_4_Chatbot/
│
├── chatbot.py
├── faq_dataset.json
├── README.md
└── screenshots/
    ├── chatbot_running.png
    └── chatbot_responses.png
```

## FAQ Dataset

The chatbot uses `faq_dataset.json` to store greetings, frequently asked questions, and their corresponding answers.

The dataset includes information about:

- Business operating hours
- Internship project submission
- Public GitHub repository requirements
- Certificate processing time
- Weekend operating hours
- Return and refund policy information
- Internship project support

Additional questions and answers can be added to the JSON file without changing the dataset structure.

## Installation and Requirements

**Requirements:**

- Python 3.x
- VS Code or any Python-supported editor
- No external Python packages required.

The project uses Python's built-in libraries.

## How to Run the Project

### Step 1: Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Task_4_Chatbot.git
```

### Step 2: Navigate to the project folder

```bash
cd Task_4_Chatbot
```

### Step 3: Run the chatbot

```bash
python chatbot.py
```

### Step 4: Start interacting

Enter your questions in the terminal and receive responses from the chatbot.

Type `bye`, `exit`, or `quit` to close the application.

## Sample Interaction

```text
======================================
       STUDENT SUPPORT CHATBOT
======================================

Hello! I am your interactive assistant.

You: Hello

Bot: Hello! Welcome to the Student Support Assistant.
How can I help you?

You: What are your working hours?

Bot: We operate Monday through Friday
from 9:00 AM to 6:00 PM IST.

You: How do I submit my internship project?

Bot: You can submit your public GitHub repository
link through your Student Workspace.

You: When will I receive my certificate?

Bot: Certificates are reviewed and issued within
3-5 business days after your code review.

You: bye

Bot: Thank you for chatting. Goodbye!
```

## Testing

The chatbot can be tested using the following test cases.

| Test Case | Input | Expected Result |
|---|---|---|
| TC01 | Hello | Greeting response |
| TC02 | What are your hours? | Business hours information |
| TC03 | How do I submit my project? | Project submission instructions |
| TC04 | When will I get my certificate? | Certificate processing information |
| TC05 | Hi, what are your hours? | Greeting and business hours response |
| TC06 | What is your return policy? | Return policy information unavailable |
| TC07 | Unknown question | Fallback response |
| TC08 | bye | Chatbot exits |
| TC09 | exit | Chatbot exits |
| TC10 | quit | Chatbot exits |

## Learning Outcomes

Through this project, I gained practical experience in:

- Python functions and modular programming.
- Regular expressions and pattern matching.
- JSON file handling.
- String normalization and processing.
- Rule-based intent recognition.
- Multi-intent conversational logic.
- Exception handling and debugging.

## Future Improvements

- Add more FAQs and response categories.
- Improve flexible question matching.
- Add a graphical user interface.
- Integrate database-based FAQ management.
- Add multilingual conversational support.

## Author

**Radhika Jejurkar**

B.Sc. Data Science Student

## Internship Task

**Organization:** Datheon

**Program:** Python Programming Internship

**Task:** Task 4 – Rule-Based Interactive Terminal Assistant / Chatbot

---

*Developed as a practical Python programming project to explore rule-based conversational systems and automated customer support.*
