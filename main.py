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

    @when_all(m.subject == PLUMES)
    def r3(m):
        assert_fact("animal", {"subject": OISEAU})

    @when_all(c.f1 << m.subject == VOLE, c.f2 << m.subject == OEUFS)
    def r4(c):
        assert_fact("animal", {"subject": OISEAU})

    @when_all(m.subject == MANGE_VIANDE)
    def r5(c):
        assert_fact("animal", {"subject": CARNIVORE})

    @when_all(
        c.f1 << m.subject == DENTS_POINTUES,
        c.f2 << m.subject == GRIFFES,
        c.f3 << m.subject == YEUX_DEVANT,
    )
    def r6(c):
        assert_fact("animal", {"subject": CARNIVORE})

    @when_all(c.f1 << m.subject == MAMMIFERE, c.f2 << m.subject == SABOTS)
    def r7(c):
        assert_fact("animal", {"subject": ONGULE})

    # regle 8
    @when_all(c.first << m.subject == MAMMIFERE, c.second << m.subject == RUMINE)
    def r8(c):
        assert_fact("animal", {"subject": ONGULE})

    # regle 9
    @when_all(
        c.f1 << m.subject == MAMMIFERE,
        c.f2 << m.subject == CARNIVORE,
        c.f3 << m.subject == BRUNE,
        c.f4 << m.subject == TACHES_SOMBRES,
    )
    def r9(c):
        assert_fact("animal", {"subject": GUEPARD})

    # regle 10
    @when_all(
        c.f1 << m.subject == MAMMIFERE,
        c.f2 << m.subject == CARNIVORE,
        c.f3 << m.subject == BRUNE,
        c.f4 << m.subject == RAIES_NOIRES,
    )
    def r10(c):
        assert_fact("animal", {"subject": TIGRE})

    # regle 11
    @when_all(
        c.f1 << m.subject == ONGULE,
        c.f2 << m.subject == LONG_COU,
        c.f3 << m.subject == LONGUES_PATTES,
        c.f4 << m.subject == TACHES_SOMBRES,
    )
    def r11(c):
        assert_fact("animal", {"subject": GIRAFE})

    # regle 12
    @when_all(c.f1 << m.subject == ONGULE, c.f2 << m.subject == RAIES_NOIRES)
    def r12(c):
        assert_fact("animal", {"subject": ZEBRE})

    # regle 13
    @when_all(
        c.f1 << m.subject == OISEAU,
        none(m.subject == VOLE),
        c.f3 << m.subject == LONG_COU,
        c.f4 << m.subject == LONGUES_PATTES,
        c.f5 << m.subject == NOIR_BLANC,
    )
    def r13(c):
        assert_fact("animal", {"subject": AUTRUCHE})

    # regle 14
    @when_all(
        c.f1 << m.subject == OISEAU,
        none(m.subject == VOLE),
        c.f3 << m.subject == NAGE,
        c.f4 << m.subject == NOIR_BLANC,
    )
    def r14(c):
        assert_fact("animal", {"subject": PINGOUIN})

    # regle 15
    @when_all(c.f1 << m.subject == OISEAU, c.f2 << m.subject == VOLE_BIEN)
    def r15(c):
        assert_fact("animal", {"subject": ALBATROS})


assert_fact("animal", {"subject": POILS})
facts = get_facts("animal")
print(facts)
