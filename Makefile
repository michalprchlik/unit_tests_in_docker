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
	
python3_api_cert:
	mkdir -p python3_api/cert
	openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout python3_api/cert/nginx.key -out python3_api/cert/nginx.crt

python3_api:
	podman build -f python3_api/Containerfile -t python3_api python3_api/
	podman run --rm localhost/python3_api		
	
python3_api_mock:
	podman build -f python3_api_mock/Containerfile -t python3_api_mock python3_api_mock/
	podman run --rm localhost/python3_api_mock