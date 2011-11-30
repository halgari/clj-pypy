(def fibonacci-1
    (fn (x)
        (fibonacci-3 0 1 x)))

(def fibonacci-3
    (fn (current next remaining)
        (if (= 0 remaining)
            current
            (recur next (+ current next) (- remaining 1)))))

(fibonacci-1 1000000)
