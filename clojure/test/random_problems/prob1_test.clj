(ns random-problems.prob1-test
  (:require [clojure.test :refer [deftest is]]
            [random-problems.prob1 :as prob1]))


(deftest get-numbers-test
  (is (= [123 456]
         (with-in-str "123 456"
           (prob1/get-numbers)))))


(deftest get-duplicates-test
  (is (= [1 2] (prob1/get-duplicates [1 2 2 1 3 4]))))
