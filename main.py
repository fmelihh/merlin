import click


@click.group()
def server_cli():
    pass


@click.group()
def client_cli():
    pass


@server_cli.command()
@click.option("--server-name", help="Server Display Name")
@click.pass_context
def server(ctx, server_name):
    # by means other than the `if` block below)
    click.echo(ctx)
    click.echo("server")


@client_cli.command()
@click.option("--server-uuid", help="Client UUID")
def client(server_uuid: str):
    click.echo(f"client {server_uuid}")


cli = click.CommandCollection(sources=[server_cli, client_cli])

if __name__ == "__main__":
    cli()
