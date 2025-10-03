from pydantic import BaseModel, Field


class LLMConfig(BaseModel):
    """
    Class where we store default values for the LLM configuration"""
    model: str = Field(
        default="llama3.1:8b",
        description="Ollama model to use"
    )
    host: str = Field(
        default="http://localhost:11434",
        description="Ollama server"
    )
    max_tokens: int = Field(
        default=2000,
        description="Maximum tokens for model response"
    )
    temperature: float = Field(
        default=0.3,
        description="Model temperature (0.0 is deterministic," \
        "1.0 is creative)"
    )
    output_dir : str = Field(
        default="./output",
        description="Path to logs where the obfuscation is recorded"
    )
