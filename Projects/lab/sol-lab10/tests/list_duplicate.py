test = {
  'name': 'duplicate',
  'points': 1,
  'suites': [
    {
      'type': 'scheme',
      'scored': True,
      'setup': """
      scm> (load-all ".")
      """,
      'cases': [
        {
          'code': """
          scm> (duplicate '()) 
          ()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': """
          scm> (duplicate '(1 2 3)) 
          (1 1 2 2 3 3)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': """
          scm> (duplicate '(1)) 
          (1 1)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': """
          scm> (duplicate '(0)) 
          (0 0)
          """,
          'hidden': False,
          'locked': False
        }
      ]
    }
  ]
}