
"""
Evaluator class with methods to evaluate coefficients and word lengths.
"""

from typing import List


class Evaluator:
    """
    A class providing static methods for evaluating lists of coefficients and words.
    """

    @staticmethod
    def zip_evaluate(coefs: List[float], words: List[str]) -> float:
        """
        Evaluate the sum of coefficients multiplied by word lengths using zip.

        Args:
            coefs: List of coefficients.
            words: List of words.

        Returns:
            The sum, or -1 if lists have different lengths.
        """
        if len(coefs) != len(words):
            return -1
        return sum(coef * len(word) for coef, word in zip(coefs, words))

    @staticmethod
    def enumerate_evaluate(coefs: List[float], words: List[str]) -> float:
        """
        Evaluate the sum of coefficients multiplied by word lengths using enumerate.

        Args:
            coefs: List of coefficients.
            words: List of words.

        Returns:
            The sum, or -1 if lists have different lengths.
        """
        if len(coefs) != len(words):
            return -1
        return sum(coefs[i] * len(word) for i, word in enumerate(words))


if __name__ == "__main__":
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    print(Evaluator.zip_evaluate(coefs, words))
    print(Evaluator.enumerate_evaluate(coefs, words))