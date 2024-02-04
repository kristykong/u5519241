import re

def word_filter_counter(text, filter_words):
    filter_words = [word.lower() for word in filter_words]
    
    words = re.findall(r'\b\w+\b', text.lower())
    
    word_counts = {}
    
    for word in words:
        if word in filter_words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    
    return word_counts


print(word_filter_counter("Hey kong kong!", ["kong"]))  