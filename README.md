## 0️⃣Projektstruktur
Skapa ett projekt enligt alla konstens regler, på det sätt vi gått igenom på lektionen.

[![UML-diagram](images/project_setup.png)](images/project_setup.png)

## 1️⃣Diskussion
Skapa en egen uppgift som handlar om att skriva integrationstest. Uppgiften ska träna på det vi gått igenom på lektionen:
integrationstest
markers (gärna spy också)

## 2️⃣Anmälningar
```
pytest -v -m "task2"
```
Skriv enhetstest och integrationstest för klasserna:

Event   
def register_new_member() ← integrationstest  
def sign_up() ← enhetstest

MemberService  
def add_member() ← enhetstest, spionera på denna

Filer:  
enrollments\event.py  
enrollments\member_service.py  

Testfiler:  
unit\test_event.py  
unit\test_member_service.py  
unit\test_event_member_service.py

I conftest.py:  
```
@pytest.fixture
def member_service():
    """
    Creates a MembersService object for testing.
    """
    return MemberService()

@pytest.fixture
def sample_event(member_service):
    """
    Creates an Event object for testing.
    """
    return Event("Bergsklättring", member_service)
```


## 3️⃣Kundvagn

```
pytest -v -m "task3"
```
Gör ett integrationstest som kontrollerar att man inte kan lägga till saker som inte 
finns på lager. Integrationstesta add_inventory_item().

Filer:  
shoppingcart\inventory.py  
shoppingcart\shopping_cart.py  

Testfiler:
unit\test_inventory_shopping_cart.py

``` 
    def add_inventory_item(self, item, amount):
        """
        Add an items to the shopping cart
        :param item: item type to add
        :param amount: amount of items to add
        """

        if item not in self.inventory.inventory_items:
            raise ValueError("Item is not in inventory")

        if item.amount_in_stock < amount:
            raise ValueError("Not enough items in stock")

        cart_item = CartItem(
            item.id,
            item.name,
            item.price,
            amount
        )

        self.items_in_cart.append(cart_item) # adds the selected item as a cart item into cart
        item.amount_in_stock -= amount # remove items from inventory
```

I conftest.py:  
```
@pytest.fixture
def sample_inventory():
    """
    Creates an inventory object for testing.
    """
    return Inventory()
```


## 4️⃣Spårbara transaktioner

## 5️⃣Betalningar

