# challenge-insert-element
These are three solution for the same problem (insert a list of elements in list at specific position, one after the other)
 - *easy-way* is the natural implementation
 - *before-after* is the way i tried to improve the "easy-way" implementation, without getting any relevant improvement. The problem is that the delete (obtained via np.concatenate of sliced list) is time-expensive. It acts by finding, step by step, the next element in the final array, by increasing/decreasing all the indices before/after the element found.
 - *double-stack* is the solution inspired by the suggestion (found online) to use two stack to solve the problem. It acts (in some sense) like a slinky.

