from durable.lang import *


POILS = "a des poils"
MAMMIFERE = "mammifere"
LAIT = "donne du lait"
PLUMES = "a des plumes"
OISEAU = "oiseau"
VOLE = "vole"
OEUFS = "oeufs"
MANGE_VIANDE = "mange de la viande"
CARNIVORE = "carnivore"
DENTS_POINTUES = "a dents pointues"
GRIFFES = "a des griffes"
YEUX_DEVANT = "yeux devant"
SABOTS = "a sabots"
ONGULE = "ongulé"
RUMINE = "rumine"
BRUNE = "couleur brune"
TACHES_SOMBRES = "taches sombres"
GUEPARD = "guepard"
RAIES_NOIRES = "raies noires"
TIGRE = "tigre"
GIRAFE = "girafe"
ZEBRE = "zebre"
LONG_COU = "long cou"
LONGUES_PATTES = "longues pattes"
NOIR_BLANC = "noir et blanc"
AUTRUCHE = "autruche"
NAGE = "nage"
PINGOUIN = "pingouin"
VOLE_BIEN = "vole bien"
ALBATROS = "albatros"


with ruleset("animal"):

    @when_all(m.subject == POILS)
    def r1(m):
        assert_fact("animal", {"subject": MAMMIFERE})

    @when_all(m.subject == LAIT)
    def r2(m):
        assert_fact("animal", {"subject": MAMMIFERE})


post("animal", {"subject": POILS})
