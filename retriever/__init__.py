try:
    from pymilvus import (
        connections, Collection, CollectionSchema,
        FieldSchema, DataType, utility
    )
    MILVUS_AVAILABLE = True
except ImportError:
    MILVUS_AVAILABLE = False
    print("Warning: pymilvus is not installed."
          "Vector database features disabled.")

from typing import Dict, Any
from transformer import Transformer


class Retriever:
    def __init__(self, config, transf: Transformer):
        self.config = config
        self.collection = None
        self.transformer = transf

    def setup_milvus(self):
        if not MILVUS_AVAILABLE:
            return

        connections.connect(
            alias="default",
            host=self.config.milvus_host,
            port=self.config.milvus_port
        )

        # Collection schema
        fields = [
            FieldSchema(name="id", dtype=DataType.INT64,
                        is_primary=True, auto_id=True),
            FieldSchema(name="description", dtype=DataType.VARCHAR,
                        max_length=1000),
            FieldSchema(name="secret_str", dtype=DataType.VARCHAR,
                        max_length=200),
            FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR,
                        dim=384)
        ]

        schema = CollectionSchema(
            fields=fields,
            description="Passwords and secrets examples for similarity search"
        )

        # Create or get collection
        collection_name = self.config.milvus_collection
        if utility.has_collection(collection_name):
            self.collection = Collection(collection_name)
            print(f"Using existing Milvus collection: {collection_name}")
        else:
            self.collection = Collection(collection_name, schema)
            print(f"Created new Milvus collection: {collection_name}")

        # Lets create the index now
        try:
            self.collection.load()
        except Exception:
            index_params = {
                "index_type": "IVF_FLAT",
                "metric_type": "L2",
                "params": {"nlist": 128}
            }
            self.collection.create_index("embedding", index_params)
            self.collection.load()

    def store_example(self, description: str,
                      secret_data: Dict[str, Any]) -> bool:
        if not MILVUS_AVAILABLE:
            print("Milvus db was not available, "
                  "so we cannot store the sample.")
            return False
        
        try:
            secret_str = secret_data
            embedding = self.transformer.get_text_embedding(description)

            # Insert data
            entities = [
                [description],
                [secret_str],
                [embedding]
            ]
            self.collection.insert(entities)
            self.collection.flush()

            print("The example was stored in the Milvus database:\n"
                  f"--> {description[:100]}")
            return True
        except Exception as e:
            print(f"An error occurred while trying to store example: {e}")
            return False

