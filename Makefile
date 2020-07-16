install:
	poetry install
lint:
	poetry run flake8 brain_games
run:
	poetry run brain-games

.PHONY: app test log doc prompt install lint run
