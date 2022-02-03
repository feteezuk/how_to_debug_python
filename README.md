# how_to_debug_python
how_to_debug_python discusses 3 ways to debug python code

## Always Set up virtual Environment.
In Terminal,
1. ```virtualenv ~/.how_to_debug_python```
2. ```source ~/.how_to_debug_python/bin/activate```
3. 
One of the critical challenges in a distributed system is that error 
conditions can appear stochastically, 
making it hard to perform root cause analysis.
Name five things that can mitigate this problem
in production distributed systems.

1. Being very consistent in naming variables
2. Writing clear notes to help multiple team members to understand the code
3. Using print statements, try/except , and dbt when errors occur
4. Understanding variable Scope very well. 
5. Use a virtual environment and pip freeze to make sure you have the latest version of each library