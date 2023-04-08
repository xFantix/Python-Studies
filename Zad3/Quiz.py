import requests
from time import perf_counter


URL = 'https://opentdb.com/api.php?amount=10&type=boolean'

user_good_response = 0
user_bad_response = 0
time = 0

def get_questions():
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()['results']
    else:
        print("Error")
        return []

questions = get_questions()
start = input('Wcisnij 1 by zacząć quiz\n')

if start == "1":
    for item in questions:
        print(item['question'])
        t1_start = perf_counter()
        response_for_question = input("True\nFalse\n")
        if response_for_question == str(item['correct_answer']):
            user_good_response += 1
        else:
            user_bad_response += 1
        t1_stop = perf_counter()
        time = time + t1_stop - t1_start

    print(f"True / False {user_good_response} / {user_bad_response}, time: {time}, average time: {time/10}")

else:
    print("Koniec programu")