import re
from typing import Any, Iterable

def filter_query(value: str, data: Iterable[str]) -> Iterable[str]:
    return filter(lambda x: value in x, data)


def unique_query(data: Iterable[str], *args: Any, **kwargs: Any) -> set[str]:
    return set(data)


def limit_query(value: str, data: Iterable[str]) ->list[str]:
    limit: int = int(value)
    return list(data)[:limit]


def map_query(value: str, data: Iterable[str]) -> Iterable[str]:
    col_number: int = int(value)
    return map(lambda x: x.split(' ')[col_number], data)


def sort_query(value: str, data: Iterable[str]):
    reverse = value == 'desc'
    return sorted(data, reverse=reverse)

def regex_query(value: str, data: Iterable[str]):
    pattern: re.Pattern = re.compile(value)
    return filter(lambda x: re.search(pattern, x), data)
