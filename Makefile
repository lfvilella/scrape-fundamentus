all:
	@echo "Hello $(LOGNAME), nothing to do by default"
	@echo "Try 'make help'"

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

validate_env:
	@command -v docker > /dev/null || (echo "You need to install docker and docker-compose before proceeding" && exit 1)
	@command -v docker-compose > /dev/null || (echo "You need to install docker and docker-compose before proceeding" && exit 1)

build: remove ## 🛠 Build the container
	@[ -f .env ] || cp template.env .env
	@docker-compose up --build -d

cmd: ## Access bash
	@docker-compose run --rm backend /bin/bash

test: ## Run tests
	@docker-compose run --rm backend /bin/bash -c "pip install pytest && pytest ../tests/"

run: build ## 🌶 Start flask dev server
	@docker-compose run --rm -e FLASK_APP=app.py -e FLASK_ENV=development --service-ports app run --host 0.0.0.0 --reload

run-debug: ## 🌶 + 🐛 Start flask dev server with Debug
	@docker-compose run --rm -e DEBUGGER=True -e FLASK_APP=app.py -e FLASK_ENV=development --service-ports app run --host 0.0.0.0

gunicorn:  ## 🦄 Start flask dev with unicorn
	@docker-compose run --rm --service-ports backend gunicorn --reload --bind 0.0.0.0:5000 app:app

gunicorndebug: ## 🦄 + 🐛 Start flask dev with unicorn and Debug
	@docker-compose run --rm -e DEBUGGER=True --service-ports backend gunicorn --reload --bind 0.0.0.0:5000 --timeout 3600 app:app

start:
	@docker-compose start

down: ## Stop container
	@docker-compose stop || true

delete-container: down
	@docker-compose down || true

remove: delete-container ## Delete containers and images

.DEFAULT_GOAL := help
