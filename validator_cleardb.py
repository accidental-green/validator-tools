import subprocess
import os
import sys

# Change to the home folder
os.chdir(os.path.expanduser("~"))

# Check sudo privileges
print("Checking sudo privileges")
try:
    subprocess.run(['sudo', '-v'], check=True)
    print("Sudo credentials authenticated.")
except subprocess.CalledProcessError:
    print("Failed to verify sudo credentials.")
    exit(1)

############# CLI CODE #######################

# Define valid execution and consensus clients
valid_clients = ['GETH', 'BESU', 'NETHERMIND', 'RETH', 'ERIGON', 'PRYSM', 'LIGHTHOUSE', 'TEKU', 'NIMBUS', 'LODESTAR']
valid_networks = ['MAINNET', 'HOLESKY', 'SEPOLIA']

# Ask the user for the execution/consensus client to DELETE
execution_client_delete = ""
while execution_client_delete not in valid_clients:
    execution_client_delete = input("\nSelect Ethereum Client database to DELETE:\ngeth, besu, nethermind, reth, erigon, prysm, lighthouse, teku, nimbus, lodestar\n\n").upper()
    if execution_client_delete not in valid_clients:
        print("Invalid option, please try again.")

# Confirmation
confirmation = ""
while confirmation not in ['Y', 'N', 'YES', 'NO']:
    confirmation = input(f"\nYou have selected to DELETE the database of {execution_client_delete}. Continue (y/n)? ").upper()
    if confirmation not in ['Y', 'N', 'YES', 'NO']:
        print("Invalid option, please try again.")

if confirmation in ['N', 'NO']:
    print("Operation cancelled by the user.")
    sys.exit()

# Convert user inputs to lowercase
execution_client_delete = execution_client_delete.lower()

# Print User Input
print("\n##### User Selected Input #####")
print(f"Execution/Consensus Client to DELETE Database: {execution_client_delete}\n")

######### REMOVE, RECREATE & SET PERMISSIONS FOR EXECUTION & CONSENSUS CLIENT DATABASES ###################

# Database paths for execution clients
execution_client_db_paths = {
    "geth": ("/var/lib/geth", "geth"),
    "besu": ("/var/lib/besu", "besu"),
    "nethermind": ("/var/lib/nethermind", "nethermind"),
    "reth": ("/var/lib/reth", "reth"),
    "erigon": ("/var/lib/erigon", "erigon"),
}

# Database paths for consensus clients
consensus_client_db_paths = {
    "prysm": ("/var/lib/prysm/beaconchain", "prysmbeacon"),
    "lighthouse": ("/var/lib/lighthouse/beacon", "lighthousebeacon"),
    "teku": ("/var/lib/teku/beacon", "teku"),
    "nimbus": ("/var/lib/nimbus/db", "nimbus"),
    "lodestar": ("/var/lib/lodestar/beacon", "lodestar"),
}

# Combine all database paths
all_client_db_paths = {**execution_client_db_paths, **consensus_client_db_paths}

# Execute database deletion, recreation, and permission setting
print(f"Resetting database for execution/consensus client: {execution_client_delete}")

if execution_client_delete in all_client_db_paths:
    db_path, user = all_client_db_paths[execution_client_delete]
    
    # Remove database folder
    subprocess.run(["sudo", "rm", "-rf", db_path], check=False)
    print(f"Deleted {execution_client_delete} database: {db_path}")

    # Recreate the folder
    subprocess.run(["sudo", "mkdir", "-p", db_path], check=False)
    print(f"Recreated {execution_client_delete} database folder: {db_path}")

    # Set the correct ownership and permissions
    subprocess.run(["sudo", "chown", "-R", f"{user}:{user}", db_path], check=False)
    subprocess.run(["sudo", "chmod", "700", db_path], check=False)
    print(f"Set permissions for {execution_client_delete} database: {db_path}")

elif execution_client_delete == 'none':
    print("No client selected for database reset")
