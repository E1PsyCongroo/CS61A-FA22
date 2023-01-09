
test = {
  'name': 'cyber-monday-part1',
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
          sqlite> SELECT category, ROUND(average_price) FROM average_prices;
          computer|109.0
          games|350.0
          phone|90.0
          """,
        },
      ],
    },
  ]
}