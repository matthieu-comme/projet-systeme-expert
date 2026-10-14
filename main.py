from durable.lang import *


class Node:
    def __init__(self, name, node_type="OU", success=False):
        self.name: str = name
        self.node_type: str = node_type
        self.success: bool = success
        self.children: list = []


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
NON = "non"
OU = "ou"
ET = "et"

### CHAINAGE AVANT

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
assert_fact("animal", {"subject": SABOTS})

facts = get_facts("animal")
# print(facts)


### CHAINAGE ARRIERE

# conclusion: [cond1], [cond2, cond3],...
# pour avoir conclusion, il faut cond1 OU (cond2 ET cond3) OU ...
regles = {
    # R1 & R2
    MAMMIFERE: [[POILS], [LAIT]],
    # R3 & R4
    OISEAU: [[PLUMES], [VOLE, OEUFS]],
    # R5 & R6
    CARNIVORE: [[MANGE_VIANDE], [DENTS_POINTUES, GRIFFES, YEUX_DEVANT]],
    # R7 & R8
    ONGULE: [[MAMMIFERE, SABOTS], [MAMMIFERE, RUMINE]],
    # R9
    GUEPARD: [[MAMMIFERE, CARNIVORE, BRUNE, TACHES_SOMBRES]],
    # R10
    TIGRE: [[MAMMIFERE, CARNIVORE, BRUNE, RAIES_NOIRES]],
    # R11
    GIRAFE: [[ONGULE, LONG_COU, LONGUES_PATTES, TACHES_SOMBRES]],
    # R12
    ZEBRE: [[ONGULE, RAIES_NOIRES]],
    # R13
    AUTRUCHE: [[OISEAU, (NON, VOLE), LONG_COU, LONGUES_PATTES, NOIR_BLANC]],
    # R14
    PINGOUIN: [[OISEAU, (NON, VOLE), NAGE, NOIR_BLANC]],
    # R15
    ALBATROS: [[OISEAU, VOLE_BIEN]],
}


def chainage_arriere(faits: set, regles: dict, buts: set, parent_node=None) -> tuple:
    p = list(buts)
    racines = []

    while p:
        f = p.pop()
        f_node = Node(f, OU, (f in faits))
        if parent_node:
            parent_node.children.append(f_node)
        racines.append(f_node)

        if f not in faits:
            s = regles.get(f, [])
            if s:
                for a in s:
                    a_node = Node(name=f"Regle {a}", node_type=ET)
                    f_node.children.append(a_node)

                    valide = True
                    for premisse in a:
                        if premisse not in faits:
                            chainage_arriere(faits, regles, [premisse], a_node)
                            if premisse not in faits:
                                valide = False
                                break
                    if valide:
                        faits.add(f)
                        f_node.success = True
                        a_node.success = True
                        break

    return faits, racines


if __name__ == "__main__":
    base_faits = {POILS, SABOTS, RAIES_NOIRES}
    but = {AUTRUCHE}

    faits_finaux, arbre = chainage_arriere(base_faits, regles, but)
    result = but.issubset(faits_finaux)
    print(f"But {but} atteignable :", result)
    print("Base de faits finale :", faits_finaux)
