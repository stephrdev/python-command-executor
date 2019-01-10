import pytest

from command_executor.command import Command
from command_executor.exceptions import CommandExecutionError, CommandParameterError


class OutputCommand(Command):
    command = 'echo "{words}"'
    required_parameters = ['words']


class InvalidCommand(Command):
    command = 'thiscommanddoesnotexist'


class RetValCommand(Command):
    command = 'sh -c "exit {code}"'
    required_parameters = ['code']


class StderrCommand(Command):
    command = 'sh -c "echo \'{words}\' >&2"'
    required_parameters = ['words']


class TestCommand:
    def test_missing_parameters(self):
        with pytest.raises(CommandParameterError) as exc:
            RetValCommand()

        assert 'code' in str(exc.value)

    def test_execute(self):
        cmd = OutputCommand(words='test')
        assert cmd.execute() is True

    def test_execute_output(self):
        cmd = OutputCommand(words='test')
        assert cmd.execute(ignore_output=False) == 'test\n'

    def test_failing_oserror(self):
        with pytest.raises(CommandExecutionError) as exc:
            cmd = InvalidCommand()
            cmd.execute()

        assert exc.value.code == 1
        assert exc.value.command == cmd
        assert exc.value.stderr == (
            "[Errno 2] No such file or directory: 'thiscommanddoesnotexist': "
            "'thiscommanddoesnotexist'"
        )

    def test_failing_return_value(self):
        with pytest.raises(CommandExecutionError) as exc:
            cmd = RetValCommand(code=23)
            cmd.execute()

        assert exc.value.code == 23
        assert exc.value.command == cmd
        assert exc.value.stderr == ''

    def test_failing_return_value_silent(self):
        cmd = RetValCommand(code=23)
        assert cmd.execute(fail_silently=True) is True

    def test_failing_stderr(self):
        with pytest.raises(CommandExecutionError) as exc:
            cmd = StderrCommand(words='test 123')
            cmd.execute()

        assert exc.value.code == 0
        assert exc.value.command == cmd
        assert exc.value.stderr == 'test 123\n'

    def test_failing_stderr_silent(self):
        cmd = StderrCommand(words='test 123')
        assert cmd.execute(fail_silently=True) is True

    def test_pid(self):
        cmd = RetValCommand(code=0)
        assert cmd.execute() is True
        assert cmd.pid == cmd.process.pid
