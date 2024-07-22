import pandas as pd
from dataclasses import dataclass

@dataclass
class PplRunResult:
    workflow:str
    result:pd.Dataframe | None
    errors:list[BaseException] | None