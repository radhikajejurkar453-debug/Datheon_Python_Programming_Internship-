
import json
import re
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "faq_dataset.json"


def load_dataset():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Error: faq_dataset.json was not found.")
        return None

    except json.JSONDecodeError:
        print("Error: Invalid JSON format in faq_dataset.json.")
        return None


def normalize_input(user_input):
    user_input = user_input.lower().strip()
    user_input = re.sub(r"\s+", " ", user_input)
    return user_input


def detect_greeting(user_input, greetings):
    for greeting in greetings:
        pattern = r"\b" + re.escape(greeting) + r"\b"

        if re.search(pattern, user_input):
            return True

    return False


def detect_intents(user_input):
    intents = []

    patterns = {
        "hours": r"\b(hours?|timings?|opening|closing|working hours|operation hours)\b",
        "submission": r"\b(submit|submission|upload|internship project|project link)\b",
        "certificate": r"\b(certificate|certification|completion certificate)\b",
        "returns": r"\b(return|refund|replacement|exchange)\b"
    }

    for intent, pattern in patterns.items():
        if re.search(pattern, user_input):
            intents.append(intent)

    return intents


def get_faq_response(intent, faqs):
    keywords = {
        "hours": ["hours of operation"],
        "submission": ["submit my internship project"],
        "certificate": ["receive my certificate"]
    }

    for faq in faqs:
        question = normalize_input(faq["question"])

        for keyword in keywords.get(intent, []):
            if keyword in question:
                return faq["answer"]

    return None


def generate_response(user_input, dataset):
    user_input = normalize_input(user_input)

    responses = []

    if detect_greeting(user_input, dataset["greetings"]):
        responses.append(
            "Hello! Welcome to the Student Support Assistant. How can I help you?")

    intents = detect_intents(user_input)

    for intent in intents:

        if intent == "returns":
            responses.append(
                "Sorry, return and refund policy information is not "
                "available in the provided FAQ dataset."
            )

        else:
            answer = get_faq_response(intent, dataset["faqs"])

            if answer:
                responses.append(answer)

    if not responses:
        return (
            "Sorry, I couldn't understand your question. "
            "Please ask about business hours, project submission, "
            "certificates, or returns."
        )

    return "\n".join(responses)


def chatbot():
    dataset = load_dataset()

    if dataset is None:
        return

    print("\n======================================")
    print("       STUDENT SUPPORT CHATBOT")
    print("======================================")
    print("Hello! I am your interactive assistant.")
    print("Ask me about business hours, project submission,")
    print("certificates, or return-related queries.")
    print("Type 'bye', 'exit', or 'quit' to end the chat.")
    print("--------------------------------------")

    while True:
        try:
            user_input = input("\nYou: ").strip()

            if not user_input:
                print("Bot: Please enter a question.")
                continue

            exit_commands = ["bye", "exit", "quit"]

            if normalize_input(user_input) in exit_commands:
                print("Bot: Thank you for chatting. Goodbye!")
                break

            response = generate_response(user_input, dataset)

            print("\nBot:", response)

        except (KeyboardInterrupt, EOFError):
            print("\nBot: Chat session ended. Goodbye!")
            break


if __name__ == "__main__":
    chatbot()

