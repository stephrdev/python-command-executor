import shlex
from subprocess import PIPE, Popen

from .exceptions import CommandExecutionError, CommandParameterError


class Command(object):
    pid = None
    command = 'true'
    ignore_output = True
    fail_silently = False
    required_parameters = None

    def __init__(self, **kwargs):
        self.parameters = kwargs
        if not self.validate_parameters():
            raise CommandParameterError(
                'Parameter(s) missing, required parameters: {0}'.format(
                    ', '.join(self.required_parameters)))

    def execute(self, ignore_output=None, fail_silently=None, **kwargs):
        command = self.get_command()
        ignore_output = ignore_output if ignore_output is not None else self.ignore_output
        fail_silently = fail_silently if fail_silently is not None else self.fail_silently

        # Don't automatically merge with os.environ for security reasons.
        # Make this forwarding explicit rather than implicit.
        environ = kwargs.pop('environ', None)
        shell = kwargs.pop('shell', False)

        try:
            process = Popen(
                command,
                shell=shell,
                universal_newlines=True,
                env=environ,
                stdout=PIPE,
                stderr=PIPE,
                stdin=PIPE,
            )
            self.pid = process.pid

            stdout, stderr = process.communicate()
        except OSError as exc:
            raise CommandExecutionError(1, str(exc), self)

        if not fail_silently and (stderr or process.returncode != 0):
            raise CommandExecutionError(process.returncode, stderr, self)

        return True if ignore_output else self.handle_output(stdout)

    def validate_parameters(self):
        return all(k in self.parameters for k in self.required_parameters or [])

    def get_parameters(self):
        return self.parameters

    def get_command(self):
        command = self.command.format(**self.get_parameters())
        return shlex.split(str(command))

    def handle_output(self, output):
        return output
