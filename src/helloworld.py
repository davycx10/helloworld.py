import click
      
# Group definition
@click.group()
def cli():
    pass

# From command
@cli.command("from", help="Say hello from someone")
@click.argument("name")
def commandFrom(name):
    click.echo(f"{name} say Hello ! ")

# To command
@cli.command("to", help="Say hello to someone.")
@click.argument("name")
@click.option("--count", default=1, help="Number of greetings.")
def commandTo(name, count):
    for _ in range(count):
        click.echo(f"Hello, {name} !")

# Main
if __name__ == "__main__":
    cli()

    
    
    
 