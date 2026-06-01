def ft_seed_inventory(name: str, number: int, unit: str) -> None:
    if (unit == "packets"):
        print(f"{name.capitalize()} seeds: {number} {unit} available")
    elif (unit == "grams"):
        print(f"{name.capitalize()} seeds: {number} {unit} total")
    elif (unit == "area"):
        print(f"{name.capitalize()} seeds: covers {number} square meters")
    else:
        print("Unknown unit type")


"""
if __name__  == '__main__':
    ft_seed_inventory("tomato", 15, "packets")
    ft_seed_inventory("carrot", 8, "grams")
    ft_seed_inventory("lettuce", 12, "area")
    ft_seed_inventory("lettuce", 12, "franis")
"""
