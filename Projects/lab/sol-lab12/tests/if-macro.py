test = {
  'name': 'if-macro',
  'points': 1,
  'suites': [
    {
      'type': 'scheme',
      'scored': True,
      'cases': [
        {
          'code': r"""
          scm> (if-macro (= 0 0) 2 3)
          2
          scm> (if-macro (= 1 0) (print 3) (print 5))
          5
          """,
          'locked' : False,
          'hidden' : False
        },
      ],
      'setup': r"""
      scm> (load-all ".")
      """,
    },
  ]
}