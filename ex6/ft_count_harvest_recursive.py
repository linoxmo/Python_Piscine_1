def ft_count(i: int, last: int):
    if i < last + 1:
        print(f"Day {i}")
        ft_count(i + 1, last)


def ft_count_harvest_recursive():
    i = 0
    ft_count(i, int(input("Days until harvest: ")))
    print("Harvest time!")


"""
if __name__ == '__main__':
    ft_count_harvest_recursive()
"""
