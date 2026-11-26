"""Feladatkártya #3: a CI lefuttatja a modell.ipynb-t, és ellenőrzi az eredményeket."""
import pytest
from kozos import futtat


@pytest.fixture(scope="module")
def e():
    eredmeny, hiba = futtat("modell.ipynb", "kartya3.json")
    if hiba:
        pytest.fail(hiba, pytrace=False)
    return eredmeny


def test_alapvonal(e):
    assert e["baseline"] == pytest.approx(0.712, abs=0.001)


def test_logisztikus_regresszio(e):
    assert e["accuracy"] == pytest.approx(0.828, abs=0.001), "Ellenőrizd a felosztást (a) és a pipeline-t (b)."


def test_felidezes(e):
    assert e["recall_hiba"] == pytest.approx(0.6667, abs=0.001), "A felidézés a sikertelen osztályra: pos_label=0."


def test_regresszio(e):
    assert e["mae"] < 60
