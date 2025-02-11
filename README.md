# Docuentation stub for car-rental-python

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
main/rental/Car.py                    7      0   100%
main/rental/CarRentalCompany.py      11      2    82%   12, 15
main/rental/Criteria.py               2      0   100%
main/rental/Renter.py                 7      0   100%
main/utils/DatePeriod.py             10      0   100%
main/utils/DatePeriodUtil.py          8      0   100%
---------------------------------------------------------------
TOTAL                                45      2    96%
```
