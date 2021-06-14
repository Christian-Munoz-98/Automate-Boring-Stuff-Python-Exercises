stuff = {'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}

def displayInventory(inventory):
    print('inventory:\n')
    item_total = 0

    for k,v in inventory.items():
        print(f'{k} - {v}')
        item_total += v
    
    print(f"\nTotal number of items: {str(item_total)}")

displayInventory(stuff)