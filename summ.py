from utils import clean_text

def summarize(text):
    cleaned = clean_text(text)
    sentences = cleaned.split('.')
    sentences = [s.strip() for s in sentences if s.strip()]
    if len(sentences) > 2:
        return sentences[0] + '. ' + sentences[-1] + '.'
    return cleaned

if __name__ == '__main__':
    sample = 'Git helps developers track changes. It is fast and reliable. It also supports branching.'
    print(summarize(sample))
