from config import key
import task
import requests

def parse_function_response():
    pass
def run_conversation(user_message):
    messages = [] # list which all messages


    system_message = " you are an AI bot that can ddo everything using function call. when you are asked to do something, use the function call you have available and then respond with message"
    message = {"role": "user", "parts": [{"text": system_message + " \n" +user_message}]}
    messages.append(message)
    data = {"contents": [messages],
            "tools":[{"functionDeclarations": task.definitions}]}
    url="https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key="+key
    response = requests.post(url, json=data)

    if response.status_code !=200:
        print(response.text)
    t1 = response.json()
    if "content" not in t1.get("candidates")[0]:
        print("Error: No content in response")
    message=t1.get("candidates")[0].get("content").get("parts")[0].get("text")
    if'functioncall'in  message[0]:
        resp1=parse_function_response(message)
        return resp1
    #print(t1)
    #t2=t1.get("candidates")[0].get("content").get("parts")[0].get("text")
    #print(t2)
        #print("now we are getting", t1)

if __name__ ==" __main__":
    user_message="hello"
    run_conversation(user_message)
