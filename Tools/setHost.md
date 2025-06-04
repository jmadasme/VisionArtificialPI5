import subprocess
import os

def set_static_ip(interface, ip_address, gateway, dns_servers):
    """
    Sets a static IP address for a specified network interface on a Raspberry Pi.

    Args:
        interface (str): The network interface name (e.g., 'eth0' for Ethernet, 'wlan0' for Wi-Fi).
        ip_address (str): The desired static IP address with CIDR notation (e.g., '192.168.1.100/24').
        gateway (str): The IP address of the default gateway (e.g., '192.168.1.1').
        dns_servers (list): A list of DNS server IP addresses (e.g., ['8.8.8.8', '8.8.4.4']).
    """

    config_path = "/etc/dhcpcd.conf"
    backup_path = "/etc/dhcpcd.conf.backup"

    print(f"Configuring static IP for interface: {interface}")
    print(f"IP Address: {ip_address}")
    print(f"Gateway: {gateway}")
    print(f"DNS Servers: {', '.join(dns_servers)}")

    # Check if the script is run with root privileges
    if os.geteuid() != 0:
        print("Error: This script must be run as root.")
        print("Please run with 'sudo python your_script_name.py'")
        return

    # Create a backup of the original dhcpcd.conf
    try:
        if os.path.exists(config_path) and not os.path.exists(backup_path):
            subprocess.run(["sudo", "cp", config_path, backup_path], check=True)
            print(f"Backup of {config_path} created at {backup_path}")
        elif os.path.exists(backup_path):
            print(f"Backup file already exists at {backup_path}. Skipping backup creation.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating backup: {e}")
        return

    try:
        # Read the current dhcpcd.conf content
        with open(config_path, 'r') as f:
            lines = f.readlines()

        # Prepare the new configuration lines
        new_config_lines = []
        interface_found = False
        skip_lines = False

        for line in lines:
            if line.strip() == f"interface {interface}":
                interface_found = True
                skip_lines = True
                # Skip existing static IP configurations for this interface
                while line.strip() and not line.strip().startswith("static"):
                    new_config_lines.append(line)
                    line = next(iter(lines), None) # Get next line
                    if line is None: break # End of file
                if line is not None:
                    # After skipping existing static config, add this interface line again
                    new_config_lines.append(f"interface {interface}\n")
                else: # If we reached end of file while skipping
                    new_config_lines.append(f"interface {interface}\n")
                    break

            if skip_lines and line.strip().startswith("static"):
                continue # Skip existing static lines

            elif interface_found and not line.strip().startswith("static") and not line.strip().startswith("interface"):
                skip_lines = False # Stop skipping when a non-static/non-interface line is encountered

            if not skip_lines:
                new_config_lines.append(line)

        # If the interface section wasn't found, append it
        if not interface_found:
            new_config_lines.append(f"\ninterface {interface}\n")

        # Add the static IP configuration
        new_config_lines.append(f"static ip_address={ip_address}\n")
        new_config_lines.append(f"static routers={gateway}\n")
        new_config_lines.append(f"static domain_name_servers={' '.join(dns_servers)}\n")

        # Write the new configuration back to dhcpcd.conf
        with open(config_path, 'w') as f:
            f.writelines(new_config_lines)

        print(f"Successfully updated {config_path} with static IP configuration.")

        # Restart dhcpcd service to apply changes
        print("Restarting dhcpcd service...")
        subprocess.run(["sudo", "systemctl", "restart", "dhcpcd"], check=True)
        print("dhcpcd service restarted.")
        print("\nChanges applied. You may need to reboot your Raspberry Pi for full effect:")
        print("sudo reboot")

    except FileNotFoundError:
        print(f"Error: {config_path} not found.")
    except PermissionError:
        print(f"Error: Permission denied when trying to write to {config_path}.")
        print("Please ensure you run the script with 'sudo'.")
    except subprocess.CalledProcessError as e:
        print(f"Error restarting dhcpcd service: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # --- Configuration for your Raspberry Pi ---
    NETWORK_INTERFACE = "eth0"  # Or "wlan0" for Wi-Fi
    STATIC_IP = "192.168.1.150/24"  # Your desired IP address and subnet mask
    GATEWAY_IP = "192.168.1.1"      # Your router's IP address
    DNS_SERVERS = ["8.8.8.8", "8.8.4.4"] # Google's public DNS servers

    set_static_ip(NETWORK_INTERFACE, STATIC_IP, GATEWAY_IP, DNS_SERVERS)