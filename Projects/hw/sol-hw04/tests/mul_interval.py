test = {
  'name': 'mul_interval',
  'points': 1,
  'suites': [
    {
      'type': 'doctest',
      'setup': """
      >>> import hw04
      >>> from hw04 import *
      """,
      'cases': [
        {
          'code': """
          >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
          '-8 to 16'
          """
        }
      ]
    },
    {
      'type': 'doctest',
      'setup': """
      >>> import hw04
      >>> old_abstraction = hw04.interval, hw04.lower_bound, hw04.upper_bound
      >>> hw04.interval = lambda a, b: lambda x: a if x == 0 else b
      >>> hw04.lower_bound = lambda s: s(0)
      >>> hw04.upper_bound = lambda s: s(1)
      >>> from hw04 import *
      """,
      'cases': [
        {
          'locked': False,
          'code': """
          >>> # Testing for abstraction violations
          >>> # Your code should not check for which implementation is used
          >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
          '-8 to 16'
          """
        },
      ],
      'teardown': """
      >>> hw04.interval, hw04.lower_bound, hw04.upper_bound = old_abstraction
      """
    },
  ]
}