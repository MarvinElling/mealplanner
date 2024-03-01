# %%
from mealplanner.src.food_database import *

apfel = Dish('Apfel',
             [('apfel', 100)])

banane = Dish('Banane',
              [('banane', 100)])

brot = Dish('Brot',
            [('brot', 100),
             ('margarine_rama', 10),
             ])


obstriegel = Dish('Obstriegel',
                  [('obstriegel', 100),
                   ])

quark_musli= Dish('Quark-Musli',
                  [('musli_basis5_kornmix', 50),
                   ('speisequark40', 250),
                   ('marmelade_erdbeer', 10)])


quinoa_bowl = Dish('Apfel-Quinoa-Mandel-Bowl',
                   [('apfel', 100),
                    ('quinoa', 75),
                    ('mandeln', 25),
                    ('tellerlinsen', 25),
                    ],
                    'https://www.ndr.de/ratgeber/kochen/rezepte/Apfel-Quinoa-Mandel-Bowl,rezept2892.html')

reis1 = Dish('Reis1',
             [('reis', 150),
              ('hirtenkase', 100)])

schoko = Dish('Schoko',
              [('schokolade_90', 25)])

shake1 = Dish('Shake1',
              [('haferdrink_gutbio', 300),
               ('banane', 100),
               ('nuss_hasel', 50),
               ('honig', 7.5),
               ('haferflocken', 20)],
            )

spagh_carb = Dish('Spaghetti Carbonara',
                  [('spaghetti', 150),
                   ('margarine_rama', 25),
                   ('parmesan', 25)])




