from typing import Tuple, List, Dict
from enum import Enum
from datetime import datetime, date, time

def my_function(a: Tuple[int, str, bool], b: List[int], c: Dict[str, Dict[str, Tuple[int, int]]]):
    print(a, b)

def a_new_function(a: int) -> int:
    return a * a


print(a_new_function(1))

EmploymentStatus = Enum('EmploymentStatus', [
                        'unemployed', 'employed', 'let_go'])


person: Dict[str, any] = {
    "name": "Linda",
    "employment_status": EmploymentStatus.employed,
    "born": date(1985, 7, 27)
}
person: Dict[str, any] = {
    "name": "Kalle",
    "employment_status": EmploymentStatus.unemployed,
    "born": date(1988, 4, 23)
}

list_of_employees = [person, person]

print(list_of_employees[0]["born"])