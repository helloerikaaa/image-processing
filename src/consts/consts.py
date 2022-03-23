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
