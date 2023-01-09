
test = {
  'name': 'cyber-monday-part4',
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
          sqlite> SELECT * FROM total_bandwidth;
          85
          """,
        },
      ],
    },
  ]
}