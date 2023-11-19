from invoke import task
import sys

@task
def start(ctx):
    pty = sys.platform != 'win32'
    ctx.run("python3 src/index.py", pty=pty)

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

@task
def lint(ctx):
    ctx.run("pylint src")

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src")