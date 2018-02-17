"""
CSC 148, Winter 2018
Lab #2
Abdullah Khokhar
"""

from typing import Any


class GradeEntry:
    """
    COMPLETE LATER
    """

    def __init__(self, course: str, weight: float, grade: Any):
        """
        Initalize a Grade Entry for a course with its weight and grade.
        The weight of the course can only be 1.0 for a half-course and 2.0 for
        a full course, and the grade can only be of letter or numerical value.

        >>> g1 = GradeEntry('csc108', 1.0, 'A+')
        >>> g1.course
        'csc108'
        >>> g1.weight
        1.0
        >>> g1.grade
        'A+'
        """
        self.course = course
        self.weight = weight
        self.grade = grade

    def __eq__(self, other: Any) -> bool:

        """
        Return True if grade of course self is equal to grade of course other.

        >>> g1 = LetterGradeEntry('csc108', 1.0, 'A+')
        >>> g2 = LetterGradeEntry('csc108', 1.0, 'A+')
        >>> g3 = NumericGradeEntry('csc236', 1.0, 88)

        >>> g1 == g2
        True
        >>> g1 == g3
        False
        """
        return issubclass(type(self), GradeEntry) and \
            issubclass(type(other), GradeEntry) and \
            self.course == other.course and self.weight\
            == other.weight and self.grade_point() == other.grade_point()

    def __str__(self) -> str:
        """
        Return a string representation of grade entry with numeric grade This
        method overrides the one in GradeEntry.

        >>> g1 = GradeEntry('csc108', 1.0, 81)
        >>> print(g1)
        The grade achieved for csc108 is 81, which has a weight of 1.0
        """
        return 'The grade achieved for {} is {}, which has a weight of ' \
               '{}'.format(self.course, self.grade, self.weight)

    def grade_point(self):
        """
        Return the grade_point associated with the grade achieved in the course.
        """
        raise NotImplementedError("subclass required!")


class NumericGradeEntry(GradeEntry):
    """
    Impliment a numeric grade entry. The course self and weight of self will
    be attributes unchanged from GradeEntry, and course_identifier,
    course_weight, are unchanged methods from GradeEntry.

    The numeric grade associated with its points are:
        value   points
    --------------------
        90-100  4.0
        85-89	4.0
        80-84 	3.7
        77-79 	3.3
        73-76	3.0
        70-72 	2.7
        67-69 	2.3
        63-66	2.0
        60-62 	1.7
        57-59 	1.3
        53-56	1.0
        50-52 	0.7
        0-49 	0.0
    """

    POINTS = {range(0, 50): 0.0, range(50, 53): 0.7,
              range(53, 57): 1.0, range(57, 60): 1.3,
              range(60, 63): 1.7, range(63, 67): 2.0,
              range(67, 70): 2.3, range(70, 73): 2.7,
              range(73, 77): 3.0, range(77, 80): 3.3,
              range(80, 85): 3.7, range(85, 90): 4.0,
              range(90, 101): 4.0}

    def __init__(self, course: str, weight: float, grade: float):
        """
        Initalize a numeric grade entry which extends the initalizer of
        GradeEntry by providing a numeric grade.
        """
        GradeEntry.__init__(self, course, weight, grade)

    def grade_point(self):
        """
        Return the grade_point associated with the grade achieved in the course.
        This method overrides the one in GradeEntry.

        >>> g1 = NumericGradeEntry('csc108', 1.0, 51)
        >>> g1.grade_point()
        0.7
        """
        for points in self.POINTS:
            if self.grade in points:
                return self.POINTS[points]


class LetterGradeEntry(GradeEntry):
    """
    Impliment a letter grade entry. The course self and weight of self will
    be attributes unchanged from GradeEntry, and course_identifier,
    course_weight, are unchanged methods from GradeEntry.

    The letter grade associated with its points are:

    value   grade-point
    -------------------
        A+ 	4.0
        A 	4.0
        A- 	3.7
        B+ 	3.3
        B 	3.0
        B- 	2.7
        C+ 	2.3
        C 	2.0
        C- 	1.7
        D+ 	1.3
        D 	1.0
        D- 	0.7
        F 	0.0
    """
    LET_POINTS = {'F': 0.0, 'D-': 0.7, 'D': 1.0, 'D+': 1.3, 'C-': 1.7,
                  'C': 2.0, 'C+': 2.3, 'B-': 2.7, 'B': 3.0, 'B+': 3.3,
                  'A-': 3.7, 'A': 4.0, 'A+': 4.0}

    def __init__(self, course: str, weight: float, grade: str):
        """
        Initalize a letter grade entry which extends the initalizer of
        GradeEntry by providing a letter grade letter.
        """
        GradeEntry.__init__(self, course, weight, grade)

    def grade_point(self):
        """
        Return the grade_point associated with the grade achieved in the course.
        This method overrides the one in GradeEntry.

        >>> g1 = LetterGradeEntry('csc108', 1.0, 'A-')
        >>> g1.grade_point()
        3.7
        """
        for points in self.LET_POINTS:
            if self.grade in points:
                return self.LET_POINTS[points]


if __name__ == "__main__":
    from doctest import testmod
    testmod()

    grades = [NumericGradeEntry('csc148', 0.5, 87),
              NumericGradeEntry('mat137', 1.0, 76),
              LetterGradeEntry('his450', 0.5, 'B+')]

    for g in grades:
        print("Weight: {}, grade: {}, points: {}".format(g.weight, g.grade, g.
                                                         grade_point()))
    total = sum([g.weight * g.grade_point() for g in grades])
    total_weight = sum([g.weight for g in grades])

    print("GPA = {}".format(total/total_weight))
