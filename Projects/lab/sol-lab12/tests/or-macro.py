test = {
  'name': 'or-macro',
  'points': 1,
  'suites': [
    {
      'type': 'scheme',
      'scored': True,
      'cases': [
        {
          'code': r"""
          scm> (or-macro #t #f)
          #t
          scm> (or-macro #f #t)
          #t
          scm> (or-macro 0 #f)
          0
          """,
          'locked' : False,
          'hidden' : False
        },
        {
          'code': r"""
          scm> (or-macro (/ 1 0) #t)
          SchemeError
          """,
          'locked' : False,
          'hidden' : False
        },
        {
          'code': r"""
          scm> (or-macro #t (/ 1 0))
          #t
          """,
          'locked' : False,
          'hidden' : False
        },
        {
          'code': r"""
          scm> (or-macro #f (/ 1 0))
          SchemeError
          """,
          'locked' : False,
          'hidden' : False
        },
        {
          'code': r"""
          scm> (or-macro (print 'hi) (print 'bye))
          hi
          scm> (or-macro (begin (print 'hi) #f) (print 'bye))
          hi
          bye
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