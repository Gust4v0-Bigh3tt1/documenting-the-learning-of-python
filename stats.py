def get_num_words(book_text):
    words=book_text.split()
    return len(words)
def get_chars_dict(book_text):
    counts={}
    for ch in book_text:
        lower_char=ch.lower()
        if lower_char not in counts:
            counts[lower_char]=0
        counts[lower_char]+=1
    return counts
def get_report(counts):
    report=[]
    for ch, count in counts.items():
        if ch.isalpha():
            report.append({"char": ch, "count": count})
    report.sort(key=lambda x: x["count"], reverse=True)
    return report