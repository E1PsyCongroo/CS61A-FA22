test = {
  'name': 'eval-calls',
  'points': 0,
  'suites': [
    {
        'type': 'concept',
        'cases': [
        {
          'question': r"""
          How many calls are made to scheme_eval to evaluate the expression: (+ 2 4 6 8) ?
          """,
          'choices': ['1', '2', '5', '6', '7', '8'],
          'answer': '6',
        },
        { 
          'question': r"""
          How many calls are made to scheme_apply: (+ 2 4 6 8) ?
          """,
          'choices': ['1', '2', '5', '6', '7', '8'],
          'answer': '1',
        },
        { 
          'question': r"""
          How many calls are made to scheme_eval: (+ 2 (* 4 (- 6 8))) ?
          """,
          'choices': ['3', '7', '8', '9', '10', '13'],
          'answer': '10',
        },
        { 
          'question': r"""
          How many calls are made to scheme_apply: (+ 2 (* 4 (- 6 8))) ?
          """,
          'choices': ['3', '7', '8', '9', '10', '13'],
          'answer': '3',
        },
        { 
          'question': r"""
          How many calls are made to scheme_eval: (if #f (+ 2 3) (+ 1 2)) ?
          """,
          'choices': ['1', '2', '4', '6', '8', '10'],
          'answer': '6',
        },
        { 
          'question': r"""
          How many calls are made to scheme_apply: (if #f (+ 2 3) (+ 1 2)) ?
          """,
          'choices': ['1', '2', '4', '6', '8', '10'],
          'answer': '1',
        },
        { 
          'question': r"""
          How many calls are made to scheme_eval: (define (cube a) (* a a a)) ?
          """,
          'choices': ['0', '1', '3', '7', '8', '9'],
          'answer': '1',
        },
        { 
          'question': r"""
          How many calls are made to scheme_apply: (define (cube a) (* a a a)) ?
          """,
          'choices': ['0', '1', '3', '7', '8', '9'],
          'answer': '0',
        },
        { 
          'question': r"""
          How many calls are made to scheme_eval: (cube 3) ?
          """,
          'choices': ['2', '3', '7', '8', '9', '11'],
          'answer': '8',
        },
        { 
          'question': r"""
          How many calls are made to scheme_apply: (cube 3) ?
          """,
          'choices': ['2', '3', '7', '8', '9', '11'],
          'answer': '2',
        }
      ],
    }
  ]
}