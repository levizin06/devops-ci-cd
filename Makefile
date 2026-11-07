up:
	docker compose up -d

down:
	docker compose down

pull:
	docker compose pull

deploy: pull up

logs:
	docker compose logs -f

ps:
	docker compose ps