from soscleanai import setup
from pathlib import Path
from retriever import Retriever


class Transformer:
    """Class transformer"""

    def __init__(self, config: setup.TransformerConfig = None,
                 milvus_available: bool = False, retriever: Retriever = None):
        """Initialize our transformer with the configuration"""
        self.config = config or setup.TransformerConfig()
        self._setup_transformer()
        self._milvus_available = milvus_available

        # Create output directory if one doesn't exist yet
        Path(self.config.output_dir).mkdir(parents=True, exist_ok=True)

        # Initialize the database
        self.milvus_available = self._milvus_available and\
            self.config.use_milvus
        self.collection = None
        if self.milvus_available:
            try:
                retriever.setup_milvus()
                print("Connected to Milvus at: "
                      f"{self.config.milvus_host}@{self.config.milvus_port}")
            except Exception as e:
                print(f"Warning: Couldn't connect to Milvus: {e}")
                self.milvus_available = False

    def _setup_transformer(self):
        pass

    def get_text_embedding(self, text: str) -> List[float]:
        """ Function to get embeddings for text"""
        try:
            # Lets try to use nomic-embed-text model for embeddings
            response = self.client.embeddings(
                model="nomic-embed-text",
                prompt=text
            )
            return response['embedding']
        except Exception:
            # Lets create a simple embedding hash-based
            # This should ensure we get 384 dimensions
            import hashlib
            hash_obj = hashlib.sha256(text.encode())
            hash_hex = hash_obj.hexdigest()

            # Now we convert the hash to a 384 dimensional vector
            embedding = []
            # SHAL256 will give us 64 hex chars, each pair gives us one float
            # we need 384 dimensions, so we'll cycle through the hash
            for i in range(384):
                char_index = (i * 2) % len(hash_hex)
                val = int(hash_hex[char_index:char_index+2], 16) / 255.0
                embedding.append(val)

            return embedding
