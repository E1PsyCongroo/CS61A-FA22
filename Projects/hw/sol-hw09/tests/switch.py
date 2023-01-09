test = {
  'name': 'switch',
  'points': 1,
  'suites': [
    {
      'type': 'scheme',
      'scored': True,
      'cases': [
        {
          'code': r"""
          scm> (switch 1 ((1 (print 'a))
          ....            (2 (print 'b))
          ....            (3 (print 'c))))
          a
          scm> (switch (+ 1 1) ((1 (print 'a))
          ....                  (2 (print 'b))
          ....                  (3 (print 'c))))
          b
          scm> (define x 'b)
          x
          scm> (switch x ((a (print 1))
          ....            (b (print 2))
          ....            (c (print 3))))
          2
          """,
          'locked' : False
        },
      ],
      'setup': r"""
      scm> (load-all ".")
      """,
    },
  ]
}