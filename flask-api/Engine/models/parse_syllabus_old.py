import requests
import re
from string import digits
from stempel import StempelStemmer
from stop_words import get_stop_words

# TODO: Parsing syllabus sylabus NEW

def parse_syllabus_old(url):
    description = get_description_from_url(url)
    description = remove_punctuation_and_special_signs(description)
    description = remove_numbers(description)
    description = make_it_small_letters(description)
    description = remove_stopwords(description)

    return description



def get_description_from_url(url):
    resp = requests.get(url, verify=False)
    if resp.status_code != 200:
        print("Error")
        return ""
    else:
        parse_result1 = re.search("\"topic\":\"Tematyka wykładów\",\"description\":\"([^\"]+)\"", resp.text)
        parse_result2 = re.search("\"topic\":\"Tematyka ćwiczeń\",\"description\":\"([^\"]+)\"", resp.text)
        parse_result3 = re.search("\"topic\":\"\",\"description\":\"([^\"]+)\"", resp.text)
        parse_result4 = re.search("\"topic\":\"([^\"]+)\",\"description\":\"([^\"]+)\"", resp.text)
        parse_result5 = re.search("\"topic\":\"([^\"]+)\",\"description\":\"\"", resp.text)

        description = ""
        if parse_result1 is not None:
            description = str(parse_result1.group(1))

        if parse_result2 is not None:
            description += " " + str(parse_result2.group(1))
        elif parse_result3 is not None:
            description += " " + str(parse_result3.group(1))
        elif parse_result4 is not None:
            description += " " + str(parse_result4.group(1)) + " " + str(parse_result4.group(2))
        elif parse_result5 is not None:
            description += " " + str(parse_result5.group(1))

        return description

def remove_punctuation_and_special_signs(description):
    description = description.replace(",", " ")
    description = description.replace(".", "")
    description = description.replace("(", " ")
    description = description.replace(")", " ")
    description = description.replace("!", " ")
    description = description.replace("?", " ")
    description = description.replace("*", " ")
    description = description.replace("\\r", " ")
    description = description.replace("\\n", " ")
    description = description.replace("\\t", " ")
    description = description.replace("#", " ")
    description = re.sub(' +', ' ', description)

    return description

def remove_numbers(description):
    remove_digits = str.maketrans('', '', digits)
    description = description.translate(remove_digits)

    return description

def make_it_small_letters(description):
    return description.lower()

def remove_stopwords(description):
    new_description = ""
    stopWords = get_stop_words('polish')
    for word in description.split():
        if word not in stopWords:
            new_description += word
            new_description += " "
    return new_description



