import requests
from bs4 import BeautifulSoup
from time import sleep
import winsound
import difflib
import re

from requests.api import get

# movie_name = "SpiderMan No Way home"
# location = "Mumbai"
# date = "16/12/2021" # DD/MM/YYYY
# movie_code = "ET00319080" # Can be obtained from bookmyshow
# cinema_type = "Carnival"

def main(movie_name, location, date, cinema_type):
    base_url = "https://in.bookmyshow.com"
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"}
    
    date_formatted = "".join(date.split("/")[::-1])
    mov_name_formatted = "-".join(movie_name.lower().split())
    movie_code = get_movie_code(base_url, location, mov_name_formatted)

    url = base_url + f"/buytickets/{mov_name_formatted}-{location.lower()}/movie-{location.lower()}-{movie_code}-MT/{date_formatted}"
    
    it = 0
    while True:
        it += 1
        r = requests.get(url, headers=headers)
        if r.url == url:
            freq = 100
            dur = 50
            for i in range(0, 20):
                winsound.Beep(freq, dur)
                freq += 100
                dur += 50
            soup = BeautifulSoup(r.content, "html.parser")
            venue_list = soup.find("ul", {"id": "venuelist"}).find_all("li")

            translator = str.maketrans({chr(10): '', chr(9): ''})
            # name.translate(translator)

            for venue in venue_list:
                venue_name = venue.text.translate(translator)
                if venue_name.split()[0].rstrip(":").lower() == cinema_type.lower():
                    print(base_url + venue.find("a", {"class": "__venue-name"})["href"])
        print("Iteration", it)
        sleep(15)


def get_movie_code(base_url, location, mov_name_formatted):
    print("Getting movie code...")
    url = base_url + f"/explore/upcoming-movies-{location}?referrerBase=movies"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    movies_list = soup.find_all("a", {"class": "commonStyles__LinkWrapper-sc-133848s-11"})
    res = {}
    for movies in  movies_list:
        link = movies["href"].split("/")
        if len(link) > 1:
            res[link[-2]] = link[-1]
            if link[-2] == mov_name_formatted:
                return link[-1]

    print("Movie code not found! Getting closest matches....")
    matches = difflib.get_close_matches(mov_name_formatted, res.keys(), cutoff=0.8)
    if len(matches) > 0:
        print("Closet matches:")
        for cnt, item in enumerate(matches):
            print(f"{cnt} | {item} | {res[item]}")
            
    ans = input("Enter index number of the closest match if the right movie is found(Y/N):").lower()
    if ans == "y":
        idx = int(input("Enter the index: "))
        return res[matches[idx]]
    elif ans == "n":            
        # Example ET00315808
        while True:
            code = input("Enter the code of the movie manually(ET00XXXXXX): ").rstrip().lstrip()
            if bool(re.match(r"ET00[0-9]{6}", code)):
                return code
            print("Not valid code")


def get_details():
    movie_name = input("Enter Movie Name\n- Only Spaces no Special Characters\n")
    location = input("Enter City\n- Enter Popular cities that appear on bookmyshow\
    \n- Enter full forms, example: National Captial Region instead of NCR\n")
    date = input("Enter date when movie is going to be released\n- Enter a future date\n- Format: DD/MM/YYYY strictly\n") # DD/MM/YYYY
    cinema_type = input("Enter theater type\n- Example: INOX, Cinepolis, Carnival, Gold, etc\n")
    
    return [movie_name, location, date, cinema_type]
    # date_formatted = "".join(date.split("/")[::-1])
    # mov_name_formatted = "-".join(movie_name.lower().split())
    # movie_code = get_movie_code(base_url, location, mov_name_formatted)


if __name__ == "__main__":
    # details = get_details()
    # movie_name = details[0]
    # location = details[1]
    # date = details[2]
    # cinema_type = details[3]
    movie_name = "Spiderman No way Home"
    location = "Mumbai"
    date = "16/12/2021"
    cinema_type = "carnival"
    main(movie_name, location, date, cinema_type)


