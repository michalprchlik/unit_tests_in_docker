bash_test:
	podman build -f bash/Containerfile -t bash_test bash/
	podman run --rm localhost/bash_test
	
bash_calculator:
	cd bash && ./calculator.sh
	
python3_test:
	podman build -f python3/Containerfile -t python3_test python3/
	podman run --rm localhost/python3_test	
	
python3_unittest:
	podman build -f python3_unittest/Containerfile -t python3_unittest python3_unittest/
	podman run --rm localhost/python3_unittest		
	

python3_api_mock:
	podman build -f python3_api_mock/Containerfile -t python3_api_mock python3_api_mock/
	podman run --rm localhost/python3_api_mock
	
python3_mock_server:
	podman build -f python3_mock_server/Containerfile -t python3_mock_server python3_mock_server/
	podman run --rm localhost/python3_mock_server	