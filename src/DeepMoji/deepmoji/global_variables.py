""" Global variables.
"""
import json
import tempfile
from os.path import abspath, dirname, join

# The ordering of these special tokens matter
# blank tokens can be used for new purposes
# Tokenizer should be updated if special token prefix is changed
SPECIAL_PREFIX = 'CUSTOM_'
SPECIAL_TOKENS = ['CUSTOM_MASK',
                  'CUSTOM_UNKNOWN',
                  'CUSTOM_AT',
                  'CUSTOM_URL',
                  'CUSTOM_NUMBER',
                  'CUSTOM_BREAK']
SPECIAL_TOKENS.extend(['{}BLANK_{}'.format(SPECIAL_PREFIX, i) for i in range(6, 10)])

ROOT_PATH = dirname(dirname(abspath(__file__)))
VOCAB_PATH = join(ROOT_PATH, "model", "vocabulary.json")


def get_vocabulary():
    """Load the default vocabulary for DeepMoji"""
    with open(VOCAB_PATH, 'r') as f:
        return json.load(f)


PRETRAINED_PATH = join(ROOT_PATH, "model", "deepmoji_weights.hdf5")

WEIGHTS_DIR = 'D:/Data_Science_all/MSC_2_anno/Tesi_Irony_Sarcasm/Code/DeepMoji/model/weights' #tempfile.mkdtemp()

NB_TOKENS = 50000
NB_EMOJI_CLASSES = 64
FINETUNING_METHODS = ['last', 'full', 'new', 'chain-thaw']
FINETUNING_METRICS = ['acc', 'weighted']