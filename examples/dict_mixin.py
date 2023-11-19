from decimal import Decimal
from typing import Self

class DictConverterMixin:
    def to_dict(self):
        return self._convert_dict(self.__dict__)

    def _unmangle(self, attr_name):
        if attr_name.startswith("_"):
            return attr_name.split("__", 1)[-1]
        return attr_name


    def _convert_dict(self, attrs):
        dct = {}
        for attr_name, attr in attrs.items():
            unmangled_name = attr_name
            if "__" in attr_name:
                unmangled_name = self._unmangle(attr_name)
            dct[unmangled_name] = self._convert(attr)
        return dct

    def _convert_list(self, attr_list):
        return [self._convert(v) for v in attr_list]

    def _convert(self, attr):
        match attr:
            case DictConverterMixin():
                return attr.to_dict()
            case dict():
                return self._convert_dict(attr)
            case list():
                return self._convert_list(attr)
            case object() if hasattr(attr, '__dict__'):
                return self._convert_dict(attr.__dict__)
            case _:
                return attr 

class Company(DictConverterMixin):
    def __init__(self, company_name: str, ticker: str):
        self.__ticker = ticker.upper()
        self.__name = company_name

    @property
    def ticker(self):
        return self.__ticker

    @property
    def name(self):
        return self.__name


class Stock:
    def __init__(
        self: Self,
        company: Company,
        market_cap: Decimal,
        pe_ratio: float,
        eps: float,
        last_3_trades: list[Decimal]
    ):
        self.__company = company
        self.__market_cap = market_cap
        self.__pe_ratio = pe_ratio
        self.__eps = eps
        self.__last_3_trades = last_3_trades


class GrowthStock(DictConverterMixin, Stock):
    def __init__(
        self: Self,
        company: Company,
        market_cap: float,
        pe_ratio: float,
        eps: float,
        last_3_trades: list[Decimal],
        key_kpi: str
    ):
        self.__key_kpi = key_kpi
        super(DictConverterMixin, self).__init__(company, market_cap, pe_ratio, eps, last_3_trades)

    @property
    def key_kpi(self):
        return self.__key_kpi

snowflake = GrowthStock(
    Company("SNOW", "Snowflake"),
    market_cap=Decimal("5.468e10"),
    pe_ratio=float('NaN'),
    eps=-2.65,
    last_3_trades=[Decimal('165.68'), Decimal('166.02'), Decimal('165.34')],
    key_kpi="global cloud infrastructure spending")

print(snowflake.to_dict())
