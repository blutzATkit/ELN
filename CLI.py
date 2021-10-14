import click
import subprocess
import pty

def getCommandOutput(commandArray, suppressErrors=True):
    process = subprocess.Popen(commandArray, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = process.communicate()
    returnCode = process.returncode
    stdout = output[0].decode("UTF-8")
    stderr = output[1].decode("UTF-8")
    if suppressErrors:
        return stdout
    else:
        return stdout, stderr, returnCode

def runShellScript(commandArray):
    subprocess.call(commandArray)

def getUbuntuVersion():
    ubuntuRelease = ""
    for line in open("/etc/lsb-release"):
        line = line.strip()
        var, arg = line.split('=', 1)
        if var.startswith('DISTRIB_RELEASE'):
            ubuntuRelease = arg

    return ubuntuRelease

@click.group()
def cli():
    pass

@click.command()
def init():
    """Initialization of the DB and required configurations"""
    click.echo(f"Initialization...")
    runShellScript(["/etc/scripts/initScript.sh"])

@click.group()
def landscape():
    pass

@landscape.command()
@click.option("--name", default="default", help="Name of an existing landscape in /share/landscapes/")
def deploy(name):
    """Establish a configuration landscape for the ELN"""
    click.echo(f"Deploy landscape: {name}")
    runShellScript(["/etc/scripts/landscapeScript.sh", name])

@click.command()
@click.option("--destination", help="Destination path for the backup.")
def backup(destination):
    """Backup the existing DB, data and configurations to a given DESTINATION"""
    click.echo(f"Backup to {destination}")
    runShellScript(["/etc/scripts/backupScript.sh"])

@click.command()
@click.option("--version", default="1.0", help="Target version for the upgrade.")
def upgrade(version):
    """Upgrade an existing ELN installation to a desired VERSION"""
    click.echo(f"Upgrading to version {version}")
    runShellScript(["/etc/scripts/upgradeScript.sh"])
    
@click.command()
def startEln():
    """Start ELN"""
    click.echo(f"Start ELN...")
    runShellScript(["/etc/scripts/startELNscript.sh"])
    
@click.command()
def startWorker():
    """Start worker"""
    click.echo(f"Start worker...")
    runShellScript(["/etc/scripts/startWorkerScript.sh"])
    
@click.command()
def shell():
    """Open a root shell"""
    click.echo(f"Root shell...")
    pty.spawn("/bin/bash")
    
@click.command()
def userShell():
    """Open a user shell"""
    click.echo(f"User shell...")
 #   pty.spawn("sudo -E -H -u ${PROD} bash -c '. $HOME/.profile; ' /bin/bash")
    
@click.command()
def info():
    """Display information about the existing installation"""
    click.echo(f"Info...")
    uname = getCommandOutput(['uname', '-a'])
    ubuntuRelease = getUbuntuVersion()
    numberCores, errorInfo, returnCode = getCommandOutput(['nproc', '--all'], False)
    click.echo(f"System: {uname}")
    click.echo(f"Ubuntu {ubuntuRelease}")
    click.echo(f"Number cores: {numberCores}")
    click.echo(f"Error info of nproc --all: {errorInfo}\n")
    click.echo(f"Return code of nproc --all: {returnCode}")

cli.add_command(init)
cli.add_command(landscape)
cli.add_command(backup)
cli.add_command(upgrade)
cli.add_command(startEln)
cli.add_command(startWorker)
cli.add_command(shell)
cli.add_command(userShell)
cli.add_command(info)

if __name__ == '__main__':
    cli()
