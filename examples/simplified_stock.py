from dataclasses import dataclass, field
from decimal import Decimal

def fetch_pe_ratio(ticker):
    return 25.0

@dataclass(frozen=True)
class Stock:
    ticker: str
    market_cap: str = "UNKNOWN"
    pe_ratio: Decimal = field(default_factory=fetch_pe_ratio)
    eps: Decimal = field(default_factory=lambda: input("provide EPS: "))
    last_3_trades: list[Decimal] = (100, 200, 300)


stock1 = Stock(
    ticker="NVDA",
    market_cap="1.2T",
    eps=Decimal(4.18),
    pe_ratio=Decimal(116.32)
)

stock2 = Stock(
    ticker="NVDA",
    market_cap="1.2T",
    eps=Decimal(4.18),
    pe_ratio=Decimal(116.32)
)

print(stock1 == stock2)
print(hash(stock1))
