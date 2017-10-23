
CP=cp
RM=rm
ECHO=echo
PYTEST=pytest


test: clean
	@$(ECHO) "Executing test cases"
	@$(PYTEST) --cov-report html --cov .

.PHONY: clean

clean:
	# Redundant, but clean anyway
	@$(ECHO) "Deleting files"
	@$(RM) -rf __pycache__
	@$(RM) -rf *.pyc
