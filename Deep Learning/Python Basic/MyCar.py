def make_car(manufacturer, model, **options):
    car_dict = {
        'manufacturer' : manufacturer,
        'model' : model,
    }
    for option, value in options.items():
        car_dict[option] = value
    return car_dict

