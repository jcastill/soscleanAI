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
        self.manifest_location = (f"{self.tmpfilename}"
                                  "/sos_reports/manifest.json")
        self.manifest = []
        # We'll have a list containing lists of files 
        # one per defined thread, to go through and obfuscate
        self.distributed_manifest = []

    def extract_archive(self):
        Path(self.tmpfilename).mkdir(exist_ok=True)
        with tarfile.open(self.filename) as arc:
            # TODO: Change the location of the file extracted
            arc.extractall(self.tmpfilename)

    def read_manifest(self):
        with open(self.manifest_location, 'r', encoding='utf-8') as mfile:
            # TODO: The manifest is actually a json, we should probably
            # use native json capabilities
            for line in mfile:
                if "filepath" in line:
                    if line != "null":
                        self.manifest.append(line.split(": ")[1])

    def distribute_files_per_thread(self):
        numfiles = len(self.manifest)
        step = int(numfiles / self.ntreads)
        # Each thread will go from its index to
        # 'step'. So if we have 100 files and 4 threads
        # thread1: 1-25
        # thread2: 26-50
        # thread3: 51-75
        # thread4: 76-100

        for i in range (0, numfiles, step):
            start_range = i
            self.distributed_manifest[i] = self.manifest[start_range:step]

    def execute(self):
        self.extract_archive()
        self.read_manifest()
        self.distribute_files_per_thread()
