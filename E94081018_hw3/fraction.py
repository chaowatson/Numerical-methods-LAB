# import gcd function
from my_gcd import gcd


# class of fraction of number
class Fraction:
    """
    User-defined ojbect to represent numeric fractions
    The top value, known as the numerator, can be any integer. The bottom value, called the denominator, can be any integer
    greater than 0
    """
    # initialize class
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

        # find the irreducible fraction
        self.simplified_denominator = self.denominator / gcd(abs(self.numerator), abs(self.denominator))
        self.simplified_numerator = self.numerator / gcd(abs(self.numerator), abs(self.denominator))

    # override add function
    def __add__(self, other):
        added_denominator = self.denominator * other.denominator
        added_numerator = (self.denominator * other.numerator) + (self.numerator * other.denominator)
        output_numerator = added_numerator / gcd(added_numerator, added_denominator)
        output_denominator = added_denominator/gcd(added_numerator, added_denominator)
        return f"{int(output_numerator)}/{int(output_denominator)}"

    # override subtract function
    def __sub__(self, other):
        subtracted_denominator = self.denominator * other.denominator
        subtracted_numerator = (self.numerator * other.denominator) - (self.denominator * other.numerator)
        output_numerator = subtracted_numerator / gcd(abs(subtracted_numerator), abs(subtracted_denominator))
        output_denominator = subtracted_denominator / gcd(abs(subtracted_numerator), abs(subtracted_denominator))
        return f"{int(output_numerator)}/{int(output_denominator)}"

    # override multiply function
    def __mul__(self, other):
        multiplied_denominator = self.denominator * other.denominator
        multiplied_numerator = self.numerator * other.numerator
        output_numerator = multiplied_numerator / gcd(abs(multiplied_numerator), abs(multiplied_denominator))
        output_denominator = multiplied_denominator / gcd(abs(multiplied_numerator), abs(multiplied_denominator))
        return f"{int(output_numerator)}/{int(output_denominator)}"

    def __truediv__(self, other):
        divied_denominator = self.denominator * other.numerator
        divied_numerator = self.numerator * other.denominator
        output_numerator = divied_numerator / gcd(abs(divied_numerator), abs(divied_denominator))
        output_denominator = divied_denominator / gcd(abs(divied_numerator), abs(divied_denominator))
        return f"{int(output_numerator)}/{int(output_denominator)}"

    # override equal function
    def __eq__(self, other):
        if self.simplified_numerator == other.simplified_numerator:
            if self.simplified_denominator == other.simplified_denominator:
                return True
            else:
                return False
        else:
            return False

    # override not equal function
    def __ne__(self, other):
        if self.simplified_numerator == other.simplified_numerator:
            if self.simplified_denominator == other.simplified_denominator:
                return False
            else:
                return True
        else:
            return True
