import random
import time
 
RULES = [
    {
        "keys": ["hello", "hi", "hey", ],
        "replies": [
            "Hey there! 👋 Good to see you!",
            "Hi! What's on your mind?",
            "Hello! 😊 Nice of you to drop by.",
        ],
    },
    {
        "keys": ["how are you", "how r u", "how do you do", "you okay"],
        "replies": [
            "I'm doing great, thanks for asking! 😊",
            "All good on my end! How about you?",
            "Feeling fantastic — just waiting to chat!",
        ],
    },
    {
        "keys": ["your name", "who are you", "what are you"],
        "replies": [
            "I'm ChatBot 🤖 — your friendly rule-based assistant!",
            "Call me ChatBot. I'm simple but I try my best 😄",
        ],
    },
    {
        "keys": ["joke", "funny", "make me laugh"],
        "replies": [
            "Why don't scientists trust atoms? Because they make up everything! 😄",
            "I told my computer I needed a break… now it won't stop sending me Kit-Kat ads 🍫",
            "Why did the programmer quit? Because he didn't get arrays. 😅",
        ],
    },
    {
        "keys": ["what can you do", "help", "capabilities"],
        "replies": [
            "I can chat, tell jokes, and brighten your day!\n"
            "  Try: 'hello', 'how are you', 'tell me a joke', or 'bye' 😊",
        ],
    },
    {
        "keys": ["thanks", "thank you", "thx", "ty", "cheers"],
        "replies": [
            "You're welcome! 😊",
            "Anytime! Happy to help.",
            "No problem at all! 🙌",
        ],
    },
    {
        "keys": ["good", "great", "fine", "awesome", "wonderful", "fantastic"],
        "replies": [
            "Love to hear that! 😄",
            "That's the spirit! ✨",
            "Awesome! Keep it up! 🙌",
        ],
    },
    {
        "keys": ["bad", "sad", "not good", "terrible", "awful"],
        "replies": [
            "Oh no, I'm sorry to hear that 😔 Hope things get better soon!",
            "Sending good vibes your way 💛",
            "Hang in there — things will look up!",
        ],
    },
    {
        "keys": ["age", "old", "born", "birthday"],
        "replies": [
            "I was born the moment my code was run — so I'm pretty fresh! 😄",
        ],
    },
    {
        "keys": ["bye", "goodbye", "see you", "cya", "later", "exit", "quit"],
        "replies": [
            "Goodbye! Have an amazing day! 👋",
            "See you later! Take care 😊",
            "Bye bye! Come back anytime 🤗",
        ],
        "farewell": True,
    },
]
 
FALLBACKS = [
    "Hmm, I'm not sure about that 🤔 Type 'help' to see what I can do!",
    "I didn't quite catch that 😅 Try rephrasing?",
    "Not sure I follow — but I'm all ears! 👂",
]

def get_response(user_input: str) -> tuple[str, bool]:
    """Return (reply_text, is_farewell)."""
    text = user_input.lower().strip()
    for rule in RULES:
        if any(key in text for key in rule["keys"]):
            reply = random.choice(rule["replies"])
            return reply, rule.get("farewell", False)
    return random.choice(FALLBACKS), False
 
 
def typing_pause(text: str) -> None:
    """Simulate a realistic typing delay before printing."""
    delay = min(0.04 * len(text), 1.8)  # cap at 1.8 s
    time.sleep(delay)
 
 

def run_chatbot() -> None:
    print("\n" + "─" * 44)
    print("  ChatBot 🤖  |  type 'bye' to exit")
    print("─" * 44)
 
    # Opening line
    opener = "Hey! 👋 I'm ChatBot. How can I help you today?"
    typing_pause(opener)
    print(f"\nChatBot: {opener}\n")
 
    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nChatBot: Catch you later! 👋\n")
            break
 
        if not user_input:
            print("ChatBot: Go ahead, I'm listening 😊\n")
            continue
 
        reply, farewell = get_response(user_input)
        typing_pause(reply)
        print(f"\nChatBot: {reply}\n")
 
        if farewell:
            break
 
    print("─" * 44 + "\n")
 
 
if __name__ == "__main__":
    run_chatbot()
 
