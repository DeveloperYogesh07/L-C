from customer import Customer
from deliveryBoy import DeliveryBoy


def main():
    my_customer = Customer("John", "Doe", 5.00)
    delivery_boy = DeliveryBoy()

    payment = 2.00
    delivery_boy.collect_payment(my_customer, payment)

    print(f"Customer's remaining balance: ${my_customer.get_balance():.2f}")


if __name__ == "__main__":
    main()
