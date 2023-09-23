from abc import ABC, absctractmethod
import typing as tp

class Rates(ABC):

    def __init__(self, currencies: tuple[str]):
        self.currencies = currencies
        self.dict_val = dict.fromvalues(currencies, 0)
        self.sum = 0

    @absctractmethod
    def get_sum(self):
        self.sum = sum(self.dict_val.values())
        return self.sum

    @absctractmethod
    def amount(self):
        res = ''
        for cur, val in self.dict_val.items():
            res += f'{cur}: {val}\n'
        return res

    @absctractmethod
    def set_vals(self, vals: dict[str: int]):
        for key, value in vals.items():
            self.dict_val[key] = value

    @absctractmethod
    def modify(self, vals: dict[str: int]):
        for key, value in vals.items():
            self.dict_val[key] =  dict_val.get(key, 0) + value

    @absctractmethod
    def get_value(self, cur):
        return self.dict_val[cur]
