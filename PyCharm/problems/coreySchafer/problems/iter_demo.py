# This is a problem from Corey Schafer's video:
# https://www.youtube.com/watch?v=C3Z9lJXI6Qw
# https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Iterators-Coding-Problem


class Sentence:
    def __init__(self, sentence: str):
        """

        :type sentence: str
        """
        self.words = sentence.split(" ")
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        current_index = self.index
        self.index += 1
        return self.words[current_index]


def generator(sentence: str):
    words = sentence.split()
    for word in words:
        yield word


my_sentence = Sentence("This is a test")
# my_sentence = generator("This is a test of willpower")

for word in my_sentence:
    print(word)
