# nTrophy Project - Tvoření Map
___
## 1. adjust_xlsx
V této složce naleznete upravené 'části' map. Každá mapa má vybarvené buňky obsahující hodnotu 1.

## 2. origin_xlsx
V této složce naleznete 'části' map, tak jak jsme je stáhli. Jsou pouze uložené jako Excelové soubory, 
nikoli jako soubory .csv.

## 3. main.xlsx
Tento soubor je shodný se souborem *vysledna_mapa.xlsx*, ale oproti němu obsahuje ve svých buňkách čísla.

## 4. vysledna_mapa.xlsx
Tento soubor je naší výslednou mapou.

## 5. Table.py
Tento soubor obsahuje kód, který jsme použili pro sestavování naší mapy. Chcete-li se o jeho fungování dozvědět více, 
podívejte se přímo do něj. Zde je rychlý přehled:

### `class Table`
Tato třída vytváří instance tabulky, které později slouží jako výsledné mapy.

>`workbook` slouží k uchování `<class 'openpyxl.workbook.workbook.Workbook'>`.

>`sheet` slouží k uchování `<class 'openpyxl.worksheet.worksheet.Worksheet'>`.

>`workbook_name` slouží k uchování jména dané tabulky.

#### `def __init__`
> Tato metoda se volá při vytváření nové instance.

Jediním parametrem metody je `woorkbook_name: str`, který slouží jako jméno pro novou tabulku.

#### `def convertCsvToExcel`
> Metoda je `@staticmethod`, míní, že metodu lze volat jak přes instanci třídy, tak i přes samotnou třídu.

Tato metoda má za úkol konvertovat .csv soubory do .xlsx soubory. My jsme ji nakonec nevyužili, 
protože nebyla potřeba.

#### `def colorTable`
> Metoda je `@staticmethod`, míní, že metodu lze volat jak přes instanci třídy, tak i přes samotnou třídu.

Tato metoda zvýrazňuje všechny buňky, které mají hodnotu 1.
Prvním parametrem metody je `workbook_name: str`, který slouží jako jméno tabulky. Druhým je `color: str`, který definuje barvu, 
jakou se budou buňky vybarvovat.

#### `def adjustCells`
> Metoda je `@staticmethod`, míní, že metodu lze volat jak přes instanci třídy, tak i přes samotnou třídu.

Tato metoda přizpůsobuje výšku a šířku jednotlivých buněk. 
Původní nastavení excelu, kdy výška jedné buňky je *29 pixelů* a šířka *96 pixelů* není vhodná k použití, protože 
zkresluje měřítko. Doporučujeme nastavit parametry `height: int` a `width: int` na stejnou hodnotu.
Dalším parametrem metody je `workbook_name: str`, který slouží jako jméno tabulky.

#### `def fillZeros`
Tato metoda se využije při "resetu" tabulky. Vyplní všechny buňky hodnotou 0.

#### `def resetColorAndBorders`
Tato metoda se také využije převážně při "resetu" tabulky. Změní všechny barvy a všechno ohraničení na původní hodnotu.

#### `def resetColor`
Tato metoda je zjednodušenou metodou `resetColorAndBorders`. Resetuje pouze barvu. Přidali jsme ji tuto "odnož", 
protože časová komplexicita všech funkcích je velká - O(n^2).

#### `def resetBorders`
Tato metoda je zjednodušenou metodou `resetColorAndBorders`. Resetuje pouze ohraničení. Přidali jsme ji tuto "odnož", 
protože časová komplexicita všech funkcích je velká - O(n^2).

#### `def copyValues`
> Metoda je `@staticmethod`, míní, že metodu lze volat jak přes instanci třídy, tak i přes samotnou třídu.

Asi nejdůležitější metoda celého programu. Kopíruje hodnoty z jedné excelové tabulky do druhé. Narazíli při průchodu 
tabulky `workbook_from: str`, ze které data kopírujeme, na hodnotu buňky 1, překopíruje danou buňku **s danou barvou** 
a s danou hodnotou do tabulky `workbook_to: str`.

#### `def deleteValues`
> Tuto metodu je důležité používat **velice obezřetně!!!**

Vymaže všechny hodnoty v buňkách. Použití je pro vytvoření definitivní mapy, která už se dál upravovat nebude. Tím, že 
se vymažou hodnoty v tabulce, vypadá mapa v excelu graficky lépe, ale už nebude možno jí předat další část mapy, protože 
na to program potřebuje znát hodnoty buněk.

## Další otázky?
Koukněte dovnitř souboru. Kontaktujte mě.