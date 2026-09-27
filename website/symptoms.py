from random import randint, choice

from .leki_test.wywiad import Wywiad
from .leki_test.pressure import Pressure
from .leki_test.age import Age
from .leki_test.consciousness import Consciousness
from .leki_test.exam import Exam
from .leki_test.ecg import Ecg
from .leki_test.temperature import Temperature
from .leki_test.skin import Skin

drgawki = ['bez drgawek', 'drgawki']


def get_symptoms():
    age = Age()
    consciousness = Consciousness()
    pressure = Pressure()
    temp = Temperature()
    skin = Skin()
    ecg = Ecg()
    return f"{age.age}, {consciousness.consciousness}, {choice(drgawki)}, częstość oddechu: {randint(0, 10)}/10 sek, saturacja {randint(50, 100)}%, częstość tętna {ecg.pulse_rate}/10 sek., {pressure.pressure}, {temp.temperature}, {skin.skin}, {ecg.ekg}."


def get_sample():
    sample = Wywiad()
    return f"{sample.symptoms}."


def get_exam():
    exam = Exam()
    return f"{exam.exam}."


class Symptoms:

    def __init__(self):
        self.symptoms = get_symptoms()