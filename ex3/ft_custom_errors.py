class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)
        self.message = message


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


def check_plant(plant: str, state: bool) -> None:
    if state is True:
        print("Plant is doing fine")
    else:
        raise PlantError(f"The {plant} plant is wilting!")


def check_water(vol: int) -> None:
    if vol > 50:
        print("Tank has enough water")
    else:
        raise WaterError("Not enough water in the tank!")


def testing_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    try:
        check_plant("tomato", False)
    except PlantError as e:
        print(f"Caught {type(e).__name__}:", e)
    print()
    print("Testing WaterError...")
    try:
        check_water(20)
    except WaterError as e:
        print(f"Caught {type(e).__name__}:", e)
    print()
    print("Testing catching all garden errors...")
    try:
        check_plant("tomato", False)
    except GardenError as e:
        print(f"Caught {GardenError.__name__}:", e)
    try:
        check_water(20)
    except GardenError as e:
        print(f"Caught {GardenError.__name__}:", e)


if __name__ == "__main__":
    testing_errors()
