import pymysql
from config import *


connection = pymysql.connect(
    host=host,
    port=8889,
    user=user,
    password=password,
    database=db_name,
    cursorclass=pymysql.cursors.DictCursor)


def fill_list_of_dishes(id, name, image, description, time, category, cuisine):
    with connection.cursor() as cursor:
        cursor.execute(f"INSERT INTO `List_of_dishes` (ID, Name, Foto, Description, TimeOfMaking, Cuisine, Category) "
                       f"VALUES ({id}, '{name}','{image}', '{description}', '{time}', '{cuisine}', '{category}');")
        connection.commit()


def fill_energy_value(id, calories, proteins, fats, carbohydrates):
    with connection.cursor() as cursor:
        cursor.execute(f"INSERT INTO `Energy_value` (ID, Calories, Proteins, Fats, Carbohydrates) "
                       f"VALUES ({id}, {calories}, {proteins}, {fats}, {carbohydrates});")
        connection.commit()


def fill_instruction(id, number, instructionText, image):
    with connection.cursor() as cursor:
        cursor.execute(f"INSERT INTO `Instruction` (ID, Number, InstructionText, InstructionFoto) "
                       f"VALUES ({id}, {number}, '{instructionText}','{image}');")
        connection.commit()


def fill_equipment(id, pan, saucepan, microwave, oven, blender, grill, mixer, slowCooker, meat_grinder):
    with connection.cursor() as cursor:
        cursor.execute(f"INSERT INTO `Equipment` (ID, Pan, Saucepan, Microwave, Oven, Blender, Grill, Mixer, SlowCooker,MeatGrinder) "
                       f"VALUES ({id}, {pan}, {saucepan}, {microwave}, {oven}, {blender}, {grill}, {mixer}, {slowCooker}, {meat_grinder});")
        connection.commit()


def fill_ingredients(id, name: str, quan, unit, default_quant):
    with connection.cursor() as cursor:
        cursor.execute(f"INSERT INTO `Ingredients` (ID, IngredientName, Quantity, unit, Default_quant) "
                       f"VALUES ({id}, '{name}', '{quan}', '{unit}', {default_quant});")
        connection.commit()
