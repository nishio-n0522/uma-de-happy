import json
from typing import Literal

from pydantic import BaseModel

class RaceConfig(BaseModel):
    date: str
    stadium: Literal["tokyo" , "kyoto" , "hanshin" , "nakayama" , "chukyo"]
    race_number: int
    race_distance: int
    surface_type: Literal["turf" , "dirt"]
    number_of_starters: int
    bet_selections_csv: str