from decimal import Decimal
from typing import Self

class DictConverterMixin:
    def to_dict(self):
        ...

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
