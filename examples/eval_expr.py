# Evaluates an expression (e.g. "X86_64 || (X86_32 && X86_LOCAL_APIC)") in the
# context of a configuration. Note that this always yields a tristate value (n,
# m, or y).
#
# Usage:
#
#   $ make [ARCH=<arch>] scriptconfig SCRIPT=Kconfiglib/examples/eval_expr.py SCRIPT_ARG=<expr>

import kconfiglib
import sys

if len(sys.argv) < 3:
    print('Pass symbol name (without "CONFIG_" prefix) with SCRIPT_ARG=NAME')
    sys.exit(1)

expr = sys.argv[2]

kconf = kconfiglib.Kconfig(sys.argv[1])

# Enable modules so that m doesn't get demoted to n
kconf.modules.set_value(2)

print("the expression '{}' evaluates to {}"
      .format(expr, kconf.eval_string(expr)))
