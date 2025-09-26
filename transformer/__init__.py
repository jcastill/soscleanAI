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
