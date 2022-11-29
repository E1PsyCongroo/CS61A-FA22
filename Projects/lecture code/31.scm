;; Compute n! * k
(define (factorial n k)
  (if (= n 0) k
    (factorial (- n 1)
               (* k n))))

;; Compute the length of well-formed list s.
(define (length s)
  (if (null? s) 0
    (+ 1 (length (cdr s)))))

;; Compute the length of well-formed list s.
(define (length-tail s)
  (define (length-iter s n)
    (if (null? s) n
      (length-iter (cdr s)
                   (+ 1 n))))
  (length-iter s 0))

;; Compute the length of well-formed list s.
(define (lengthy s)
  (+ 1 (if (null? s)
           -1
           (lengthy (cdr s)))))

;; Return whether s contains v.
(define (contains s v)
  (if (null? s)
      false
      (if (= v (car s))
          true
          (contains (cdr s) v))))

;; Return whether s has any repeated elements
(define (has-repeat s)
  (if (null? s)
      false
      (if (contains? (cdr s) (car s))
          true
          (has-repeat (cdr s)))))

;; Return the nth Fibonacci number.
(define (fib n)
  (define (fib-iter current k)
    (if (= k n)
        current
        (fib-iter (+ current
                     (fib (- k 1)))
                  (+ k 1))))
  (if (= 1 n) 0 (fib-iter 1 2)))

;; Reduce s using procedure and start value.
(define (reduce procedure s start)
  (if (null? s) start
    (reduce procedure
            (cdr s)
            (procedure start (car s)))))

;; Return a copy of s with elements in reverse order.
(define (reverse s)
  (define (reverse-iter s r)
    (if (null? s) r
      (reverse-iter (cdr s)
                    (cons (car s) r))))
  (reverse-iter s nil))

;; Map procedure over s.
(define (map-rec procedure s)
  (if (null? s) nil
    (cons (procedure (car s))
          (map-rec procedure (cdr s)))))

;; Map procedure over s.
(define (map procedure s)
  (define (map-reverse s m)
    (if (null? s) m
      (map-reverse (cdr s)
                (cons (procedure (car s)) m))))
  (reverse (map-reverse s nil)))

;;; Tests

(define (assert-equal v1 v2)
  (if (equal? v1 v2) 'okay (list v2 'does 'not 'equal v1)))

(define square (lambda (x) (* x x)))

(assert-equal 360 (factorial 5 3))
(assert-equal 4 (length '(5 6 7 8)))
(assert-equal 4 (length-tail '(5 6 7 8)))
(assert-equal 4 (lengthy '(5 6 7 8)))
(assert-equal #t (contains '(4 5 6) 5))
(assert-equal #f (contains '(4 6 8) 5))
(assert-equal 5 (fib 6))
(assert-equal 1680 (reduce * '(5 6 7 8) 1))
(assert-equal '(5 4 3 2)
              (reduce (lambda (x y) (cons y x)) '(3 4 5) '(2)))
(assert-equal '(8 7 6 5) (reverse '(5 6 7 8)))
(assert-equal '(25 36 49 64) (map-rec square '(5 6 7 8)))
(assert-equal '(25 36 49 64) (map square '(5 6 7 8)))
