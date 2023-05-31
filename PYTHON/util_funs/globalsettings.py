import os
import configparser

class prjSettings():
    def __init__(self):
        pass

the_folders = prjSettings()

the_folders.DIR_ROOT  = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "..") # Project root is defined by globalsettings.py location
# the_folders.DIR_ROOT  = os.path.join(os.getcwd()) 
the_folders.DIR_DATA = os.path.join(the_folders.DIR_ROOT, "data")
the_folders.DIR_DATA_RAW = os.path.join(the_folders.DIR_DATA, "raw")
the_folders.DIR_DATA_CLEAN = os.path.join(the_folders.DIR_DATA, "clean")

the_folders.DIR_PERSIST = os.path.join(the_folders.DIR_DATA, "chroma")

the_files = prjSettings()

the_files.PROBE_CSV = os.path.join(the_folders.DIR_DATA_RAW, "titanic.csv")
the_files.PROBE_PDF = os.path.join(the_folders.DIR_DATA, "77009321.pdf")
the_folders.DIR_PDF_FILES = os.path.join(the_folders.DIR_DATA, "pdf_files")
the_folders.DIR_PDF_CSV_FILES = os.path.join(the_folders.DIR_DATA, "pdf_csv_files")

the_files.CFG_FILE = os.path.join(the_folders.DIR_ROOT, "config.ini")

the_files.BF_TRAIN = os.path.join(the_folders.DIR_DATA_RAW, "black_friday_train.csv")
the_files.BF_TEST  = os.path.join(the_folders.DIR_DATA_RAW, "black_friday_test.csv")

the_files.CSV_FILES = [os.path.join(the_folders.DIR_PDF_CSV_FILES, "tasa_paro_espanya_simplificado.csv"),
                       os.path.join(the_folders.DIR_PDF_CSV_FILES, "tasa_paro_mensual_por_pais_ue.csv")]

## CONSTANTS

the_constants = prjSettings()

the_constants.COLLECTION = "forecasting_ccb"


## CONFIG FILE
prj_cfg = prjSettings()

config = configparser.ConfigParser()

config.read(the_files.CFG_FILE)

prj_cfg.serveraliveinterval = config['DEFAULT']['serveraliveinterval']
prj_cfg.compression         = config['DEFAULT']['compression']
prj_cfg.compressionlevel    = config['DEFAULT']['compressionlevel']
prj_cfg.forwardx11          = config['DEFAULT']['forwardx11']