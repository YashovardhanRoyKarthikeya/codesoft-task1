import random
memory={}
responses_AI={
        "greetings":["Hello!","Hi there!","Hey!","Hey, how's it going?"],
        "farewell":["Goodbye!","See you later!","Bye! Take care!"],
        "acknowledge":["Great! Let me know if there's anything else I can help with."],
        "thankyou":["You're welcome! If you have any further questions or need assistance, feel free to ask."],
        "questions":["I'm doing well, thank you!","I'm good, thanks for asking.","All good!"],
        "default_responses":["Sorry, I didn't catch that. Could you please repeat?",
            "I'm not sure I understand. Could you provide more details?",
            "Hmm, I'm having trouble understanding. Can you rephrase that?",
            "Apologies, could you clarify what you mean?",
            "I'm still learning! Can you try saying that another way?",
            "It seems I'm not following. Could you explain again?",
            "I'm having trouble processing that. Can you try again?",
            "That's a bit unclear to me. Can you give me more context?",
            "I'm afraid I didn't get that. Can you elaborate?",
            "Sorry, could you please clarify what you're asking?",
            "I'm not quite sure what you mean. Could you explain further?",
            "Hmm, that's not ringing any bells. Can you give me more details?",
            "I'm having trouble processing your request. Can you try again?",
            "It seems like I'm missing something. Could you provide additional information?",
            "Sorry, I'm drawing a blank. Can you give me some more context?",
            "I'm not sure I'm following. Could you break it down for me?",
            "I'm having difficulty understanding your message. Can you simplify it?",
            "I'm struggling to understand. Could you phrase it differently?",
            "It appears I'm not getting your point. Can you try expressing it differently?",
            "Sorry, I'm a bit confused. Can you provide more clarity?"],
    }
responses_HI={
        "greetings":["hi","hello","Hey","good morning"],
        "farewell":["bye","quit"],
        "thankyou":["thanks","thankyou so much","you are great","thats working"],
        "acknowledge":["ok"],
        "questions":["how are you?"],
        "commands":["greet","farewell","ask","repeat","memory","forget","clear"]
    }
def respond(input_text):
    input_text_lower=input_text.lower()
    if input_text_lower in memory:
        return memory[input_text_lower]
    if input_text_lower in responses_HI["greetings"]:
        response=random.choice(responses_AI["greetings"])
    elif input_text_lower in responses_HI["farewell"]:
        response=random.choice(responses_AI["farewell"])
    elif input_text_lower in responses_HI["questions"]:
        response=random.choice(responses_AI["questions"])
    elif input_text_lower in responses_HI["thankyou"]:
        response=random.choice(responses_AI["thankyou"])
    elif input_text_lower in responses_HI["acknowledge"]:
        response=random.choice(responses_AI["acknowledge"])
    elif "my name is" in input_text_lower:
        name=input_text_lower.split("my name is")[-1].strip()
        response=f"Nice to meet you, {name}!"
        memory["user_name"]=name
    elif "what is my name" in input_text_lower:
        if "user_name" in memory:
            response=f"Your name is {memory['user_name']}."
        else:
            response="I don't know your name yet."
    else:
        response=random.choice(responses_AI["default_responses"])
    memory[input_text_lower]=response
    return response
def start():
    print("Chatbot: Hi! How can I help you today?")
    while True:
        user_input=input("You:")
        response=respond(user_input)
        print("Chatbot:",response)
        if user_input.lower() in responses_HI["farewell"]:
            break
start()
