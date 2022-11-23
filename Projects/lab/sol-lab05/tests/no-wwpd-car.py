test = {
  'name': 'Car',
  'points': 0,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': """
          >>> from car import *
          >>> deneros_car = Car('Tesla', 'Model S')
          >>> deneros_car.model
          'Model S'
          >>> deneros_car.gas = 10
          >>> deneros_car.drive()
          'Tesla Model S goes vroom!'
          >>> deneros_car.drive()
          'Cannot drive!'
          >>> deneros_car.fill_gas()
          'Gas level: 20'
          >>> deneros_car.gas
          20
          >>> Car.gas
          30
          """
        },
        {
          'code': """
          >>> from car import *
          >>> deneros_car = Car('Tesla', 'Model S')
          >>> deneros_car.wheels = 2
          >>> deneros_car.wheels
          2
          >>> Car.num_wheels
          4
          >>> deneros_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          'Cannot drive!'
          >>> Car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          Error
          >>> Car.drive(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
          'Cannot drive!'
          """
        }
      ]
    }
  ]
}