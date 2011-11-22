(def fibonacci
    (fn (x)
        (fibonacci 0 1 x)))

(def fibonacci
    (fn (current next remaining)
        (if (= 0 remaining)
            current
            (fibonacci next (+ current next) (- remaining 1)))))

(fibonacci 100000)
