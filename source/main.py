import re
import os
import string
from collections import Counter

import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('stopwords')

STOP_WORDS = list(set(stopwords.words('english')))

def read_chat_log(filename):
    pattern = re.compile(r'^(User|AI):\s*(.*)$')
    chats = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            match = pattern.match(line)
            if match:
                speaker, message = match.groups()
                chats.append((speaker, message))
    return chats

def count_messages(chats):
    total = len(chats)
    return total

def extract_keywords(chats, top_n=5):
    documents = [' '.join([msg for _, msg in chats])]
    
    vectorizer = TfidfVectorizer(stop_words=STOP_WORDS, max_features=top_n)
    tfidf_matrix = vectorizer.fit_transform(documents)
    feature_names = vectorizer.get_feature_names_out()
    scores = tfidf_matrix.toarray()[0]

    keywords_scores = sorted(zip(feature_names, scores), key=lambda x: x[1], reverse=True)
    keywords = [kw for kw, _ in keywords_scores]
    return keywords

def conversation_topic(keywords):
    topics = {
        'python': ['python', 'code', 'programming', 'script', 'language'],
        'machine learning': ['machine', 'learning', 'model', 'data', 'train', 'ai'],
        'web development': ['web', 'html', 'css', 'javascript', 'server'],
        'ai': ['ai', 'artificial', 'intelligence', 'neural', 'network', 'deep'],
    }
    for topic, keywords_list in topics.items():
        if any(k in keywords for k in keywords_list):
            return topic
    return 'unknown'

def generate_summary(chats):
    total = count_messages(chats)
    keywords = extract_keywords(chats)
    topic = conversation_topic(keywords)
    summary = f"Summary:\n" \
              f"- The conversation had {total} exchanges.\n" \
              f"- The user asked mainly about {topic}.\n" \
              f"- Most common keywords: {', '.join(keywords)}."
              
    return summary


if __name__ == "__main__":
    input_file = "chat_logs/chat.txt" 

    if input_file:
        try:
            chats = read_chat_log(input_file)
            print(f"Summary for file: {input_file}")
            print(generate_summary(chats))
        except FileNotFoundError:
            print(f"Error: File '{input_file}' not found.")