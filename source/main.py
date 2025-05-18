import re
import os
import string
from collections import Counter


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

def generate_summary(chats):
    total = count_messages(chats)
    summary = f"Summary:\n" \
              f"- The conversation had {total} exchanges.\n" \
              
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