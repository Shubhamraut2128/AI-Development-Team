from typing import TypedDict


class State(TypedDict):
    
    requirement: str

    backend_code : str
    frontend_code : str
    database_schema : str

    testing_reports : str
    review_reports : str
    documentation : str

    
