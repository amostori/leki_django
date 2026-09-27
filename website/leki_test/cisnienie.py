from random import choice

cis_list = ["120/80 mmHg", "70/20 mmHg", "nieoznaczalne", "50/40mmHg", "nieoznaczalne", "nieoznaczalne", "100/80 mmHg", "90/70 mmHg", "80/60 mmHg", "50/20 mmHg", "90/60 mmHg", "100/80 mmHg", "60/20 mmHg"]


class Cisnienie:

    def __init__(self):
        self.cisnienie = f"ciśnienie {choice(cis_list)}"
