import pymysql
from config import *


connection = pymysql.connect(
    host=host,
    port=8889,
    user=user,
    password=password,
    database=db_name,
    cursorclass=pymysql.cursors.DictCursor)


def fill_list_of_dishes(id, name, image, description, time, category, cuisine, time_min):
    with connection.cursor() as cursor:
        cursor.execute(f"INSERT INTO `List_of_dishes` (ID, Name, Foto, Description, TimeOfMaking, Category, Cuisine, TimeOfMakingMin) "
                       f"VALUES ({id}, '{name}','{image}', '{description}', '{time}', '{category}', '{cuisine}', {time_min});")
        connection.commit()


def fill_energy_value(id, calories, proteins, fats, carbohydrates):
    with connection.cursor() as cursor:
        cursor.execute(f"INSERT INTO `Energy_value` (ID, Calories, Proteins, Fats, Carbohydrates) "
                       f"VALUES ({id}, {calories}, {proteins}, {fats}, {carbohydrates});")
        connection.commit()


def fill_instruction(id, number, instructionText):
    with connection.cursor() as cursor:
        cursor.execute(f"INSERT INTO `Instruction` (ID, Number, InstructionText) "
                       f"VALUES ({id}, {number}, '{instructionText}');")
        connection.commit()


def fill_equipment(id, pan, saucepan, microwave, oven, blender, grill, mixer, slowCooker, meat_grinder,
                   grater, steamer, mortar, seeder_for_flour, garlic_crusher):
    with connection.cursor() as cursor:
        cursor.execute(f"INSERT INTO `Equipment` (ID, Pan, Saucepan, Microwave, Oven, Blender, Grill, Mixer, SlowCooker,"
                       f" MeatGrinder, Grater, Steamer, Mortar, Seeder_for_flour, Garlic_crusher) "
                       f"VALUES ({id}, {pan}, {saucepan}, {microwave}, {oven}, {blender}, {grill}, {mixer}, {slowCooker},"
                       f"{meat_grinder}, {grater}, {steamer}, {mortar}, {seeder_for_flour}, {garlic_crusher});")
        connection.commit()


def fill_ingredients(id, name: str, quan, unit, default_quant):
    with connection.cursor() as cursor:
        cursor.execute(f"INSERT INTO `Ingredients` (ID, IngredientName, Quantity, unit, Default_quant) "
                       f"VALUES ({id}, '{name}', '{quan}', '{unit}', {default_quant});")
        connection.commit()


def fill_all_ingredients(ingredient_id, name: str, description, image, category):
    with connection.cursor() as cursor:
        cursor.execute(f"INSERT INTO `All_Ingredients` (IngredientID, Name, Description, image, Category) "
                       f"VALUES ({ingredient_id}, '{name}', '{description}', '{image}', '{category}');")
        connection.commit()
