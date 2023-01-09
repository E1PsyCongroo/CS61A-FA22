test = {
  'name': 'sevens',
  'points': 1,
  'suites': [
    {
      'type': 'sqlite',
      'setup': """
      sqlite> .read lab13.sql
      """,
      'cases': [
        {
          'locked': False,
          'code': r"""
          sqlite> SELECT * FROM sevens;
          7
          I find this question condescending
          7
          seven
          7
          7
          7
          7
          """,
        },
      ],
    },
  ]
}