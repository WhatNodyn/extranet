from extranet import app, db, cache
from extranet.crawler import locations, log

@app.cli.command('createdb')
def createdb():
  print('Creating database...')
  db.create_all()
  print('Done.')

@app.cli.command('dropdb')
def dropdb():
  print('Dropping database...')
  db.drop_all()
  print('Done.')

@app.cli.command('clearcache')
def clearcache():
  print('Clearing cache...')
  cache.clear()
  print('Done.')

@app.cli.command('crawl')
def crawl():
  print('Updating data...')
  if log.needs_crawling('locations'):
    locations.update()
  else:
    print('Locations up to date!')
  print('Done.')