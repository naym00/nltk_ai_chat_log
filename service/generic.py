from nltk.corpus import stopwords
from collections import Counter
import string
import nltk
import re
import os

nltk.download("stopwords")
STOP_WORDS = set(stopwords.words("english"))

class Generic:
    @staticmethod
    def clean_and_tokenize(messages: dict[str, list[str]]):
        words = []
        for msg in messages["user"] + messages["ai"]:
            msg = msg.lower()
            msg = re.sub(rf"[{string.punctuation}]", "", msg)
            tokens = msg.split()
            words.extend([word for word in tokens if word not in STOP_WORDS])
        return words
    
    @staticmethod
    def keyword_analysis(messages: dict[str, list[str]], top_n: int =5):
        words = Generic.clean_and_tokenize(messages)
        most_common = Counter(words).most_common(top_n)
        return [word for word, _ in most_common]
    
    @staticmethod
    def prepare_summary(messages: dict[str, list[str]]):
        total_messages = len(messages["user"]) + len(messages["ai"])
        keywords = Generic.keyword_analysis(messages)

        summary = f"""
    Summary:
    - The conversation had {total_messages} exchanges.
    - The user asked mainly about {' and '.join(keywords[:2])} and related topics.
    - Most common keywords: {', '.join(keywords)}
    """
        print(summary.strip())
    
    @staticmethod
    def parse_chat_log(lines: list[str]):
        messages = {"user": [], "ai": []}
        for line in lines:
            if line.startswith("User:"):
                messages["user"].append(line[5:].strip())
            elif line.startswith("AI:"):
                messages["ai"].append(line[3:].strip())
        return messages
    
    @staticmethod
    def read_file(path: str):
        response = {"flag": True, "lines": []}
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as file:
                response["lines"] = file.readlines()
        else: response["flag"] = False
        return response
    
    @staticmethod
    def generate_summary(path: str = "./static/chat.txt"):
        file_response = Generic.read_file(path)
        if file_response["flag"]:
            user_ai_messages = Generic.parse_chat_log(file_response["lines"])
            Generic.prepare_summary(user_ai_messages)
        else: print("File doesn\'t found!")