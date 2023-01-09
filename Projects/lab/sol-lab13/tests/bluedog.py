test = {
  'name': 'bluedog',
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
          sqlite> SELECT * FROM bluedog;
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          sqlite> SELECT * FROM bluedog_songs;
          blue|dog|Glimpse of Us
          blue|dog|The Other Side of Paradise
          blue|dog|Leave the Door Open
          blue|dog|Bohemian Rhapsody
          blue|dog|Dancing Queen
          blue|dog|Palette
          blue|dog|Bohemian Rhapsody
          blue|dog|good 4 u
          blue|dog|Clair de Lune
          blue|dog|Dancing Queen
          """,
        },
      ],
    },
  ]
}