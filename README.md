# Bolyai Labs – 3. blokk: Az első modell élesben

Ebben a repóban két feladat van:

| Óra | Feladat | Notebook | CI-feladat |
| --- | --- | --- | --- |
| 1. óra | Feladatkártya #3: Sikeres lesz-e a hívás? | `modell.ipynb` | Feladatkártya 3 |
| 2. óra | Junior rangemelő mérés (egyéni, 40 perc) | `meres_junior.ipynb` | Junior mérés |

## Feladatkártya #3

> Termékfelelősként szeretném tudni előre, melyik MI-hívás fog valószínűleg elbukni, hogy időben átirányíthassuk egy másik modellre.

- [ ] saját repó ebből a sablonból (pl. `modell-13b-07`, Public)
- [ ] a `modell.ipynb` négy TODO-ja (a–d) kitöltve, az önellenőrzés lefut
- [ ] visszamentve Colabból, commitüzenet: `feat: első modellek (feladatkártya #3)`
- [ ] az Actions fülön a **Feladatkártya 3** futás zöld
- [ ] a repó linkje beadva a Teams-feladatba

**Érték:** 5 sprintpont (zöld build 2, határidő 1, commitüzenet 1, kilépőkérdések 1). **Határidő:** az 1. óra vége.

## Junior rangemelő mérés

- Egyéni munka, 40 perc. Használhatod a saját jegyzeteidet és a `modell.ipynb`-t; MI-asszisztenst és mások segítségét nem.
- F1–F4: feladatonként 2 pont, a CI ellenőrzi (az Actions fülön a **Junior mérés** futásban feladatonként látod). F5: 2 pont, a tanár értékeli.
- **A Junior ranghoz legalább 6 pont kell a 10-ből.**
- Beadás: mentés `meres_junior.ipynb` néven, commitüzenet: `meres: Junior rangemelő mérés`, majd a repó linkje a Teams-feladatba.

A „Junior mérés” futás az óra elején piros: ez így van rendjén, amíg a mérést meg nem írod.

## Megnyitás Colabban

[colab.research.google.com](https://colab.research.google.com) → **File → Open notebook → GitHub** fül → felhasználónév → saját repó → a notebook.

## Fogalmak

| Fogalom | Jelentés |
| --- | --- |
| Alapvonal (baseline) | A „mindig a leggyakoribb válasz” pontossága; ezt kell legyőzni |
| Pontosság (accuracy) | A helyes jóslatok aránya |
| Felidézés (recall) | A valóban sikertelen hívások hány százalékát találja meg a modell |
| MAE | Átlagos abszolút hiba, regressziónál; itt ezredmásodpercben |

## Két szabály egész évre

1. API-kulcs és személyes adat soha nem kerül commitba vagy promptba.
2. Az MI által írt kódot is érteni kell. Amit nem tudsz elmagyarázni, azt nem adod be.
