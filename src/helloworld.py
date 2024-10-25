import click
from hello_from import helloFrom
from hello_to import helloTo 
      
# Group definition
@click.group()
def cli():
    pass

# From command
@cli.command("from", help="Say hello from someone")
@click.argument("name")
def commandFrom(name):
    click.echo(helloFrom(name))

# To command
@cli.command("to", help="Say hello to someone.")
@click.argument("name")
@click.option("--count", default=1, help="Number of greetings.")
def commandTo(name, count):
    list = helloTo(name, count)
    for entry in list:
        click.echo(entry)

# Main
if __name__ == "__main__":
    cli()