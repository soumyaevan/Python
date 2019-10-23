import requests
from termcolor import colored
from pyfiglet import figlet_format
header = figlet_format("BAD JOKE!!!")
header = colored(header,color="magenta")
print(header)
term = input("For what topic you want joke? ")
url = "https://www.icanhazdadjoke.com/search"
res = requests.get(
    url,
    headers={"Accept":"application/json"},
    params={"term":term}
    ).json()
num_of_joke = res["total_jokes"]
print(f"Number of jokes found: {num_of_joke}")
if(num_of_joke>0):
    result = res["results"]
    print("The jokes are: ")
    for item in result:
        print(item["joke"])
