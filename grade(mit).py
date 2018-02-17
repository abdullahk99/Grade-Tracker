""" Lab 2"""
from typing import Union, Any


class GradeEntry:
    """ This is a system to keep track of student grades.

    === Attributes ===
    name - course identifier such as "CSC148"
    weight - course weight, either 1.0 for a half-course or 2.0 for a
    full course
    grade - not meaningful yet
    CATEGORY_TO_POINTS - a mapping of grade categories to a grade point
    """
    name: str
    weight: float
    grade: Union[int, str]

    CATEGORY_TO_POINTS = {0: 0.0, 1: 0.7, 2: 1.0, 3: 1.3, 4: 1.7, 5: 2.0,
                          6: 2.3, 7: 2.7, 8: 3.0, 9: 3.3, 10: 3.7, 11: 4.0,
                          12: 4.0}

    def __init__(self, name: str, grade: Union[int, str], weight: float) -> \
            None:
        """ Initialize a grade entry.

        >>> grade1 = GradeEntry('CSC148', 'A+', 1)
        >>> grade1.name
        'CSC148'
        >>> grade1.weight
        1.0
        >>> grade1.grade
        'A+'
        """
        self.name = name
        self.weight = float(weight)
        self.grade = grade

    def __eq__(self, other: Any) -> bool:
        """ Check if self and other are equivalent.

        #>>> grade1 = GradeEntry('CSC148', 'A+', 1)
        #>>> grade2 = GradeEntry('CSC148', 'A+', 1)
        #>>> grade3 = GradeEntry('CSC148', 'B', 1)
        #>>> grade4 = GradeEntry('CSC148', 88, 1)
        #>>> grade1 == grade2
        True
        #>>> grade1 == grade3
        False
        #>>> grade1 == grade4
        True
        """
        return issubclass(type(self), GradeEntry) and \
            issubclass(type(other), GradeEntry) and self.name == other.name and\
            self.weight == other.weight and self.grade_to_points() == \
            other.grade_to_points()

    def __str__(self) -> str:
        """ Return a string representation of self.
        """
        return f'Weight: {self.weight}, grade: {self.grade}, ' \
               f'points: {self.grade_to_points()}'

    def grade_to_points(self) -> float:
        """ Overridden in the subclasses. """
        raise NotImplementedError('Subclass needed')

    def total(self) -> float:
        """ Compute weight times points of self.

        >>> LetterGradeEntry('CSC148', 'A+', 1).total()
        4.0
        """
        return self.grade_to_points() * self.weight


class NumericGradeEntry(GradeEntry):
    """ A course grade with an integer value.

    === Attributes ===
    name - course identifier such as "CSC148"
    grade - course grade, which has an integer value
    weight - course weight, either 1.0 for a half-course or 2.0 for a
    full course
    _grade_category - represents a category that the grade falls into
    """
    name: str
    grade: int
    weight: float

    def __init__(self, name: str, grade: int, weight: float) -> None:
        """ Initialize a numeric grade entry which extends GradeEntry.

        >>> grade1 = NumericGradeEntry('CSC148', 96, 1)
        >>> grade1.name
        'CSC148'
        >>> grade1.weight
        1.0
        >>> grade1.grade
        96
        >>> grade1._grade_category
        12
        """
        self.name = name
        self.weight = float(weight)
        self.grade = grade

        if 0 <= self.grade <= 49:
            self._grade_category = 0
        elif 50 <= self.grade <= 52:
            self._grade_category = 1
        elif 53 <= self.grade <= 56:
            self._grade_category = 2
        elif 57 <= self.grade <= 59:
            self._grade_category = 3
        elif 60 <= self.grade <= 62:
            self._grade_category = 4
        elif 63 <= self.grade <= 66:
            self._grade_category = 5
        elif 67 <= self.grade <= 69:
            self._grade_category = 6
        elif 70 <= self.grade <= 72:
            self._grade_category = 7
        elif 73 <= self.grade <= 76:
            self._grade_category = 8
        elif 77 <= self.grade <= 79:
            self._grade_category = 9
        elif 80 <= self.grade <= 84:
            self._grade_category = 10
        elif 85 <= self.grade <= 89:
            self._grade_category = 11
        elif 90 <= self.grade <= 100:
            self._grade_category = 12
        else:
            raise ValueError('Enter a grade between 0 and 100.')

    def grade_to_points(self) -> float:
        """ Overrides the corresponding method in GradeEntry. Returns the number
        of points that the grade in self is worth.

        >>> grade1 = NumericGradeEntry('CSC148', 96, 1)
        >>> grade1.grade_to_points()
        4.0
        """
        return self.CATEGORY_TO_POINTS[self._grade_category]


class LetterGradeEntry(GradeEntry):
    """ A course grade with a character value.

    === Attributes ===
    name - course identifier such as "CSC148"
    grade - course grade, which has a letter value like A, B-, C+,...
    weight - course weight, either 1.0 for a half-course or 2.0 for a
    full course
    _grade_category - represents a category that the grade falls into
    """
    name: str
    grade: str
    weight: float

    def __init__(self, name: str, grade: str, weight: float) -> None:
        """ Initialize a letter grade entry which extends GradeEntry.

        >>> grade1 = LetterGradeEntry('CSC148', 'A', 1)
        >>> grade1.name
        'CSC148'
        >>> grade1.weight
        1.0
        >>> grade1.grade
        'A'
        >>> grade1._grade_category
        11
        """
        self.name = name
        self.weight = float(weight)
        self.grade = grade

        if self.grade == 'F':
            self._grade_category = 0
        elif self.grade == 'D-':
            self._grade_category = 1
        elif self.grade == 'D':
            self._grade_category = 2
        elif self.grade == 'D+':
            self._grade_category = 3
        elif self.grade == 'C-':
            self._grade_category = 4
        elif self.grade == 'C':
            self._grade_category = 5
        elif self.grade == 'C+':
            self._grade_category = 6
        elif self.grade == 'B-':
            self._grade_category = 7
        elif self.grade == 'B':
            self._grade_category = 8
        elif self.grade == 'B+':
            self._grade_category = 9
        elif self.grade == 'A-':
            self._grade_category = 10
        elif self.grade == 'A':
            self._grade_category = 11
        elif self.grade == 'A+':
            self._grade_category = 12
        else:
            raise ValueError("Enter a grade between 'A' and 'F' with a "
                             "possible suffix of '+' or '-'.")

    def grade_to_points(self) -> float:
        """ Overrides the corresponding method in GradeEntry. Returns the number
        of points that the grade in self is worth.

        >>> grade1 = LetterGradeEntry('CSC148', 'A', 1)
        >>> grade1.grade_to_points()
        4.0
        """
        return self.CATEGORY_TO_POINTS[self._grade_category]


if __name__ == '__main__':
    from doctest import testmod
    testmod()
    grades = [NumericGradeEntry('csc148', 87, 1.0),
              NumericGradeEntry('mat137', 76, 2.0),
              LetterGradeEntry('his450', 'B+', 1.0)]

    for g in grades:
        print(g)

    total = sum([g.total() for g in grades])
    total_weight = sum([g.weight for g in grades])
    print(f'GPA = {total / total_weight}')
