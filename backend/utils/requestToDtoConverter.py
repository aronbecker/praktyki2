from typing import TypeVar, Type

T = TypeVar('T')

def convert(data, dtoClass: Type[T]) -> T:
    res = dtoClass()
    for name, _ in vars(dtoClass()).items():
        if name.startswith('__'):
            continue

        val = data.get(name)
        if val:
            setattr(res, name, val)

    return res

    