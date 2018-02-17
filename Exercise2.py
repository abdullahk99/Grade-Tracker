"""
Additional Exercise #1
Class Roster together with subclass RunnerRoster
"""

from typing import Dict, List, Any


class Roster:
    """
    Impiliment a system that keeps track of members and their information.
    A memember should be of the form FirstName, Lastname.
    """
    member_to_info: Dict[str, List[Any]]

    def __init__(self) -> None:
        """
        Initalize a roster.
        """
        self.member_to_info = {}

    def add_member(self, info1: Any, info2: Any, info3: Any, info4: Any) -> \
            None:
        """
        Update roster self by adding member with information info. A member
        should be of the form Fistname, Lastname
        """
        raise NotImplementedError("Subclass needed")

    def remove_member(self, member: str) -> None:
        """
        Update the roster self by removing the member member.
        """
        if member in self.member_to_info:
            del self.member_to_info[member]

    def display_list_members(self) -> List[Any]:
        """
        Return a list of all memmbers

        >>> r1 = Roster()
        >>> r1.add_member('p1', 'blahblah')
        >>> r1.add_member('p2', 'hellohello')
        >>> r1.display_list_members()
        ['p1: blahblah', 'p2: hellohello']

        """
        list_of_member = []

        for people in self.member_to_info:
            string = ''
            string += str(self.member_to_info[people][0]) + ', '
            string += str(self.member_to_info[people][1]) + ', '
            string += str(people)
            list_of_member.append(string)
        return list_of_member


class PatientRoster(Roster):
    """
    Impliment a class to organize patients at a doctor's office.  All attributes
    and Methods are inherited from Roster.
    """

    def __init__(self, limit: int) -> None:
        """
        Initalize a partient roster by extending the initalizer of Roster by
        adding a limit to the difference between number of male and female
        patients
        """
        Roster.__init__(self)
        self.limit = limit
        self.female_patients = 0
        self.male_patients = 0

    def add_member(self, ohip: 'int', first_name: 'str', family_name: 'str',
                    gender: 'str') -> None:
        """
        Add the patient to the doctors office registery with OHIP number ohip,
        first name first_name, family name family_name, and gender gender, if
        and only if by adding the patient of the gender gender does not surpass
        the limit of its gender.

        Precondition: gender can only be M for make or F for female

        >>> doc1 = PatientRoster(2)
        >>> doc1.add_member(1234, 'Abdullah', 'Khokhar', 'M')
        >>> doc1.add_member(1212, 'Emily', 'Buck', 'F')

        >>> doc1.member_to_info
        {1234: ['Abdullah', 'Khokhar', 'M'], 1212: ['Emily', 'Buck', 'F']}

        >>> doc1.display_list_members()
        ['Abdullah, Khokhar, 1234', 'Emily, Buck, 1212']

        """
        if gender == 'M' and self.male_patients < self.limit:
            self.member_to_info[ohip] = [first_name, family_name, gender]
            self.male_patients += 1
        elif gender == 'F' and self.female_patients < self.limit:
            self.member_to_info[ohip] = [first_name, family_name, gender]
            self.female_patients += 1


if __name__ == '__main__':
    from doctest import testmod
    testmod()
