class Database:
    def __init__(self):
        self.item_data = [
            {
                'id': 11,
                'name': 'Помидорка',
                'description': 'Красная',
                'count': 1
            },
            {
                'id': 69,
                'name': 'Голубика',
                'description': 'Фиолетовая',
                'count': 4
            },
            {
                'id': 98,
                'name': 'Клубника',
                'description': 'Сладкая',
                'count': 6
            }
        ]
        self.basket = {}

    def add_item_basket(self, item_index, user_id):
        data = self.basket.get(user_id, [])
        data.append(item_index)
        self.basket[user_id] = data

    def get_item_basket(self, user_id):
        return self.basket.get(user_id, [])

    def add_item(self, id: int, name: str, description: str, count: int):
        self.item_data.append(
            {
                id: id,
                'name': name,
                'description': description,
                'count': count
            }
        )

    def get_item(self, item_index):
        status = 'Ok'
        if item_index == 0:
            status = 'Small'
        elif item_index == len(self.item_data) - 1:
            status = 'Big'
        return status, self.item_data[item_index]

    # def get_display(self, id: int, name: str, description: str, count: int):

