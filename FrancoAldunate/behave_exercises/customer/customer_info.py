# Module: customer_info

class Customer():
    # Constructor
    def __init__(self):
        self.client_name = {1: 'Franco', 2: 'Raul', 3: 'Daniel', 4: 'Alejandra', 5: 'Daniela'}
        self.client_total_price = {1: 500, 2: 700, 3: 70, 4: 800, 5: 1200}

    # Function: Get client id by client_name
    def get_id_by_client_name(self, client_name):
        for key in self.client_name.keys():
            if self.client_name[key] == client_name:
                return key

    # Function: Check if client is present in clients'list
    def is_client_name_found(self, client_name):
        return client_name in self.client_name.values()

    # Function: Get client_total_price by id
    def get_client_total_price_by_id(self, id):
        for key in self.client_total_price.keys():
            if key == int(id):
                return self.client_total_price[key]
