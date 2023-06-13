all:
	python3 -B src/main.py

venv:
	python3 -m venv . && . bin/activate && pip3 install -r requirements.txt

run_venv:
	. bin/activate && python3 -B src/main.py

clean:
	true || deactivate && rm -rf bin/ lib/ lib64/ lib64 include/ share/ pyvenv.cfg