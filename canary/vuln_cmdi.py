# CANARY FILE — codice deliberatamente vulnerabile per validare Snyk Code.
# NON deve essere mai mergiato su branch protetti. Rimuovere dopo il test.
import os
import sys


def run_lookup(user_input: str) -> None:
    # Atteso: Command Injection (CWE-78) — severity High.
    # Taint: argv (source) -> os.system (sink), nessuna sanitizzazione.
    os.system("host " + user_input)


if __name__ == "__main__":
    run_lookup(sys.argv[1])