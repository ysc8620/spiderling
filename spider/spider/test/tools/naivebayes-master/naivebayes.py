"""
Implementation of the Naive Bayes algorithm
"""

from collections import defaultdict
import json
import math
import re

class NaiveBayes(object):
    """The NaiveBayes class implements the naive bayes algorithm"""
    def __init__(self):
        self.classes = defaultdict(lambda: defaultdict(int))
        self.vocabulary = defaultdict(int)
        self.priors = defaultdict(int)

    def train(self, classes):
        """Train the clasifier.

        The classes variable is a dictionary with the key as the class and a list
        of tokenized documents as value for every class."""
        class_document_count = defaultdict(float)

        for klass in classes:
            for document in classes[klass]:
                class_document_count[klass] += 1
                for item in document:
                    self.vocabulary[item] += 1
                    self.classes[klass][item] += 1

        total_documents = float(sum(class_document_count.values()))

        for klass in class_document_count:
            self.priors[klass] = class_document_count[klass] / total_documents

    def scores(self, document):
        """Returns a dictionary with the scores of the document for every class.

        The document variable must be a list with the terms of the document."""

        class_scores = {}

        vocabulary_count = len(self.vocabulary)

        for klass in self.classes:
            score = math.log(self.priors[klass])

            class_word_count = float(sum(self.classes[klass].values()))

            for item in document:
                item_count = self.classes[klass][item]
                score += math.log((item_count + 1.0) / (class_word_count + vocabulary_count))

            class_scores[klass] = score

        return class_scores

    def classify(self, document):
        """Return the class of the document.
        The document must be a list with the terms of the document."""
        scores = self.scores(document)

        sorted_scores = sorted(scores.items(), reverse=True, key=lambda x: x[1])

        predicted_class, predicted_class_score  = sorted_scores[0]

        return predicted_class

    def accuracy(self, test_documents):
        """Return the accuracy of the classifier."""
        predictions = 0

        total_documents = 0
        for klass in test_documents:
            total_documents += len(test_documents[klass])
            
            for document in test_documents[klass]:
                classification = self.classify(document)
                if classification == klass:
                    predictions += 1

        return float(predictions) / float(total_documents)

    def class_accuracy(self, test_documents):
        """Return the class accuracy of the classifier."""
        accuracies = {}

        for klass in test_documents:
            class_documents = len(test_documents[klass])
            predictions = 0
            
            for document in test_documents[klass]:
                classification = self.classify(document)
                if classification == klass:
                    predictions += 1

            accuracies[klass] = float(predictions) / float(class_documents)

        return accuracies

    def save(self, filename):
        """Save the classifier to a file."""
        classifier_data = {"classes": self.classes,
                           "vocabulary": self.vocabulary,
                           "priors": self.priors}

        with open(filename, "w") as f:
            json.dump(classifier_data, f)

    def load(self, filename):
        """Load the classifier from a file."""
        with open(filename, "r") as f:
            classifier_data = json.load(f)

        self.classes = classifier_data['classes']
        self.priors = classifier_data['priors']
        self.vocabulary = classifier_data['vocabulary']

def document_vector(document):
    terms = defaultdict(int)
    
    for term in document:
        terms[term] += 1

    return terms

def tokenize_document(document):
    """Tokenize the contents of a document."""
    tokens = re.findall(r'\w+', document, flags=re.UNICODE)
    
    return tokens
