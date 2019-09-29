# Ant-Colony
Решение задачи коммивояжера с помощью муравьиного алгоритма.
На вход подается YxY чисел, представляющих собой матрицу смежности полносвязного
графа.
На выходе получается вес наиболее выгодного маршрута.
Суть алгоритма заключается в многократном проходе по разным путям. Выбор
очередной вершины случаен, но на него равносильно влияют вес вершины (наименьший
вес обладает большим приоритетом) и концентрация феромона в конкретной вершине.
Концентрация феромона зависит от того, сколько муравьёв прошло по данной вершине,
причем чем более длинный путь уже прошел муравей, тем меньше феромона он оставит.
Также, после распределения вероятностей прохода в каждую доступную вершину,
совершается еще одна случайная выборка из этих вероятностей, благодаря которой
несколько муравьев могут найти еще более удачный путь.
За счёт всего вышесказанного, задача коммивояжера, перебор всех путей которой
имеет сложность n! ((n-1)!/2 при небольшой оптимизации), где n - количество
вершин, может быть решена во много раз более оптимизированным способом.
К примеру, на матрицу 14х14 может уйти перебор всего 4000~5000 вариантов,
вместо 13!/2.
К минусам алгоритма можно отнести получение не всегда наилучшего пути,
тем не менее, можно гарантировать, что найденный путь будет далеко не наихудшим.
