import random

with open("./user_agent.txt", "r") as file:
    text_user_agent = file.read()
def generator_user_agent(text_user_agent = text_user_agent):    
    list_user_agent = text_user_agent.split("\n")
    return random.choice(list_user_agent)

if __name__ == "__main__":    
    user_agent = generator_user_agent()
    print(user_agent)