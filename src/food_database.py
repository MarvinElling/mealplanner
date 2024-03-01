# %%
from __future__ import annotations

food_100 = {
    'apfel': 50,

    'banane' : 100,
    'berglinsen' : 350,
    'brot' : 120,

    'ei': 80,

    'haferflocken': 360,
    'hirtenkase': 250,
    'honig': 300,

    'kartoffel': 70,
    'kase_tilsiter': 120,

    'lachs_raucher': 200,

    'mandeln': 576,
    'margarine_rama': 530,
    'marmelade_erdbeer': 150,
    'musli_basis5_kornmix': 361,
    'musli_lidl': 400,

    'nuss_hasel': 628,

    'obstriegel': 96,

    'parmesan': 250,

    'quinoa': 366,

    'reis' : 350,
    'reiswaffel_piece': 25,

    'sahnejoghurt_milsani': 150,
    'schokolade_90': 605,
    'spaghetti': 350,
    'speisequark40' : 139,

    'tellerlinsen': 300,
    'toast': 90,

    'milch': 64,
    'haferdrink_gutbio' : 42,

    'paprika':0,
    'tomate':0,
    'weintrauben':0,
}


class Dish:
    """Essen."""

    def __init__(self, name: str,
                 ingredients: None | list[tuple[str, float | int]],
                 link: None | str = None) -> None:
        """Init of dish.

        Args:
            name (str): Name of dish
            ingredidients (list[tuple[str, float | int]]): Ingreditients in gramm
        """
        self.name = name
        self.link = link
        if ingredients is not None:
            self.ingre = ingredients
            self.calories = self.calc_calories()
            print(f'{self.name} with {self.calories} successfully initiated')
        else:
            self.calories = 0
            print(f'{self.name} successfully initiated')

    def calc_calories(self) -> float:
        """Calculates calories.

        Returns:
            float: calories
        """
        calories = 0.0
        for ing in self.ingre:
            calories += food_100[ing[0]] * ing[1] / 100
        return calories

    def __str__(self) -> str:
        """Return dish name.
        """
        return f'{self.name}'

    def __add__(self, other: float | int) -> float:
        """Calculate self + other."""
        if isinstance(other, (float, int)):
            return other + self.calories

    def __radd__(self, other: float | int) -> float:
        """Calculate other + self."""
        if isinstance(other, (float, int)):
            return other + self.calories        
