from src.algorithms.grayscale import avg_grayscale
from src.algorithms.grayscale import luma_grayscale
from src.algorithms.grayscale import desaturate

from src.consts.consts import Filters

FILTERS = {
    Filters.AVG_GRAYSCALE: avg_grayscale,
    Filters.LUMA_GRAYSCALE: luma_grayscale,
    Filters.DESATURATE_GRAYSCALE: desaturate

}
