"""Junior rangemelő mérés: feladatonként egy teszt (F1–F4), mindegyik 2 pont."""
import pytest
from kozos import adat, futtat, train_test_split, DecisionTreeClassifier, accuracy_score, recall_score


@pytest.fixture(scope="module")
def e():
    eredmeny, hiba = futtat("meres_junior.ipynb", "meres.json")
    if hiba:
        pytest.fail(hiba, pytrace=False)
    return eredmeny


@pytest.fixture(scope="module")
def felosztas():
    _, X, y = adat()
    return train_test_split(X, y, test_size=0.3, random_state=7, stratify=y)


def test_F1_felosztas(e):
    assert e["f1_teszt_meret"] == 300, "A teszthalmaz 30% legyen."
    assert e["f1_baseline"] == pytest.approx(0.71, abs=0.001), "random_state=7 és stratify=y kell."


def test_F2_dontesi_fa(e, felosztas):
    X_train, X_test, y_train, y_test = felosztas
    p = DecisionTreeClassifier(max_depth=4, random_state=0).fit(X_train, y_train).predict(X_test)
    assert e["f2_accuracy"] == pytest.approx(accuracy_score(y_test, p), abs=1e-6)
    assert e["f2_recall_hiba"] == pytest.approx(recall_score(y_test, p, pos_label=0), abs=1e-6)


def test_F3_elkapja_a_hibakat(e):
    assert e["f3_recall_hiba"] >= 0.80, f"A felidézés {e['f3_recall_hiba']:.3f}, legalább 0,80 kell."
    assert e["f3_accuracy"] >= 0.72, f"A pontosság {e['f3_accuracy']:.3f}, legalább 0,72 kell."


def test_F4_regresszio(e):
    assert e["f4_mae"] < 60, f"A MAE {e['f4_mae']:.1f} ms, 60 alatt kell."
