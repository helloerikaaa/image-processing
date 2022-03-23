from tracemalloc import Filter
from src.algorithms.grayscale import avg_grayscale, luma_grayscale, desaturate, max_decomposition, min_decomposition, red_reduction, green_reduction, blue_reduction

from src.consts.consts import Filters

FILTERS = {
    Filters.AVG_GRAYSCALE: avg_grayscale,
    Filters.LUMA_GRAYSCALE: luma_grayscale,
    Filters.DESATURATE_GRAYSCALE: desaturate,
    Filters.MAX_DECOMPOSITION: max_decomposition,
    Filters.MIN_DECOMPOSITION: min_decomposition,
    Filters.RED_REDUCTION: red_reduction,
    Filters.GREEN_REDUCTION: green_reduction,
    Filters.BLUE_REDUCTION: blue_reduction,
}
