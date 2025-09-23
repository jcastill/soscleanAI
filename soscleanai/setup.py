from pydantic import BaseModel, Field


class TransformerConfig(BaseModel):
    """Configuration for the tranformer part of the project"""

    model: str = Field(
        default="llama3.1:8b",
        description="Model to use"
    )
    host: str = Field(
        default="http://localhost:11434",
        description="Transformer host"
    )
    max_tokens: int = Field(
        default=2000,
        description="Max tokens for the model response"
    )
