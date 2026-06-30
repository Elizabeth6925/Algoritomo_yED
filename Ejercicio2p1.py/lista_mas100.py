#Dada una lista de personajes de marvel (usar el archivo adjunto) debe tener 100 o mas

from typing import Any, Optional
 
 
class List(list):
 
    __CRITERION_FUNCTION = {}
 
    def add_criterion(self, criterion_key: str, criterion_function) -> None:
        self.__CRITERION_FUNCTION[criterion_key] = criterion_function
 
    def show(self) -> None:
        for element in self:
            print(element)
 
    def search(self, search_value: Any, criterion: str = None) -> Optional[int]:
        self.sort_by_criterion(key_criterion=criterion)
        search_criterion = self.__CRITERION_FUNCTION.get(criterion)
 
        start = 0
        end = len(self) - 1
        middle = (start + end) // 2
 
        while start <= end:
 
            if search_criterion is None and not isinstance(self[0], (bool, int, float, str)):
                print('no se pudo determinar criterio de busqueda')
                return None
 
            value = search_criterion(self[middle]) if search_criterion else self[middle]
 
            if value == search_value:
                return middle
            elif value < search_value:
                start = middle + 1
            else:
                end = middle - 1
 
            middle = (start + end) // 2
 
    def delete_value(self, value, criterion=None) -> Optional[Any]:
        index = self.search(value, criterion)
        return self.pop(index) if index is not None else None
 
    def sort_by_criterion(self, key_criterion=None) -> None:
        sort_criterion = self.__CRITERION_FUNCTION.get(key_criterion)
 
        if sort_criterion:
            self.sort(key=sort_criterion)
        elif self and isinstance(self[0], (bool, int, float, str)):
            self.sort()
        else:
            print('no se puede ordenar la lista no se como se debe ordenar')
 
    def size(self) -> int:
        return len(self)
 
 
class Heroe:
 
    def __init__(self, name, alias, real_name, short_bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain
 
    def __str__(self):
        return f"{self.name} ({self.real_name}) - {'Villano' if self.is_villain else 'Héroe'}"
 
 
def by_name(item):
    return item.name
 
def by_real_name(item):
    return item.real_name or ""
 
def by_first_appearance(item):
    return item.first_appearance
 