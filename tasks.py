import sys
from subprocess import call
from invoke import task

@task
def start(ctx):
    pty = sys.platform != 'win32'
    ctx.run("python3 src/index_gui.py", pty=pty)

@task
def start_text(ctx):
    pty = sys.platform != 'win32'
    ctx.run("python3 src/index_text.py", pty=pty)

@task
def test(ctx):
    pty = sys.platform != 'win32'
    ctx.run("pytest src", pty=pty)

@task
def coverage(ctx):
    pty = sys.platform != 'win32'
    ctx.run("coverage run --branch -m pytest src", pty=pty)

@task(coverage)
def coverage_report(ctx):
    pty = sys.platform != 'win32'
    ctx.run("coverage html", pty=pty)
    if sys.platform != "win32":
        call(("xdg-open", "htmlcov/index.html"))

@task
def lint(ctx):
    ctx.run("pylint src")

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src")

@task
def build(ctx):
    ctx.run("python3 src/init_database.py")
