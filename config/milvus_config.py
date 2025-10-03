from pydantic import BaseModel, Field


class MilvusConfig(BaseModel):
    """Class where we store default values for milvus database"""
    milvus_host: str = Field(
        default="localhost",
        description="Host where the Milvus db exists"
    )
    milvus_port: int = Field(
        default=19530,
        description="Port for Milvus db"
    )
    milvus_collection: str = Field(
        default="secret_str_examples",
        description="Milvus collection name for storing secret examples"
    )
    use_milvus: bool = Field(
        default=True,
        description="Should we use Milvus for example storage and retrieval?"
    )
    max_examples: int = Field(
        default=5,
        description="Maximum number of similar examples to retrieve"
    )
