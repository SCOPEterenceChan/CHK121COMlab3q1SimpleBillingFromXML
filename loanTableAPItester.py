import sys
import loanTableAPI

if __name__ == "__main__":
    try:
        loanTableAPI.loanTable(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]))
        loanTableAPI.loanTableHTML(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]))
    except ValueError as valueError:
        print(valueError,file=sys.stderr,flush=True)
