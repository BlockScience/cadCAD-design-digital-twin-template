from typing import Annotated, TypedDict, Union
from dataclasses import dataclass


Days = Annotated[float, 'days']  # Number of days

class PreyPredatorModelState(TypedDict):
    days_passed: Days
    delta_days: Days

class PreyPredatorModelParams(TypedDict):
    label: str
    timestep_in_days: Days

class PreyPredatorModelSweepParams(TypedDict):
    label: list[str]
    timestep_in_days: list[Days]