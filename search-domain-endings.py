import whois
import argparse


parser = argparse.ArgumentParser(description='Searches for unregistered domains', add_help=True)
parser.add_argument('-f', '--file', action='store', dest='file', help='Reads domain roots to check from a file. One word per line.')
parser.add_argument('-l', '--length', action='store', dest='maxLength', help='Maximum length of the domain (excluding the .com, .us TLD endings)' )
args = parser.parse_args()

def checkRegistration(domain):
    try:
        check = whois.whois(domain)
    except:
        print(domain+" is unregistered")
        logUnregisteredDomain(domain)

def logUnregisteredDomain(domain, logFile="unregistered-domains-endings.txt"):
    with open(logFile, "a") as file:
        file.write(domain+'\n')

if __name__ == "__main__":
    # Setting variables. Inserting defaults if not specified by command flag
    if args.file:
        file = args.file
    if not args.maxLength:
        maxLength = 4
    else:
        maxLength = int(args.maxLength)

    allchar = '0123456789abcdefghijklmnopqrstuvwxyz'
    # If a file is passed, check all of them
    if args.file:
        print("Checking from file")
        with open(args.file) as domainList:
            for domain in domainList:
                domainToCheck = domain.rstrip()
                if len(domainToCheck) <= maxLength:
                    if domainToCheck[-3:] == 'com':
                        print(domainToCheck[:-3]+'.com')
                    #checkRegistration(domainToCheck+".us")
                    #checkRegistration(domainToCheck+".com")



    '''  #Generating 3 letter domains with duplicate letters
    for char in allchar:
        checkRegistration(5 * char + '.us')
        checkRegistration(6 * char + '.us')
        #for secondChar in allchar:
            #checkRegistration(char+secondChar+secondChar+".us")
            #checkRegistration(secondChar+secondChar+char+".us")
    '''
