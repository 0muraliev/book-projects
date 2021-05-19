stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def add_to_inventory(inventory, loot):
    for i in loot:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1

    return inventory


print(add_to_inventory(stuff, dragon_loot))
