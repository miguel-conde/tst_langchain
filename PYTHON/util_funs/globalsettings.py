import os
import configparser

class prjSettings():
    def __init__(self):
        pass

# class folders():
#     def __init__(self):
#         pass

# class files():
#     def __init__(self):
#         pass

# class constants():
#     def __init__(self):
#         pass

the_folders = prjSettings()

the_folders.dir_root  = os.path.abspath(os.path.dirname(__file__)) # Project root is defined by globalsettings.py location
the_folders.DIR_DATA = os.path.join(os.getcwd(), "data")
the_folders.DIR_DATA_RAW = os.path.join(the_folders.DIR_DATA, "raw")
the_folders.DIR_DATA_CLEAN = os.path.join(the_folders.DIR_DATA, "clean")

the_folders.DIR_PERSIST = os.path.join(the_folders.DIR_DATA, "chroma")

the_files = prjSettings()

the_files.PROBE_PDF = os.path.join(the_folders.DIR_DATA, "77009321.pdf")

the_files.cfg_file = os.path.join(the_files.dir_root, "config.ini")

## CONSTANTS

the_constants = prjSettings()

the_constants.COLLECTION = "forecasting_ccb"


## CONFIG FILE
prj_cfg = prjSettings()

config = configparser.ConfigParser()

config.read(the_files.cfg_file)

prj_cfg.serveraliveinterval = config['DEFAULT']['Serveraliveinterval']
prj_cfg.compression         = config['DEFAULT']['Compression']
prj_cfg.compressionlevel    = config['DEFAULT']['Compressionlevel']
prj_cfg.forwardx11          = config['DEFAULT']['Forwardx11']