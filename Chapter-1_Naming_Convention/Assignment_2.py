import sys

# Dictionary mapping country codes to adjacent countries
ADJACENT_COUNTRIES = {
    "CA": ["United States"],
    "FR": ["Belgium", "Germany", "Italy", "Spain", "Switzerland"],
    "CN": ["India", "Mongolia", "Russia", "Vietnam", "Laos"],
    "IN": ["Pakistan", "China", "Nepal", "Bhutan", "Bangladesh", "Myanmar"],
    "US": ["Canada", "Mexico"],
    "NZ": ["No adjacent countries (island nation)"],
}


def get_adjacent_countries(country_code):
    """
    Returns the list of adjacent countries for a given country code.
    """
    country_code = country_code.upper()
    if country_code in ADJACENT_COUNTRIES:
        return ADJACENT_COUNTRIES[country_code]
    else:
        return None


def main():
    """
    Main function to handle user input and provide adjacent country names.
    """
    print("Welcome to the Adjacent Country Finder!")
    while True:
        # Taking input from the user
        user_input = input(
            "Enter a country code (e.g., IN, US, NZ) or Q to quit: "
        ).strip()

        if user_input.upper() == "Q":
            print("Exiting the application")
            sys.exit(0)

        # Get adjacent countries
        adjacent_countries = get_adjacent_countries(user_input)

        if adjacent_countries:
            print(f"Adjacent countries for '{user_input.upper()}':")
            for country in adjacent_countries:
                print(f"- {country}")
        else:
            print(
                f"No data found for country code '{user_input.upper()}'. Please try again."
            )


# if __name__ == "__main__":

main()
