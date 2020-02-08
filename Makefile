
CP=cp
RM=rm
ECHO=echo
PYTEST=pytest


test: clean
	@$(ECHO) "Executing test cases"
	@$(PYTEST) --cov-report html --cov .

.PHONY: clean

clean:
	@$(ECHO) "Deleting files"
	@$(RM) -rf .coverage
	@$(RM) -rf .pytest_cache
	@$(RM) -rf htmlcov
