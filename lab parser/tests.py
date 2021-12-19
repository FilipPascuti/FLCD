from grammar import Grammar
from recursive_descendent import RecursiveDescendent


def test_start():
    grammar = Grammar()
    grammar.read_grammar("g1.txt")
    rec = RecursiveDescendent(grammar, "c")
    productions, state = rec.start()
    assert state == "success"
    assert productions.strip() == "S2"


def test_start_failure():
    grammar = Grammar()
    grammar.read_grammar("g1.txt")
    rec = RecursiveDescendent(grammar, "ca")
    productions, state = rec.start()
    assert state == "error"
    assert productions is None


def test_complex_string():
    grammar = Grammar()
    grammar.read_grammar("g1.txt")
    rec = RecursiveDescendent(grammar, "aacbcbacbc")
    productions, state = rec.start()
    assert state == "success"


def test_expand():
    grammar = Grammar()
    grammar.read_grammar("g1.txt")
    rec = RecursiveDescendent(grammar, "aacbcbacbc")
    rec.expand()
    assert len(rec.input_stack) == 4


test_start()
test_start_failure()
test_complex_string()
test_expand()
print("Tests succeeded")
