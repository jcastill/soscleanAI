"""
This class will deal with different formats of data
i.e. a sos report, and will uncompress it and review 
the list of files for the cleaner
"""

class Data():
    def __init__(self, filename=None, nthreads=4):
        self.filename = filename
        self.ntreads = nthreads

    def extract_archive(self):
        pass

    def read_manifest(self):
        pass

    def distribute_files_per_thread(self):
        pass