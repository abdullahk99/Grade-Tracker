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

    def add_member(self, member: str, info: Any) -> None:
        """
        Update roster self by adding member with information info. A member
        should be of the form Fistname, Lastname
        """
        self.member_to_info[member] = info

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
            string += people + ': '
            string += str(self.member_to_info[people])
            list_of_member.append(string)
        return list_of_member


class RunnerRoster(Roster):
    """
    Impliment a class for organizing a roster of runners which includes details
    about the runners taking part of the race and organizes them in respect to
    their speed category and e-mail.
    The speed categories are:
        - 1: if speed less than 20
        - 2: if speed less than 30
        - 3: if speed less than 40
        - 4: if speed greater than or equal to 40.

    All attributes and Methods are inherited from Roster.
    """
    

if __name__ == '__main__':
    from doctest import testmod
    testmod()

    race1 = RunnerRoster()
    race1.add_member('abd@hotmail.com', 2)
    race1.add_member('test@hotmail.com', 1)
    race1.add_member('bob@hotmail.com', 2)

    print(race1.display_list_members())
