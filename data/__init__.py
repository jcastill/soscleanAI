"""
This class will deal with different formats of data
i.e. a sos report, and will uncompress it and review 
the list of files for the cleaner
"""
import tarfile
from pathlib import Path


class Data():
    def __init__(self, filename=None, nthreads=4):
        self.filename = filename
        self.ntreads = nthreads
        self.tmpfilename = "/var/tmp/soscleanAI_dir"

    def extract_archive(self):
        Path(self.tmpfilename).mkdir(exist_ok=True)
        with tarfile.open(self.filename) as arc:
            # TODO: Change the location of the file extracted
            arc.extractall(self.tmpfilename)

    def read_manifest(self):
        pass

    def distribute_files_per_thread(self):
        pass