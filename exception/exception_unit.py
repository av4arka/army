class UnitIsDead(Exception):


    def __init__(self, text):
        UnitIsDead.text = text
