from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int
    

# basemodel alrerady provides __init__ and validation logic, so we don't need to define it ourselves.
# Note: avoid overriding BaseModel.__init__ with a positional signature.
# Pydantic handles initialization and validation. Use validators or call
# super().__init__(**data) if you need custom behavior.

