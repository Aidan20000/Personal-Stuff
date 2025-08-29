import requests

def find_all_instances(string, char):
    return [i for i, c in enumerate(string) if c == char]

while True:
    answers = []
    baseUrl = "https://api.datamuse.com/words?sp="
    print("Wordscapes Cheats Active!\nType your word with known letters and what you dont know fill in with a ?")
    inputStr = input("")

    url = baseUrl + inputStr
    questions = find_all_instances(inputStr, "?")

    response = requests.get(url).json()

    print("What letter Options are there?")
    letterOptions = input("")

    for item in response:
        curr = True
        for num in questions:
            if item["word"][num] in letterOptions:
                continue
            else:
                curr = False
        if curr:
            answers.append(item["word"])

    print(answers)