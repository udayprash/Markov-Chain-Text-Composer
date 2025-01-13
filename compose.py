import string
from graph import Graph, Vertex
import random


# steps to take:
def get_words(path):
    f = open(path, 'r')
    text = f.read()

    # turns whitespace to just spaces
    text = ' '.join(text.split())
    text = text.lower()

    # remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()    # split on spaces
    return words


def make_graph(words):
    graph = Graph()

    previous_word = None

    # for each word, check that word is in graph
    for word in words:
        # if not, add it
        word_vertex = graph.get_vertex(word)

        if previous_word:
            previous_word.increment_edge(word_vertex)

        previous_word = word_vertex

    graph.generate_probability_mappings()

    return graph


def compose(graph, words, length=50):
    composition = []
    word = graph.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.value)
        word = graph.get_next_word(word)

    return composition


def main():
    # 1. get words from text
    words = get_words('texts/hp_sorcerer_stone.txt')

    # 2. make a graph using words
    graph = make_graph(words)
    # 3. get the next word for x number of words (defined by user)
    # 4. show the user
    composition = compose(graph, words, 100)
    return ' '.join(composition)    # returns a string, where words are separated by a space


if __name__ == "__main__":
    print(main())

