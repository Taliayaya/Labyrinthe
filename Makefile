init:
	pip install .
deps:
	pip install -r requirements.txt
test:
	python tests/basic.test.py
run:
	python labyrinthe/
clean:
	@echo "Début de la tentative de suppression du cache"
	rm -rf __pycache__
	rm -rf labyrinthe/__pycache__
	@echo "Fin de la suppression du cache"
windows:
	python3.10.exe -m pip install .