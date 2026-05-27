def ft_harvest_total():
    i = 1
    count = 0
    while i < 4:
        harvest = int(input(f"Day {i} harvest: "))
        i += 1
        count += harvest
    print("Total harvest:", count)


"""
if __name__ == '__main__':
        ft_harvest_total()
"""
