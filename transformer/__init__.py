from soscleanai import setup


class Transformer:
    """Class transformer"""

    def __init__(self, config: setup.TransformerConfig = None):
        """Initialize our transformer with the configuration"""
        self.config = config or setup.TransformerConfig()
        self._setup_transformer()