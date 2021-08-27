bash_test:
	docker build -f bash/Containerfile -t unit_test_bash bash/
	docker run localhost/unit_test_bash
	
bash_calculator:
	cd bash && ./calculator.sh