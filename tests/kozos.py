import json
import re
from pathlib import Path

import nbformat
import pandas as pd
import pytest
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError
from sklearn.metrics import accuracy_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

ROOT = Path(__file__).resolve().parent.parent


def futtat(nev, eredmeny):
    """Lefuttatja a notebookot, és beolvassa a mentett eredményfájlt. Ha a notebook hibával áll le, None-t ad vissza a hibaüzenettel."""
    path = ROOT / nev
    if not path.exists():
        return None, f"Hiányzik a {nev} (Colabból ugyanezen a néven mentsd vissza)."
    nb = nbformat.read(path, as_version=4)
    try:
        NotebookClient(nb, timeout=300, kernel_name="python3", resources={"metadata": {"path": str(ROOT)}}).execute()
    except CellExecutionError as e:
        return None, "A notebook hibával állt le: " + re.sub(r"\x1b\[[0-9;]*m", "", str(e)).strip().splitlines()[-1]
    return json.load(open(ROOT / "eredmenyek" / eredmeny)), None


def adat():
    df = pd.read_csv(ROOT / "data" / "hivasok_november.csv")
    df["modell_nagyobb"] = (df["modell"] == "nagyobb").astype(int)
    return df, df[["tokenek", "valaszido_ms", "modell_nagyobb"]], df["sikeres"]
