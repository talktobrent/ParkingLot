#!/usr/bin/python3
""" Parking lot module, simulates a parking lot """


class ParkingLot:
    """ Simulates parking lot"""

    lots = []
    id = 0

    def __init__(self, width, moto=1, small=1, big=1):
        """ initialize parking lot
        args:
            width: max width of all rows
            moto: motorcycle size
            small: small size spot
            big: big siz spot
        """
        if width > moto + small + big:
            width = moto + small + big
        sizer = [moto, small, big]
        self.tickets = set()
        row = []
        self.lot = []
        for sz, amount in enumerate(sizer, 1):
            while amount > 0:
                row.append(sz)
                amount -= 1
                if len(row) == width:
                    self.lot.append(row)
                    row = []
        if row:
            self.lot.append(row)

        self.id = ParkingLot.id
        ParkingLot.id += 1

        ParkingLot.lots.append(self)

    def park(self, vehicle):
        """ park a vehicle"""

        if vehicle == 'motorcycle':
            avail = [1]
        elif vehicle == 'car':
            avail = [2]
        elif vehicle == 'bus':
            avail = [3, 3, 3, 3, 3]
        else:
            raise ValueError
        for index, row in enumerate(self.lot):
            for x in range(len(row) - (len(avail) - 1)):
                try:
                    if all(test >= avail[0] for test in row[x: x + len(avail)]):
                        ticket = str(index) + '.'
                        for spot in range(x, x + len(avail)):
                            ticket += str(spot)
                            self.lot[index][spot] *= -1
                        self.tickets.add(ticket)
                        return {self.id: ticket}
                except IndexError:
                    break
        print("No Space")
        return False

    def find(self, ticket):
        """ find and remove vehicle"""

        ticket = ticket.pop(self.id)
        if not ticket:
            print("Not parked")
            return False
        for x in ticket.rsplit('.')[1]:
            self.lot[int(ticket[0])][int(x)] *= -1
        self.tickets.remove(ticket)
        return True

    def status(self):
        """ view status of lot"""

        for index, x in enumerate(self.lot):
            print('|', end='')
            for spot, value in enumerate(x):
                if value == 1:
                    print("|", end='')
                if value == 2:
                    print("   |", end='')
                if value == 3:
                    print("     |", end='')
                if value == -1:
                    print("X|", end='')
                if value == -2:
                    print("XXX|", end='')
                if value == -3:
                    print("XXXXX|", end='')
            print()

    @classmethod
    def finder(cls, ticket):
        """ find and retrieve vehicle from any parking lot"""

        for x in cls.lots:
            if x.id in ticket:
                return x.find(ticket)
        return False
