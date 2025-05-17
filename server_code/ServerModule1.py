import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

from datetime i

@anvil.server.callable
def say_hello(name):
  print(name)
  app_tables.visitors.add_row(name=name, when=datetime.now())