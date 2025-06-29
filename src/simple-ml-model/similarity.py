import math

def create_unique_words(sentences_list):
    unique_words = set()
    for sentence in sentences_list:
        for word in sentence.lower().split():
            unique_words.add(word)
    return sorted(unique_words)

def embed(sentence,unique_words):
    words = sentence.lower().split()
    return [words.count(word) for word in unique_words]
        
def cosine_similarity(vec1, vec2):
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    magnitude1 = math.sqrt(sum(a * a for a in vec1))
    magnitude2 = math.sqrt(sum(b * b for b in vec2))
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    return dot_product / (magnitude1 * magnitude2)


if __name__ == "__main__":
    sentence_1 = input("Enter sentence 1: ")
    sentence_2 = input("Enter sentence 2: ")
    unique_words = create_unique_words([sentence_1,sentence_2])
    print(f"unique_words - {unique_words}")

    vec1 = embed(sentence_1, unique_words)
    vec2 = embed(sentence_2, unique_words)

    print(f"vec1 - {vec1}")
    print(f"vec2 = {vec2}")
    similarity_score = cosine_similarity(vec1, vec2)
    print(f"similarity score: {similarity_score:.4f}")



