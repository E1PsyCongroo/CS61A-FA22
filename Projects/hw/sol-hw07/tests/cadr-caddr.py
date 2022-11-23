test = {
  'name': 'cadr-caddr',
  'points': 1,
  'suites': [
    {
      'type': 'scheme',
      'setup': r"""
      scm> (load-all ".")
      """,
      'cases': [
        {
          'code': r"""
          scm> (cddr '(1 2 3 4))
          (3 4)
          """,
        },
        {
          'code': r"""
          scm> (cadr '(1 2 3 4))
          2
          """,
        },
        {
          'code': r"""
          scm> (caddr '(1 2 3 4))
          3
          """,
        },
      ],
    },
  ]
}