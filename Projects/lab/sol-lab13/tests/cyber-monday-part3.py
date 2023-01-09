
test = {
  'name': 'cyber-monday-part3',
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
          sqlite> SELECT * FROM shopping_list;
          GameStation|Hallmart
          uPhone|RestBuy
          wBook|RestBuy
          """,
        },
      ],
    },
  ]
}