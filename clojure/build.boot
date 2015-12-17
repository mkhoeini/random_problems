
(set-env!
 :source-paths #{"src" "test"}
 :dependencies '[[org.clojure/clojure "1.8.0-RC4"]])

(task-options!
 pom {:project 'random-problems
      :version "0.1.0"})

