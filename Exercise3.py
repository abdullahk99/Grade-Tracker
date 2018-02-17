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
