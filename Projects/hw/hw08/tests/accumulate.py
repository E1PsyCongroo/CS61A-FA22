test = {
  'name': 'accumulate',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (accumulate * 1 5 identity)
          120
          scm> (accumulate * 2 4 identity)
          48
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      scm> (define (identity x) x)
      """,
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (define (square x) (* x x))
          square
          scm> (accumulate + 0 5 square)
          55
          scm> (accumulate + 5 5 square)
          60
          scm> (accumulate + 2 3 square)
          16
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
