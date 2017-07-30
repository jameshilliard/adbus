# == Copyright: 2017, CCX Technologies

import inspect

from .. import sdbus


class Listen:
    """Calls a D-Bus Method in another process.

    This is a co-routine, so must be await-ed from within a asyncio mainloop.

    Args:
        service (adbus.server.Service): service to connect to
        address (str): address (name) of the D-Bus Service to call
        path (str): path of method to call, ie. /com/awesome/Settings1
        interface (str): interface label to call, ie. com.awesome.settings
        signal (str): name of the signal to listen to, ie. TestSignal
        args (list or tuple): optional, list of argument values to match,
            the argument must be a string, useful for listening to property
            changes
    """

    def __init__(
        self,
        service,
        address,
        path,
        interface,
        signal,
        callback,
        args=(),
    ):

        self.signature = ''
        sig = inspect.signature(callback)
        for param in sig.parameters.values():
            if param.annotation != inspect.Parameter.empty:
                self.signature += sdbus.dbus_signature(param.annotation)
            else:
                self.signature += sdbus.variant_signature()

        self.sdbus = sdbus.Listen(
            service.sdbus, address, path, interface, signal, callback, args,
            self.signature
        )
