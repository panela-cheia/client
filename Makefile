all:
	python3 -B src/main.py

venv:
	python3 -m venv . 

run_venv:
	. bin/activate && python3 -B src/main.py

clean:
	true || deactivate && rm -rf bin/ lib/ lib64/ lib64 include/ share/ pyvenv.cfg