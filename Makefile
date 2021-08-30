bash_test:
	podman build -f bash/Containerfile -t unit_test_bash bash/
	podman run --rm localhost/unit_test_bash
	
bash_calculator:
	cd bash && ./calculator.sh
	
python3_test:
	podman build -f python3/Containerfile -t unit_test_python3 python3/
	podman run --rm localhost/unit_test_python3	