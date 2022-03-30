# WarHammer_DB

War Hammer 40.000 Universe

## database tables:

- heroes: id, side, name, birthday, power, story, motos   
- motos: id, hero_id, moto_id, moto
- battles: id, hero_id_1, hero_id_2, moto_id_1, moto_id_2, winner
- story: id, story, hero_id

## for start project

- start:
  `docker-compose up -d --build`

- fill test database:
  `python fill_db.py`

## python scripts

- add hero:
  `python -m scripts add-hero <name> <side>`

- add hero:
  `python -m scripts add-moto <hero_id> <moto>`

- do battle:
  `python -m scripts add-battle`

- add story:
  `python -m scripts add-story <hero_id> <story>`

- delete hero:
  `python -m scripts delete-hero <hero_id>`
