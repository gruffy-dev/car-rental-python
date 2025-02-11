# Documentation stub for car-rental-python

# Prerequisites

These set of classes have been tested on Python 3.9.6.

# Installation

1. Clone the code from the git repository [here](https://github.com/gruffy-dev/car-rental-python).

2. Create the virtual environment as follows:

```
% python3 -m venv venv
% pip install -r requirements.txt
```

# Usage

These set of classes expose a set of methods that are executed as part of their corresponding unit tests.  Refer to the subsequent section on Testing for instructions on how to execute these tests.

# Testing

The coverage library is employed to measure code coverage for the test casts.  The tests and coverage analysis can be executed as follows:

```
% coverage run --source main -m unittest  && coverage report -m
Name                              Stmts   Miss  Cover   Missing
---------------------------------------------------------------
main/rental/Car.py                   38      0   100%
main/rental/CarRentalCompany.py      39      1    97%   66
main/rental/Criteria.py              12      0   100%
main/rental/Renter.py                 7      0   100%
main/utils/DatePeriod.py             10      0   100%
main/utils/DatePeriodUtil.py          8      0   100%
---------------------------------------------------------------
TOTAL                               114      1    99%

```

# Thoughts on Productionisation

- Though there is no strict rule on the file naming in Python, snake case is generally preferred.  As Python supports multi platform execution, naming files using upper case (in this example, Pascal Case) is generally discouraged.  
- Unit test files are normally named with a test_ prefix.  In fact, this is the default convention that coverage expects.
- There are missing __init__.py files in the class directories which really should be there we are making this a package.  Though this has not been added to them, they are a requirement in the test directories for coverage to work.
- Methods are missing type hints.  Though this is not enforced by the runtime, it does add a layer of additional checks within the IDE.
- Class properties are missing accessor methods.  Again, though properties cannot be marked private, they can be highlighted as private by convention with the _ prefix.  Accessor metthods provide a layer of data encapsulation.