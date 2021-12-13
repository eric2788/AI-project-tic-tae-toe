
from typing import List
from datetime import datetime


class Record:

    def __init__(self, time: datetime, result: str) -> None:
        self.time = time
        self.result = result

    def __repr__(self) -> str:
        return str(self.time)

    def time(self) -> datetime:
        return self.time

histories: List[Record] = []

def add_record(result: str):
    time = datetime.now()
    histories.append(Record(time, result))
    if len(histories) > 10:
        histories.pop(0)

def list_records() -> List[str]:
    lines = []
    histories_list = histories.copy()
    histories_list.reverse()
    for his in histories_list:
        lines.append(f'Time: {his.time.strftime("%m/%d/%Y, %H:%M:%S")}, Result: {his.result}')
    return lines


