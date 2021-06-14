def addToInventory(inventory,addeditems):
    
    for i in addeditems:
        inventory.setdefault(i,0)
        for k in inventory:
            if i == k:
                inventory[k] +=1
    
    return inventory

def displayInventory(inventory):
    
    print('\nNew inventory:\n')
    
    item_total = 0

    for k,v in inventory.items():
        print(f'{k} - {v}')
        item_total += v
    
    print(f"\nTotal number of items: {str(item_total)}")

inv = {'gold coin':42,'rope':1}

print("\nActual Items:\n")
for k,v in inv.items():
    print(k, '- ',v)

dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby','rope','rope','gun','gun','gun','machete','poison','book','book']
print('\nAdded Items:\n')
for i in dragonLoot:
    print('+1 - '+ i)

inv =addToInventory(inv,dragonLoot)

displayInventory(inv)

