"""
A tiny statistics module for computing mean, median, quartiles, variance, and standard deviation.
"""

from typing import List, Optional, Union


class TinyStatistician:
    """
    A simple statistics calculator.
    """

    @staticmethod
    def mean(x: List[Union[int, float]]) -> Optional[float]:
        """
        Calculate the mean of a list.

        Args:
            x: List of numbers.

        Returns:
            The mean, or None if list is invalid.
        """
        if not isinstance(x, list) or len(x) == 0:
            return None
        return sum(x) / len(x)

    @staticmethod
    def median(x: List[Union[int, float]]) -> Optional[float]:
        """
        Calculate the median of a list.

        Args:
            x: List of numbers.

        Returns:
            The median, or None if list is invalid.
        """
        if not isinstance(x, list) or len(x) == 0:
            return None

        sorted_x = sorted(x)
        n = len(sorted_x)

        if n % 2 == 0:
            return (sorted_x[n // 2 - 1] + sorted_x[n // 2]) / 2
        else:
            return float(sorted_x[n // 2])

    @staticmethod
    def quartile(x: List[Union[int, float]]) -> Optional[List[float]]:
        """
        Calculate the quartiles (25th and 75th percentiles) of a list.

        Args:
            x: List of numbers.

        Returns:
            List [Q1, Q3], or None if list is invalid.
        """
        if not isinstance(x, list) or len(x) == 0:
            return None

        sorted_x = sorted(x)
        n = len(sorted_x)

        q1 = TinyStatistician.median(sorted_x[:n // 2])
        q3 = TinyStatistician.median(sorted_x[(n + 1) // 2:])

        return [q1, q3]

    @staticmethod
    def var(x: List[Union[int, float]]) -> Optional[float]:
        """
        Calculate the variance of a list.

        Args:
            x: List of numbers.

        Returns:
            The variance, or None if list is invalid.
        """
        if not isinstance(x, list) or len(x) == 0:
            return None

        m = TinyStatistician.mean(x)
        if m is None:
            return None

        return sum((val - m) ** 2 for val in x) / len(x)

    @staticmethod
    def std(x: List[Union[int, float]]) -> Optional[float]:
        """
        Calculate the standard deviation of a list.

        Args:
            x: List of numbers.

        Returns:
            The standard deviation, or None if list is invalid.
        """
        var = TinyStatistician.var(x)
        if var is None:
            return None
        return var ** 0.5


if __name__ == "__main__":
    tstat = TinyStatistician()
    a = [1, 42, 300, 10, 59]
    print(tstat.mean(a))
    # Expected: 82.4
    print(tstat.median(a))
    # Expected: 42.0
    print(tstat.quartile(a))
    # Expected: [10.0, 59.0]
    print(tstat.var(a))
    # Expected: 12279.439999999999
    print(tstat.std(a))
    # Expected: 110.81263465868862