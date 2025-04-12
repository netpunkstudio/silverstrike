from . import dkb, dkb_visa, pc_mastercard, volksbank, chase, bmo

IMPORTERS = [
    chase,
    bmo,
    dkb,
    dkb_visa,
    pc_mastercard,
    volksbank,
]

IMPORTER_NAMES = [
    'Chase',
    'BMO',
    'DKB Giro',
    'DKB Visa',
    'PC MasterCard',
    'Volksbank',
]

try:
    from . import ofx
    IMPORTERS.append(ofx)
    IMPORTER_NAMES.append('OFX Importer')
except ImportError:
    pass
