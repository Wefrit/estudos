"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    seat_row = ["A","B","C","D"]
    counter = 0
    while counter < number:
        for seat in seat_row:
            yield seat
            counter += 1


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    seat_row = ["A","B","C","D"]
    seat_number = 1
    count = 0
    while count < number:
        for seat in seat_row:
            yield (f"{seat_number}{seat}")
            count += 1
            if seat_number == 13:
                seat_number +=1
                continue
        seat_number += 1



def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    passengers_seats_dict = {}
    seat = generate_seats(len(passengers))
    for passenger in passengers:
        passengers_seats_dict[passenger] = next(seat)
    return passengers_seats_dict

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    ticket_id = 0
    for seat in seat_numbers:
        ticket_id = (f"{seat}{flight_id}0000")
        yield ticket_id[:11]


seat_numbers = ['1A', '17D']
flight_id = 'CO1234'
generate_codes(seat_numbers, flight_id)
ticket_ids = generate_codes(seat_numbers, flight_id)
print(next(ticket_ids))
print(next(ticket_ids))