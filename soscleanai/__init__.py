
class SosCleanAI():
    """ Main class for the SoS cleaner with AI assistance"""

    def __init__(self, file=None):
        self._file = file

    def sosclean(self):
        """ This function will be used to run the classic sos-clean tool
        on the sos archive"""
        from data import Data
        archive_cleaned = Data(self._file)
        return archive_cleaned

    def review_pending(self, file):
        """ This function takes an already cleaned sos and runs
        our RAG functions on it to see if we forgot something"""
        return file

    def execute(self):
        archive_first_pass = self.sosclean()
        archive_second_pass = self.review_pending(archive_first_pass)
