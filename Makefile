bash_test:
	podman build -f bash/Containerfile -t unit_test_bash bash/
	podman run localhost/unit_test_bash
	
bash_calculator:
	cd bash && ./calculator.sh