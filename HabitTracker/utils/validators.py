def validate_habit_number(number, habits):
    try:
        number = int(number)
    except ValueError:
        return None

    if 1 <= number <= len(habits):
        return number

    return None