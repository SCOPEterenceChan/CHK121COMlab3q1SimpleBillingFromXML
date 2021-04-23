import sys
import loanTableAPI

if __name__ == "__main__":
    loanTableAPI.loanTable(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]))
    loanTableAPI.loanTableHTML(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]))
