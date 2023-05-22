import os

class folders():
    def __init__(self):
        pass

class files():
    def __init__(self):
        pass

class constants():
    def __init__(self):
        pass

the_folders = folders()

the_folders.DIR_DATA = os.path.join(os.getcwd(), "data")
the_folders.DIR_DATA_RAW = os.path.join(the_folders.DIR_DATA, "raw")
the_folders.DIR_DATA_CLEAN = os.path.join(the_folders.DIR_DATA, "clean")

the_folders.DIR_PERSIST = os.path.join(the_folders.DIR_DATA, "chroma")

the_files = files()

the_files.PROBE_PDF = os.path.join(the_folders.DIR_DATA, "77009321.pdf")

the_constants = constants()

the_constants.COLLECTION = "forecasting_ccb"