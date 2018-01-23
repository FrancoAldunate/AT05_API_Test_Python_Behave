# Module: main
from FrancoAldunate.online_shopping_page.pickup_items import PickupItems
from FrancoAldunate.online_shopping_page.purchase_items import PurchaseItem
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
handler = logging.FileHandler('Test_Log.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class ShoppingPage():
    # Class constructor
    def __init__(self):
        self.items_selected = []
        self.items_purchased = {}
        self.pickupItems = PickupItems()
        self.purchaseItem = PurchaseItem()

    # Function: Shop items
    def shop(self):
        logger.info("Starting execution...")
        logger.info("Items' stock: %s", self.purchaseItem.get_items())
        flag = True
        while flag:
            response = input("Select item? Yes:y, No:no: ")
            if response.lower() == "y":
                logger.info("Selecting item...")
                print(f"Items: {self.purchaseItem.get_items().keys()}")
                item = input("Item?: ")
                if item in self.purchaseItem.get_items():
                    logger.debug("Item %s selected", item)
                    quantity = int(input("Quantity?: "))
                    if quantity <= self.purchaseItem.get_items()[item]:
                        logger.debug("Item quantity selected %s", quantity)
                        item_info = self.pickupItems.pickup_item(item, quantity)
                        self.items_selected.append(item_info[0])
                        purchase_response = input(f"Purchase Item  {item_info[0]}?: ")
                        if purchase_response.lower() == "y":
                            logger.debug("Item: %s purchased with price: %s", item_info[0], item_info[1])
                            total_price = self.purchaseItem.purchase_item(item_info[0], item_info[1])
                            self.items_purchased[item_info[0]] = total_price
                    else:
                        print("Not enough units in stock")
                else:
                    print("Item not in stock")
            elif response.lower() == "n":
                flag = False
                print(f"Items selected: {self.items_selected}")
                print(f"Items purchased: {self.items_purchased}")
                print(f"Items' stock: {self.purchaseItem.get_items()}")
                logger.debug("Items' stock: %s", self.purchaseItem.get_items())


# Execution
shoppingPage = ShoppingPage()
shoppingPage.shop()
