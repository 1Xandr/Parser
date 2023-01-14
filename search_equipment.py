# Key-words
check_equip = ["сковород", "кастрюл", "микроволновк", "духовк", "блендер", "грил", "миксер", "мультиварк", "мясорубк"]


def check_equipment(text: str, equipment_list: list) -> list:
    """
    Code search key-words in text and then append to list that we got

    :param text: text of instruction
    :param equipment_list: list where be kept found equipment
    :return: list that came in all_instrument
    """
    split_text = text.lower().split(' ')

    for word in split_text:  # cycle for all word in sentence
        for instrument in check_equip:  # cycle for all word in try_instrument
            if instrument in word:  # if "кастрюл" in "кастрюльку" -> all_instrument.append
                equipment_list.append(instrument)

    return equipment_list


def equipment_for_sql(all_equipment: list) -> list:
    """
    We used a bit system because boolean did not work
    If dish requires equipment "Pan" -> list `equip[0]` = 1 | if not = 0
    :param all_equipment: list that have all equipment that need for cook
    :return: list that have 1 and 0 for SQL | 0 -> Dish does not need this equipment for cook
    """
    equip = [0 for i in range(9)]  # 0 -> Dish does not need this equipment for cook
    for x in range(9):
        equip[x] = 1 if check_equip[x] in all_equipment else 0
    return equip


# Pan, SaucePan, Microwave, Oven, Blender, Grill, Mixer, SlowCooker, Meat Grinder
