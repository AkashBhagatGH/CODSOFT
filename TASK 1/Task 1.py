import time
import random

now = time.strftime("%Y-%m-%d %H:%M:%S")
interesting_facts = [
    "The footprints left by astronauts on the moon will likely remain for millions of years, as there's no wind or water to erode them.",
    "More than 80% of the Earth's oceans remain unexplored, making them one of the last truly unknown frontiers on our planet.",
    " If uncoiled, the DNA in all of your cells would stretch about twice the diameter of the Solar System!",
    "Honey never spoils! Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.",
    "Human eyes can detect over 10 million different colors, and our brain interprets the colors based on a combination of red, blue, and green receptors.",
    "There are museums around the world, like the Museum of Non-Visible Art, which “exhibits” artworks that are only in the artist’s imagination. Visitors pay to experience a concept or idea rather than a physical piece."
]

def chatbot(user_input, memory):
    user_input = user_input.lower()

    if "hi" in user_input or "hello" in user_input:
        return "Hi there! I'm a chatbot here to assist you. What's your name?"
    elif "my name is" in user_input:
        name = user_input.split("my name is")[-1].strip()
        memory['name'] = name
        return f"Nice to meet you, {name}!"
    elif "what is your name" in user_input:
        return "I'm just a chatbot, so I don't have a name, but you can call me anything."
    elif "where are you from" in user_input:
        return "I'm from the digital world, always ready to chat!"
    elif "how are you" in user_input:
        return "I'm fine. How about you?"
    elif "do you have any hobbies" in user_input or "interests" in user_input:
        return "I'm always busy helping users, so my hobby is chatting with people like you!"
    elif "what did you eat today" in user_input or "what do you like to eat" in user_input:
        return "I don't eat, but I can help you find delicious recipes and food-related information."
    elif "favorite color" in user_input:
        return "I'm a chatbot, so I don't have personal preferences for colors."
    elif "tell me a joke" in user_input or "another joke" in user_input:
        return "Parallel Lines are so Common, It's a shame they'll never meet."
    elif "tell me an interesting fact" in user_input or "another interesting fact" in user_input:
        return random.choice(interesting_facts)
    elif "weather in" in user_input:
        return "I can help you with weather information soon. Stay tuned for updates!"
    elif "latest news" in user_input:
        return "I can help you with the latest news soon. Stay tuned for updates!"
    elif "translate" in user_input:
        return "I can help you with translations soon. Stay tuned for updates!"
    elif "what is the time now" in user_input:
        return now
    elif "bye" in user_input:
        return f"Goodbye, {memory.get('name', 'friend')}! Take care and have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase your sentence?"

print("Chatbot: Hi! I'm a simple chatbot, I'm here to assist you!")

memory = {}

while True:
    user_input = input("Me: ")  
    if user_input.lower() == 'bye':
        print(f"Chatbot: Goodbye, {memory.get('name', 'friend')}! Have a great day!")
        break  
    
    response = chatbot(user_input, memory)  
    print("Chatbot:", response) # type: ignore