from customer import Customer

class DeliveryBoy:
    def collect_payment(self, customer: Customer, payment: float):
        if customer.make_payment(payment):
            print(f"Thanks for the ${payment:.2f}!")
        else:
            print("Come back later and get my money.")
