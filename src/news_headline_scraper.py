
import re

POSITIVE_WORDS = {"amazing", "awesome", "good", "great", "fantastic", "enjoyed", "love", "liked", "wonderful", "best"}
NEGATIVE_WORDS = {"awful", "bad", "boring", "terrible", "worst", "hate", "disliked", "poor", "annoying", "disappointing"}

def get_user_input():
    while True:
        review = input("Enter your movie review: ").strip()
        if review:
            return review.lower()
        print("Please enter a non-empty review.")

def extract_words(text):
    words = re.findall(r'\b\w+\b', text)
    return set(words)

def count_sentiment_words(words):
    positive_count = sum(word in POSITIVE_WORDS for word in words)
    negative_count = sum(word in NEGATIVE_WORDS for word in words)
    return positive_count, negative_count

def classify_sentiment(pos_count, neg_count):
    if pos_count == 0 and neg_count == 0:
        return "No sentiment detected"
    if pos_count > neg_count:
        return "Positive"
    elif neg_count > pos_count:
        return "Negative"
    else:
        return "Neutral"

def display_results(pos_count, neg_count, sentiment):
    print(f"\nPositive words: {pos_count}, Negative words: {neg_count}")
    print(f"Overall Sentiment: {sentiment}")

def main():
    review = get_user_input()
    words = extract_words(review)
    pos_count, neg_count = count_sentiment_words(words)
    sentiment = classify_sentiment(pos_count, neg_count)
    display_results(pos_count, neg_count, sentiment)

if __name__ == "__main__":
    main()
