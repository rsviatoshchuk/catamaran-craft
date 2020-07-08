
def get_stability1():
    """
    Отношение конструктивной ширины к длине по ГВЛ
    """
    pass


def is_good_stability1(stability1):
    if 0.33 <= stability1 <= 0.4:
        return True
    else:
        return False


def get_stability2(LOA, maxBeam):
    """
    Отношение наибольшей длины к наибольшей ширине
    """
    return LOA/maxBeam


def is_good_stability2(stability2):
    if 2 < stability2 < 3:
        return True
    else:
        return False


def get_stability3(depth, draft):
    """
    Отношение высоты борта к углублению
    """
    return depth/draft


def get_seaworthiness1(LOA, LWL):
    """
    Отношение наибольшей длины к длине по ГВЛ
    """
    return LOA/LWL


def is_good_seaworthiness1(seaworthiness1):
    if 1.05 < seaworthiness1 < 1.17:
        return True
    else:
        return False


def get_seaworthiness2(LOA, LWL):
    """
    Отношение вертикального клиренса к полной длине катамарана
    """
    return LOA/LWL


def get_seaworthiness3(deck_length, LOA):
    """
    Отношение длины среднего моста к наибольшей длине
    """
    return deck_length / LOA


def get_marine_propulsion1(LWL, hull_BWL):
    """
    Отношение длины корпуса по ГВЛ к ширине корпуса по ГВЛ
    """
    return LWL/hull_BWL


def is_good_marine_propulsion1(marine_propulsion1):
    if 15 < marine_propulsion1:
        return True
    else:
        return False


def get_marine_propulsion2(LWL, hull_BWL):
    """
    Отношение ширины корпуса катамарана по ГВЛ к углублению
    """
    return LWL/hull_BWL


def get_course_steadiness(LWL, hull_BWL):
    """
    Отношение ширины корпуса катамарана по ГВЛ к углублению
    """
    return LWL/hull_BWL


def get_strength1(LWL, depth):
    return LWL/depth


def is_good_strength1(strength):
    if strength < 7.5:
        return True
    else:
        return False


def get_strength2(depth, draft):
    """
    Отношение высоты борта к углублению
    """
    return depth/draft


def get_turning_capacity(LWL, draft):
    """
    Отношение длины по ГВЛ к углублению
    """
    return LWL/draft


def get_floodability(depth, draft):
    """
    Отношение высоты борта к углублению
    """
    return depth/draft
