(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))

(define (ascending? asc-lst)
  (if (or (null? asc-lst) (null? (cdr asc-lst)))
      #t
      (and (<= (car asc-lst) (car (cdr asc-lst)))
           (ascending? (cdr asc-lst)))))

(define (square n) (* n n))

(define (pow base exp)
  (cond 
    ((= exp 0)   1)
    ((even? exp) (square (pow base (/ exp 2))))
    (else        (* base (pow base (- exp 1))))))
