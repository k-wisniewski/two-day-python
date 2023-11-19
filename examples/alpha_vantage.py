from pydantic import BaseModel, model_validator, Field, ValidationError
from datetime import date
from decimal import Decimal
from typing import Annotated, Self
import json

class MetaData(BaseModel):
    information: str = Field(alias="1. Information")
    symbol: str = Field(alias="2. Symbol", exclude=True)
    last_refreshed: date = Field(alias="3. Last Refreshed")
    output_size: str = Field(alias="4. Output Size")
    time_zone: str = Field(alias="5. Time Zone")

class OHLCV(BaseModel):
    open: Decimal = Field(alias="1. open")
    high: Decimal = Field(alias="2. high")
    low: Decimal = Field(alias="3. low")
    close: Decimal = Field(alias="4. close")
    volume: int = Field(alias="5. volume")

    @model_validator(mode="after")
    def validate_bounds(self) -> Self:
        if not (self.low <= self.open <= self.high):
            raise ValidationError("value for open field ({self.open}) does not fall within ({self.low}, {self.high}) bounds")
        if not (self.low <= self.close<= self.high):
            raise ValidationError("value for close field ({self.close}) does not fall within ({self.low}, {self.high}) bounds")
        return self


class AlphaVantageResponse(BaseModel):
    meta_data: MetaData = Field(alias="Meta Data")
    time_series: Annotated[dict[date, OHLCV], Field(alias="Time Series (Daily)")]


if __name__ == "__main__":
    with open("example_alpha_vantage_response.json") as f:
        contents = f.read()
        response = AlphaVantageResponse.model_validate_json(contents)
        with open("alpha_vantage_schema.json", "w+") as schema_file:
            schema_file.write(json.dumps(response.model_json_schema(), indent=2))
        print(response.meta_data.symbol)
        print(response.model_dump_json(indent=2, exclude='metadata.symbol'))
