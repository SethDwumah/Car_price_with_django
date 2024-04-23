from django.db import models

# Create your models here.

class CarPrice(models.Model):
   

    MAKE_CHOICES = (
    (1, 'BMW'),
    (2, 'Audi'),
    (3, 'FIAT'),
    (4, 'Mercedes-Benz'),
    (5, 'Chrysler'),
    (6, 'Nissan'),
    (7, 'Volvo'),
    (8, 'Mazda'),
    (9, 'Mitsubishi'),
    (10, 'Ferrari'),
    (11, 'Alfa Romeo'),
    (12, 'Toyota'),
    (13, 'McLaren'),
    (14, 'Maybach'),
    (15, 'Pontiac'),
    (16, 'Porsche'),
    (17, 'Saab'),
    (18, 'GMC'),
    (19, 'Hyundai'),
    (20, 'Plymouth'),
    (21, 'Honda'),
    (22, 'Oldsmobile'),
    (23, 'Suzuki'),
    (24, 'Ford'),
    (25, 'Cadillac'),
    (26, 'Kia'),
    (27, 'Bentley'),
    (28, 'Chevrolet'),
    (29, 'Dodge'),
    (30, 'Lamborghini'),
    (31, 'Lincoln'),
    (32, 'Subaru'),
    (33, 'Volkswagen'),
    (34, 'Spyker'),
    (35, 'Buick'),
    (36, 'Acura'),
    (37, 'Rolls-Royce'),
    (38, 'Maserati'),
    (39, 'Aston Martin'),
    (40, 'Land Rover'),
    (41, 'Lotus'),
    (42, 'Infiniti'),
    (43, 'Scion'),
    (44, 'Genesis'),
    (45, 'HUMMER'),
    (46, 'Bugatti')
    )

    ENGINE_TYPE_CHOICES = (
    (1, 'premium unleaded (required)'),
    (2, 'regular unleaded'),
    (3, 'premium unleaded (recommended)'),
    (4, 'flex-fuel (unleaded/E85)'),
    (5, 'diesel'),
    (6, 'flex-fuel (premium unleaded recommended/E85)'),
    (7, 'electric'),
    (8, 'natural gas'),
    (9, 'flex-fuel (premium unleaded required/E85)'),
)

    TRANSMISSION_TYPE_CHOICES = (
    (1, 'MANUAL'),
    (2, 'AUTOMATIC'),
    (3, 'AUTOMATED_MANUAL'),
    (4, 'UNKNOWN'),
    (5, 'DIRECT_DRIVE'),
)

    DRIVEN_WHEELS_CHOICES = (
    (1, 'rear wheel drive'),
    (2, 'front wheel drive'),
    (3, 'all wheel drive'),
    (4, 'four wheel drive'),
)

    VEHICLE_SIZE_CHOICES = (
        (1,'Compact'),
        (2,'Midsize'),
        (3,'Large'),
    )

    VEHICLE_STYLE_CHOICES = (
    (1, 'Coupe'),
    (2, 'Convertible'),
    (3, 'Sedan'),
    (4, 'Wagon'),
    (5, '4dr Hatchback'),
    (6, '2dr Hatchback'),
    (7, '4dr SUV'),
    (8, 'Passenger Minivan'),
    (9, 'Cargo Minivan'),
    (10, 'Crew Cab Pickup'),
    (11, 'Regular Cab Pickup'),
    (12, 'Extended Cab Pickup'),
    (13, '2dr SUV'),
    (14, 'Cargo Van'),
    (15, 'Convertible SUV'),
    (16, 'Passenger Van'),
)

    make =models.IntegerField(choices=MAKE_CHOICES)
    year = models.IntegerField()
    engine_fuel_type =models.IntegerField(choices=ENGINE_TYPE_CHOICES)
    engine_hp = models.IntegerField()
    engine_cylinders  =models.IntegerField()
    transmission_type = models.IntegerField(choices=TRANSMISSION_TYPE_CHOICES)
    driven_wheels =models.IntegerField(choices=DRIVEN_WHEELS_CHOICES)
    number_of_doors = models.IntegerField()
    vehicle_size =models.IntegerField(choices=VEHICLE_SIZE_CHOICES)
    vehicle_style = models.IntegerField(choices=VEHICLE_STYLE_CHOICES)
    highway_mpg = models.IntegerField()
    city_mpg = models.IntegerField()
    popularity = models.IntegerField()
    price = models.IntegerField()


    def __str__(self):
        return self.price
    

