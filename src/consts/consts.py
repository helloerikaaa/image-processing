import enum


class EnumConstant(enum.Enum):
    def __str__(self):
        return self.value


class Methods(EnumConstant):
    GRAYSCALE = 'Grayscale'


class Filters(EnumConstant):
    AVG_GRAYSCALE = 'avg_grayscale'
    LUMA_GRAYSCALE = 'luma_grayscale'
    DESATURATE_GRAYSCALE = 'desaturate'
    MAX_DECOMPOSITION = 'max_decomposition'
    MIN_DECOMPOSITION = 'min_decomposition'
    RED_REDUCTION = 'red_reduction'
    GREEN_REDUCTION = 'green_reduction'
    BLUE_REDUCTION = 'blue_reduction'
    GRAY_HISTOGRAM = 'get_histogram'
