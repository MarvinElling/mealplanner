# %%
food_100 = {
    'apfel': 50,
    'banane' : 100,
    'berglinsen' : 350,
    'kartoffel': 70,
    'nuss_haselnuss': 628,
    'obstriegel': 96,
    'reis' : 350,
    'schokolade_90': 605,
    'seelachs'
    'speisequark' : 139,

    'milch': 64,

    'paprika':0,
    'tomate':0,
    'weintrauben':0,
}


class dish:
    """Essen."""

    def __init__(self, name: str,
                 ingredients: None | list[tuple[str, float | int]]) -> None:
        """Init of dish.

        Args:
            name (str): Name of dish
            ingredidients (list[tuple[str, float | int]]): Ingreditients in gramm
        """
        self.name = name
        self.ingre = ingredients
        self.calories = self.calc_calories()
        print(f'{self.name} with {self.calories} successfully initiated')
    def calc_calories(self) -> float:
        """Calculates calories.

        Returns:
            float: calories
        """
        calories = 0
        for ing in self.ingre:
            calories += food_100[ing[0]] * ing[1] / 100
        return calories

    def __str__(self) -> str:
        """Return dish name.
        """
        return f'{self.name}'
