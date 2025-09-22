try:
    from pymilvus import (
        connections, Collection, CollectionSchema,
        FieldSchema, DataType, utility
    )
    MILVUS_AVAILABLE = True
except ImportError:
    MILVUS_AVAILABLE = False
    print("Warning: pymilvus is not installed"
          "Vector database features will not be used")

class Retriever():

    def __init__(self, database = None):
        self._database = database

    def search_similar(self, text: str) -> List[Tuple[str, Dict[str, Any]]]:
        """
        Search for similar samples in the database.

        Args:
            text: Text to use for search

        Returns:
            List with tuples consisting on (description, data)
        """
        if not self.milvus_available:
            return []
        
        try:
            embedding = self._get_text_embedding(text)
            search_params = {"metric_type: "L2",
                            "params": {"nprobe", 10}
                            }
            results = self.collection.search(
                [embedding],
                "embedding",
                search_params,
                limit=self.config.max_examples,
                output_fields=["description", "data"]
            )

            examples = []
            for hits in results:
                for hit in hits:
                    description = hit.entity.get("description")
                    data_str = hit.entity.get("data")
                    examples.append((description, data_str))
            if examples:
                print(f"We've found {len(examples)}"
                    "similar samples in the database.")
            return examples
        except Exception as e:
            print(f"An error occurred while searching the database: {e}")
            return []
    
