(ns random-problems.prob1
  (:require [clojure.string :as string]))


(defn get-numbers []
  (->> (read-line)
       (#(string/split % #"\s+"))
       (mapv #(Integer/parseInt %))))

(defn get-duplicates [numbers]
  (->> numbers
       frequencies
       (filter #(< 1 (val %)))
       (map key)))

(println (get-duplicates (get-numbers)))
